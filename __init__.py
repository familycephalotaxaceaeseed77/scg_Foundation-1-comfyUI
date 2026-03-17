"""SCG Foundation-1 Sample Generator – ComfyUI custom node package."""

import importlib
import os

_LOG = "[SCG Foundation-1]"
_INSTALL_OK = True

# Apply compatibility patches BEFORE anything imports stable_audio_tools.
# On PyTorch < 2.5 this shims torch.nn.attention.flex_attention so the
# top-level import in stable_audio_tools doesn't crash.
try:
    from .compat import apply_patches
    apply_patches()
except Exception as e:
    print(f"{_LOG} Warning: could not apply compat patches: {e}")


def _check_dependencies():
    """
    Verify that stable-audio-tools was installed correctly (via install.py
    or --no-deps).  If it's missing, print a loud startup warning so the
    user knows why generation will fail.
    """
    global _INSTALL_OK

    try:
        importlib.import_module("stable_audio_tools")
        return
    except ImportError:
        pass

    _INSTALL_OK = False

    node_dir = os.path.dirname(os.path.abspath(__file__))
    install_script = os.path.join(node_dir, "install.py")

    print("")
    print("=" * 72)
    print(f"  {_LOG}  MISSING DEPENDENCY: stable-audio-tools")
    print("=" * 72)
    print("")
    print("  The Foundation-1 nodes will appear in ComfyUI but will NOT")
    print("  be able to generate audio until this is resolved.")
    print("")
    print("  stable-audio-tools must be installed with --no-deps or it")
    print("  will break your ComfyUI environment.  Do NOT pip install it")
    print("  normally.")
    print("")
    print("  Fix with ONE of:")
    print("")
    print("    1) ComfyUI Manager → Install Missing (runs install.py)")
    print("")
    print(f"    2) python \"{install_script}\"")
    print("")
    print("    3) pip install stable-audio-tools --no-deps")
    print("")
    print("=" * 72)
    print("")


_check_dependencies()

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS  # noqa: E402

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
