"""Standalone diagnostic for AI background removal environment.
Run on target machine (same folder as executable or source) with:
    python ai_diagnostic.py
Outputs detailed status and exits 0 on success, non-zero on failure.
"""
import sys, os, time, traceback

RESULT = 1

def log(msg):
    print(f"[DIAG] {msg}")

def find_model_files():
    """Search for rembg model files in common cache locations."""
    import pathlib
    possible_paths = [
        os.path.expanduser("~/.cache/rembg"),
        os.path.expanduser("~/.u2net"),
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "rembg"),
        os.path.join(os.environ.get("APPDATA", ""), "rembg"),
        os.path.join(os.environ.get("USERPROFILE", ""), ".cache", "rembg"),
        os.getcwd(),  # Current directory
    ]
    
    found_models = []
    for path in possible_paths:
        if os.path.exists(path):
            log(f"Found cache dir: {path}")
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(('.onnx', '.pth')):
                        full_path = os.path.join(root, file)
                        size_mb = os.path.getsize(full_path) / (1024*1024)
                        found_models.append((full_path, size_mb))
                        log(f"  Model: {file} ({size_mb:.1f} MB) at {full_path}")
    
    if not found_models:
        log("No model files found in standard cache locations")
    return found_models

try:
    log(f"Python: {sys.version.split()[0]} ({sys.executable})")
    log(f"Platform: {sys.platform}")
    log(f"Working directory: {os.getcwd()}")
    
    # Check for model files before importing
    log("Searching for existing model files...")
    find_model_files()
    
    start = time.time()
    try:
        import onnxruntime as ort
        log(f"onnxruntime version: {ort.__version__}")
        log(f"onnxruntime providers: {ort.get_available_providers()}")
    except Exception as e:
        log(f"onnxruntime import failed: {e}")
        if "DLL load failed" in str(e):
            log("This likely indicates missing Visual C++ Redistributable")
            log("Install from: https://aka.ms/vs/17/release/vc_redist.x64.exe")
        raise

    try:
        import rembg
        log(f"rembg version: {getattr(rembg, '__version__', 'unknown')}")
        log(f"rembg location: {rembg.__file__}")
    except Exception as e:
        log(f"rembg import failed: {e}")
        raise

    # Attempt session creation (this may download model)
    try:
        log("Creating rembg session (u2net)... This may download ~175MB model on first run")
        session_start = time.time()
        session = rembg.new_session('u2net')
        session_time = time.time() - session_start
        log(f"Session created in {session_time:.1f}s")
        
        # Check for model files after session creation
        log("Model files after session creation:")
        find_model_files()
        
    except Exception as e:
        log(f"Session creation failed: {e}\n{traceback.format_exc()}")
        if "HTTP" in str(e) or "download" in str(e).lower() or "network" in str(e).lower():
            log("This appears to be a network/download issue")
            log("The model may need to be bundled with the application for offline use")
        raise

    # Minimal test image (4x4 opaque PNG)
    from io import BytesIO
    from PIL import Image
    test_img = Image.new('RGBA', (4, 4), (255, 0, 0, 255))
    buf = BytesIO()
    test_img.save(buf, format='PNG')
    data = buf.getvalue()
    buf.close()

    try:
        log("Running background removal on tiny test image...")
        removal_start = time.time()
        out_bytes = rembg.remove(data, session=session)
        removal_time = time.time() - removal_start
        
        if not out_bytes:
            raise RuntimeError("No output bytes returned")
        out_img = Image.open(BytesIO(out_bytes))
        log(f"Output mode: {out_img.mode}, size: {out_img.size} (took {removal_time:.1f}s)")
    except Exception as e:
        log(f"Removal failed: {e}\n{traceback.format_exc()}")
        raise

    elapsed = time.time() - start
    log(f"All diagnostics passed in {elapsed:.1f}s")
    RESULT = 0
except Exception:
    log("DIAGNOSTIC FAILED")
finally:
    sys.exit(RESULT)
