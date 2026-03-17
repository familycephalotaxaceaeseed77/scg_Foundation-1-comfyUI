"""
Install script for SCG Foundation-1 Sample Generator.

stable-audio-tools has extremely aggressive version pinning for training
dependencies (pandas==2.0.2, numpy==1.23.5, wandb==0.15.4, etc.) that
will destroy a working ComfyUI environment if installed normally.

We only need the inference code path, so we install it with --no-deps
and provide the handful of lightweight inference deps separately via
requirements.txt.
"""

import subprocess
import sys


def pip_install(*args):
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", *args],
        stdout=sys.stdout,
        stderr=sys.stderr,
    )


def is_installed(package):
    try:
        __import__(package)
        return True
    except ImportError:
        return False


if __name__ == "__main__":
    if not is_installed("stable_audio_tools"):
        print("[SCG Foundation-1] Installing stable-audio-tools (--no-deps to avoid conflicts)...")
        pip_install("stable-audio-tools", "--no-deps")
    else:
        print("[SCG Foundation-1] stable-audio-tools already installed.")

    deps = [
        ("huggingface_hub", "huggingface_hub"),
        ("einops", "einops"),
        ("safetensors", "safetensors"),
        ("alias_free_torch", "alias-free-torch"),
        ("einops_exts", "einops-exts"),
        ("local_attention", "local-attention"),
        ("ema_pytorch", "ema-pytorch"),
    ]
    missing = [(mod, pkg) for mod, pkg in deps if not is_installed(mod)]
    if missing:
        pkgs = [pkg for _, pkg in missing]
        print(f"[SCG Foundation-1] Installing missing deps: {', '.join(pkgs)}")
        pip_install(*pkgs)
    else:
        print("[SCG Foundation-1] All inference dependencies satisfied.")
