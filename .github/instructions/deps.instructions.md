---
applyTo: "requirements.txt"
---

Dependency rules
- Python runtime: 3.13.x on Windows x64. Validate compatibility of rembg, onnxruntime, Pillow, and PyInstaller before bumping Python or majors.
- Keep `opencv-python-headless` (no GUI bindings) to reduce EXE size.
- rembg is CPU-only here; do not add GPU backends (CUDA) unless the build and runtime story are updated.
- Keep `pyinstaller` and `pyinstaller-hooks-contrib` versions aligned; bump together and test a full build.
- After editing requirements, run a clean install and smoke test run + build:
```
python -m pip install --upgrade pip
python -m pip install --force-reinstall -r requirements.txt
python image_converter.py
python -m PyInstaller .\SHH_Image_Converter_v4_SingleFile.spec
```
- Prefer pinning exact versions; avoid unpinned dependencies.
