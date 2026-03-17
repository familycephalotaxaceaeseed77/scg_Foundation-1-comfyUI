# SCG Foundation-1 Sample Generator

ComfyUI nodes for [**Foundation-1**](https://huggingface.co/RoyalCities/Foundation-1) by [RoyalCities](https://huggingface.co/RoyalCities) — a structured text-to-sample model for music production. Generates tempo-synced, key-aware loops with deep control over instrumentation, timbre, FX, and musical structure.

## Screenshots

<img width="1052" height="809" alt="image" src="https://github.com/user-attachments/assets/50b01da0-ed22-4c48-a014-872eba9a8a7e" />


## Credits

This node wraps the **Foundation-1** model created by **RoyalCities**.

- Model: [RoyalCities/Foundation-1 on HuggingFace](https://huggingface.co/RoyalCities/Foundation-1)
- Built on [Stability AI's stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools)
- Prompt system and tag vocabulary informed by the [RC Enhanced Fork](https://github.com/RoyalCities/RC-stable-audio-tools)

All model weights are downloaded directly from the original HuggingFace repository. This project provides only the ComfyUI integration layer.

## Installation

> **Do NOT run `pip install -r requirements.txt` by itself.**
>
> This node depends on `stable-audio-tools`, which pins dozens of
> training-only dependencies to old versions (torch 2.10, numpy 1.23,
> pandas 2.0, etc.) and **will break your ComfyUI environment** if
> installed normally.

### Option 1 — ComfyUI Manager (recommended)

Install through the ComfyUI Manager UI. It will run `install.py`
automatically, which handles the `--no-deps` install.

### Option 2 — Run the install script

```bash
cd ComfyUI/custom_nodes/scg_Foundation-1-comfyUI
python install.py
```

### Option 3 — Manual pip (two steps, in order)

```bash
pip install stable-audio-tools --no-deps
pip install -r requirements.txt
```

## Nodes

| Node | Purpose |
|------|---------|
| **SCG Foundation-1 Loader** | Downloads the model from HuggingFace on first use (~1.5 GB) and loads it onto GPU. Caches in `ComfyUI/models/audio_checkpoints/Foundation-1/`. |
| **SCG Foundation-1 Sample Generator** | Main generation node. Set BPM, bars, key, scale, sampler params, and seed. Outputs ComfyUI `AUDIO` with built-in preview player. Supports negative prompts and audio-to-audio style transfer. |
| **SCG Foundation-1 Prompt Builder** | Build structured prompts from dropdowns — instrument family, sub-family, timbre, FX, spatial, structure, speed, density, and more. |
| **SCG Foundation-1 Random Prompt** | Weighted random prompt generation in Simple or Experimental mode, matching the RC Enhanced Fork's random prompt system. |

## Typical workflow

```
[Loader] ──→ [Sample Generator] ──→ [Save Audio / Preview Audio]
                     ↑
        [Prompt Builder] or [Random Prompt]
```

The prompt nodes output a `STRING` with instrument/timbre/FX/structure tags.
The Sample Generator appends key, scale, bars, and BPM automatically and
handles all timing alignment for loop-accurate output.

## Supported parameters

**Musical controls:** 4 or 8 bars · 100–150 BPM · All 12 keys · Major/minor

**Sampler:** dpmpp-3m-sde (default), dpmpp-2m-sde, k-heun, k-lms, k-dpmpp-2s-ancestral, k-dpm-2, k-dpm-fast · 1–500 steps · CFG 0–25 · Sigma min/max

**Style transfer:** Connect any `AUDIO` input as init audio with adjustable noise level

**Prompt tags:** 10 instrument families · 40+ sub-families · 50 timbre descriptors · 11 spatial tags · 13 wave/tech tags · 11 style tags · Reverb/delay/distortion/modulation FX with graduated levels · Structure, speed, density, contour, rhythm controls

## Hardware requirements

~7 GB VRAM during generation. A GPU with at least 8 GB VRAM is recommended.

## License

The Foundation-1 model is licensed under the [Stability AI Community License](https://huggingface.co/RoyalCities/Foundation-1) (non-commercial, or commercial under $1M revenue).
