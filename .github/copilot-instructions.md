# Repository custom instructions for GitHub Copilot

Project overview
- Windows desktop GUI (Tkinter + ttkthemes) for batch converting images (Pillow) with optional AI background removal (rembg/U²-Net).
- Target: Multi-file Windows 10/11 x64 executable via PyInstaller. No installer. Shows a loading screen, then launches the main app.
- **Optimized builds**: Fast startup (2-3s) with complete AI functionality.

Tech stack and constraints
- Language/runtime: Python 3.13.5 (Windows-only).
- Key libraries: Pillow, numpy, tkinterdnd2, ttkthemes, rembg, onnxruntime, opencv-python-headless, scipy, PyInstaller.
- Memory: ~1.5GB peak when AI background removal is enabled (CPU). No GPU assumptions.

Repository layout (high value files)
- image_converter.py — main Tkinter app, tabs, drag-and-drop, preview, conversion threads, lazy AI loading via AIManager.
- loading_screen.py — optimized pre-app loading screen; calls launch_main_application().
- config.json — persisted user settings (output_width, output_height, output_format, quality, theme, remove_background).
- **SHH_Image_Converter_v4_Complete.spec** — **primary build spec** for releases (multi-file EXE with AI support).
- SHH_Image_Converter_v4_Fast.spec — lightweight build without AI (fast startup, no background removal).
- SHH_Image_Converter_v4_SingleFile.spec — legacy single-file build (slow startup, avoid for production).
- build-configs/*.spec — historical specs; do not use for releases.
- requirements.txt — pinned dependencies for Python 3.13.
- docs/ — user and technical docs.
- build/, __pycache__/ — generated artifacts; do not edit or commit.

Run and validate (PowerShell)
1) Install deps (fresh or after Python upgrade):
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
2) Run the app:
```
python image_converter.py
```
3) Smoke test in the GUI:
- Drag a folder with images; pick destination; set width/height and format; preview updates; Convert runs without blocking the UI.
- Toggle "Remove Background (PNG only)": quality slider disables; output format switches to PNG; transparency is preserved in preview and output.

Build (multi-file EXE - recommended)
- Primary spec: **SHH_Image_Converter_v4_Complete.spec** (includes AI background removal)
```
python -m PyInstaller .\SHH_Image_Converter_v4_Complete.spec
```
- Alternative: SHH_Image_Converter_v4_Fast.spec (no AI, faster build)
```
python -m PyInstaller .\SHH_Image_Converter_v4_Fast.spec
```
- Expected: Multi-file distribution in dist/ folder; size ~360MB (complete) or ~70MB (fast); startup 2-3s. Do not commit build outputs.

Coding conventions and invariants
- Follow PEP 8; add type hints for new/edited functions.
- UI responsiveness: perform long work on background threads; only update Tk widgets from the main thread.
- Preview logic: keep letterboxing (center paste on a background canvas sized to output dimensions). Do not stretch.
- Transparency:
  - PNG keeps RGBA.
  - JPEG/WebP flatten onto white if source has alpha.
- AI background removal invariants:
  - Enabling "Remove Background" must force PNG format and keep transparency.
  - Rely on a cached rembg session via new_session('u2net') protected by a lock.
- Settings persistence: write/read config.json keys: output_width, output_height, output_format, quality, theme, remove_background. Keep backward-compatible defaults.
- Version: update ImageConverterApp.version in image_converter.py and keep docs/ and release names consistent.

Common pitfalls and notes
- First AI use has a model warmup (adds ~2–3s); startup after packaging takes 2-3s due to optimization.
- rembg/onnxruntime failures should not crash the app; log and continue without AI.
- tkinterdnd2 drag-and-drop requires the TkinterDnD root (already set up in launch_main_application()).
- Avoid editing files in build/ and __pycache__/; regenerate instead.

Validation checklist before proposing changes
- Preview shows before/after correctly; quality slider disables for PNG; AI toggle forces PNG.
- Conversion preserves transparency for PNG and flattens for non-PNG where needed.
- Settings save/load work and theme applies.
- Building via SHH_Image_Converter_v4_Complete.spec produces a working EXE that shows the loading screen and launches.

Search guidance
- Prefer these instructions. Only search the codebase if key information is missing or inconsistent with observed behavior.
