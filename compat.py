"""
Compatibility patches for stable-audio-tools on PyTorch < 2.5.

stable-audio-tools 0.0.19 unconditionally imports
torch.nn.attention.flex_attention (added in PyTorch 2.5).  The feature
is only used when specific mask/score_mod args are passed to the
attention layer — which never happens during standard inference — so we
can safely provide a stub that raises at call time instead of at import
time.
"""

import importlib
import sys
import types

_LOG = "[SCG Foundation-1 compat]"


def _needs_flex_attention_shim():
    try:
        importlib.import_module("torch.nn.attention.flex_attention")
        return False
    except (ImportError, ModuleNotFoundError):
        return True


def _install_flex_attention_shim():
    """
    Create a minimal stub module at torch.nn.attention.flex_attention
    so that stable_audio_tools can import the name without crashing.
    """
    import torch

    # Ensure torch.nn.attention exists as a package
    attn_parent = "torch.nn.attention"
    if attn_parent not in sys.modules:
        mod = types.ModuleType(attn_parent)
        mod.__path__ = []
        mod.__package__ = attn_parent
        sys.modules[attn_parent] = mod
        torch.nn.attention = mod

    # Create the flex_attention sub-module with a stub function
    mod_name = "torch.nn.attention.flex_attention"
    if mod_name not in sys.modules:
        flex_mod = types.ModuleType(mod_name)
        flex_mod.__package__ = attn_parent

        def _flex_attention_stub(*args, **kwargs):
            raise NotImplementedError(
                "flex_attention requires PyTorch >= 2.5.  "
                "This code path should not be reached during normal "
                "Foundation-1 inference."
            )

        flex_mod.flex_attention = _flex_attention_stub
        sys.modules[mod_name] = flex_mod
        sys.modules[attn_parent].flex_attention = flex_mod

    print(f"{_LOG} Installed flex_attention shim (PyTorch < 2.5 detected).")


def apply_patches():
    if _needs_flex_attention_shim():
        _install_flex_attention_shim()
