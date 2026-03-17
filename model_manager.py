"""
Foundation-1 model download, loading, and caching.
Handles auto-download from HuggingFace and GPU memory management.
"""

import os
import gc
import json
import torch
import folder_paths

try:
    import comfy.model_management as model_management
except ImportError:
    model_management = None

HF_REPO_ID = "RoyalCities/Foundation-1"
MODEL_FILENAME = "Foundation_1.safetensors"
CONFIG_FILENAME = "model_config.json"
MODEL_SUBDIR = "Foundation-1"

LOG_PREFIX = "[SCG Foundation-1]"

_cached_model = None
_cached_config = None


def get_models_directory():
    """Return the directory where Foundation-1 model files are stored."""
    base = folder_paths.models_dir
    model_dir = os.path.join(base, "audio_checkpoints", MODEL_SUBDIR)
    os.makedirs(model_dir, exist_ok=True)
    return model_dir


def _model_files_present():
    """Check if model files already exist locally."""
    model_dir = get_models_directory()
    ckpt_path = os.path.join(model_dir, MODEL_FILENAME)
    config_path = os.path.join(model_dir, CONFIG_FILENAME)
    return os.path.isfile(ckpt_path) and os.path.isfile(config_path)


def download_model():
    """Download Foundation-1 model from HuggingFace if not already present."""
    if _model_files_present():
        print(f"{LOG_PREFIX} Model files already present.")
        return get_models_directory()

    print(f"{LOG_PREFIX} Downloading Foundation-1 from {HF_REPO_ID}...")

    try:
        from huggingface_hub import hf_hub_download
    except ImportError:
        raise RuntimeError(
            f"{LOG_PREFIX} huggingface_hub is required for auto-download.\n"
            "Install with: pip install huggingface_hub"
        )

    model_dir = get_models_directory()

    for filename in (MODEL_FILENAME, CONFIG_FILENAME):
        target = os.path.join(model_dir, filename)
        if os.path.isfile(target):
            print(f"{LOG_PREFIX} {filename} already exists, skipping.")
            continue

        print(f"{LOG_PREFIX} Downloading {filename}...")
        downloaded = hf_hub_download(
            repo_id=HF_REPO_ID,
            filename=filename,
            local_dir=model_dir,
            local_dir_use_symlinks=False,
        )
        print(f"{LOG_PREFIX} Downloaded {filename} → {downloaded}")

    print(f"{LOG_PREFIX} Download complete.")
    return model_dir


def load_model(device="auto", force_reload=False):
    """
    Load the Foundation-1 model and config.

    Returns:
        (model, model_config) tuple. The model is moved to the requested device.
    """
    global _cached_model, _cached_config

    if _cached_model is not None and not force_reload:
        print(f"{LOG_PREFIX} Using cached model.")
        return _cached_model, _cached_config

    download_model()

    model_dir = get_models_directory()
    ckpt_path = os.path.join(model_dir, MODEL_FILENAME)
    config_path = os.path.join(model_dir, CONFIG_FILENAME)

    print(f"{LOG_PREFIX} Loading model config from {config_path}")
    with open(config_path, "r") as f:
        model_config = json.load(f)

    try:
        from stable_audio_tools.models.factory import create_model_from_config
        from stable_audio_tools.models.utils import load_ckpt_state_dict
    except ImportError:
        raise RuntimeError(
            f"{LOG_PREFIX} stable-audio-tools is required.\n"
            "Install with: pip install stable-audio-tools"
        )

    print(f"{LOG_PREFIX} Building model from config (this may download t5-base tokenizer on first run)...")
    model = create_model_from_config(model_config)

    print(f"{LOG_PREFIX} Loading checkpoint weights from {ckpt_path}")
    state_dict = load_ckpt_state_dict(ckpt_path)

    model.load_state_dict(state_dict, strict=False)
    del state_dict
    gc.collect()

    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"

    print(f"{LOG_PREFIX} Moving model to {device}")
    model = model.to(device)
    model.eval()

    _cached_model = model
    _cached_config = model_config

    vram_gb = torch.cuda.memory_allocated() / (1024 ** 3) if device == "cuda" else 0
    print(f"{LOG_PREFIX} Model loaded. VRAM usage: {vram_gb:.1f} GB")

    return model, model_config


def unload_model():
    """Unload the cached model and free memory."""
    global _cached_model, _cached_config

    if _cached_model is not None:
        try:
            _cached_model.to("cpu")
        except Exception as e:
            print(f"{LOG_PREFIX} Warning: could not move model to CPU during unload: {e}")
        _cached_model = None
        _cached_config = None

    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()
    print(f"{LOG_PREFIX} Model unloaded.")


def is_model_loaded():
    return _cached_model is not None
