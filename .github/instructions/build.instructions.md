---
applyTo: "**/*.spec"
---

Build guidance
- Prefer `SHH_Image_Converter_v4_Complete.spec` in the repo root for releases with full AI functionality; `SHH_Image_Converter_v4_Fast.spec` for lightweight builds without AI.
- Legacy specs: `SHH_Image_Converter_v4_SingleFile.spec` and specs in `build-configs/` are deprecated (slow startup).
- Do not modify or commit files under `build/` or `__pycache__/`.
- Ensure Pillow, rembg, onnxruntime, numpy, scipy, and tkinter-related imports are discoverable (hiddenimports configured as needed).
- Validate output is a multi-file distribution and launches with optimized loading screen.

Commands (PowerShell)
- Build (Complete with AI):
```
python -m PyInstaller .\SHH_Image_Converter_v4_Complete.spec
```
- Build (Fast without AI):
```
python -m PyInstaller .\SHH_Image_Converter_v4_Fast.spec
```
- Clean (optional): delete `build/`, `dist/` folders before rebuilding.

Checks
- The EXE starts within ~2–3 seconds on all runs.
- AI background removal works offline (U²-Net model downloaded on demand by rembg/pooch) in Complete build.
- Fast build excludes AI libraries for minimal size and fastest startup.
- No unused large assets bundled.
