---
applyTo: "**/*.spec"
---

Build guidance
- Prefer `SHH_Image_Converter_v4_SingleFile.spec` in the repo root for releases; other specs in `build-configs/` are legacy.
- Do not modify or commit files under `build/` or `__pycache__/`.
- Ensure Pillow, rembg, onnxruntime, numpy, scipy, and tkinter-related imports are discoverable (hiddenimports configured as needed).
- Validate output is a single-file EXE and launches with the loading screen.

Commands (PowerShell)
- Build:
```
python -m PyInstaller .\SHH_Image_Converter_v4_SingleFile.spec
```
- Clean (optional): delete `build/`, `dist/` folders before rebuilding.

Checks
- The EXE starts within ~15–25 seconds on first run.
- AI background removal works offline (U²-Net model downloaded on demand by rembg/pooch).
- No unused large assets bundled.
