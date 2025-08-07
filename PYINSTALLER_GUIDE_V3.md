# PyInstaller Integration: Hidden Complexities

## Critical PyInstaller Considerations Missed

### 1. ONNX Runtime Provider Issues

ONNX Runtime may try to load different execution providers that aren't bundled correctly:

```python
# Add to spec file
hiddenimports=[
    'rembg',
    'rembg.session_factory',
    'onnxruntime',
    'onnxruntime.capi',
    'onnxruntime.capi.onnxruntime_pybind11_state',
    'numpy',
    'cv2',
    'gdownload',  # Used by rembg for model downloads
]
```

### 2. Model Path Resolution Issues

In packaged applications, model paths may not resolve correctly:

```python
def get_model_path():
    """Get correct model path in both dev and packaged environments"""
    if hasattr(sys, '_MEIPASS'):
        # Running in PyInstaller bundle
        base_path = sys._MEIPASS
        model_path = os.path.join(base_path, '.u2net')
    else:
        # Running in development
        model_path = os.path.expanduser("~/.u2net")
    
    return model_path

# Usage in session creation
def get_bg_session(self):
    if self.bg_session is None:
        try:
            from rembg import new_session
            # Set model path for packaged app
            model_path = get_model_path()
            if hasattr(sys, '_MEIPASS'):
                os.environ['U2NET_HOME'] = model_path
            
            self.bg_session = new_session("u2net")
        except Exception as e:
            # Fallback error handling
            pass
    return self.bg_session
```

### 3. Spec File Completeness

The current spec file is missing several critical elements:

```python
# Complete spec file additions
import sys
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect all rembg data files
rembg_data = collect_data_files('rembg')

# Get model directory
home_dir = os.path.expanduser("~")
u2net_dir = os.path.join(home_dir, ".u2net")

# Verify models exist
if not os.path.exists(os.path.join(u2net_dir, "u2net.onnx")):
    print("WARNING: u2net.onnx not found. Run download_models.py first!")

a = Analysis(
    ['image_converter.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Existing data files
        ('C:/Users/LWR/AppData/Local/Programs/Python/Python313/Lib/site-packages/tkinterdnd2', 'tkinterdnd2'),
        ('C:/Users/LWR/AppData/Local/Programs/Python/Python313/Lib/site-packages/ttkthemes/themes', 'ttkthemes/themes'),
        
        # rembg model files
        (u2net_dir, '.u2net'),
        
        # rembg package data
        *rembg_data,
    ],
    hiddenimports=[
        'rembg',
        'rembg.session_factory',
        'rembg.sessions',
        'rembg.sessions.u2net',
        'onnxruntime',
        'onnxruntime.capi',
        'onnxruntime.capi.onnxruntime_pybind11_state',
        'numpy',
        'cv2',
        'PIL._tkinter_finder',
        'gdownload',
        'pooch',  # Used by some model downloads
        'requests',  # May be needed for model downloads
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tensorflow',  # Exclude if not needed
        'torch',       # Exclude if not needed
        'matplotlib',  # Exclude if not needed
    ],
    noarchive=False,
    optimize=0,
)

# Remove duplicate entries
seen = set()
a.datas = [x for x in a.datas if not (x[0] in seen or seen.add(x[0]))]
```

### 4. Runtime Environment Variables

Some ONNX configurations may need environment variables set:

```python
# Add to application startup
def setup_runtime_environment():
    """Setup environment variables for packaged app"""
    if hasattr(sys, '_MEIPASS'):
        # Disable ONNX telemetry in packaged app
        os.environ['ORT_DISABLE_TELEMETRY'] = '1'
        
        # Set CPU-only mode
        os.environ['OMP_NUM_THREADS'] = '1'
        
        # Set model cache location
        model_path = os.path.join(sys._MEIPASS, '.u2net')
        if os.path.exists(model_path):
            os.environ['U2NET_HOME'] = model_path

# Call during app initialization
setup_runtime_environment()
```

### 5. Build Validation Script

Create a comprehensive build validation script:

```python
#!/usr/bin/env python3
"""
validate_build.py - Validate PyInstaller build before distribution
"""

import os
import sys
import subprocess
import tempfile

def validate_executable(exe_path):
    """Validate the built executable"""
    print(f"Validating executable: {exe_path}")
    
    # Check file exists and size
    if not os.path.exists(exe_path):
        print("ERROR: Executable not found")
        return False
    
    file_size = os.path.getsize(exe_path) / (1024 * 1024)  # MB
    print(f"Executable size: {file_size:.1f} MB")
    
    if file_size > 300:
        print("WARNING: Executable is very large (>300MB)")
    
    # Test basic execution
    try:
        result = subprocess.run([exe_path, '--help'], 
                              capture_output=True, 
                              timeout=30)
        if result.returncode != 0:
            print("WARNING: Executable returned non-zero exit code")
    except subprocess.TimeoutExpired:
        print("WARNING: Executable seems to hang")
    except Exception as e:
        print(f"ERROR: Cannot execute: {e}")
        return False
    
    return True

def test_background_removal():
    """Test background removal functionality"""
    # This would need to be run with a test image
    pass

if __name__ == "__main__":
    exe_path = sys.argv[1] if len(sys.argv) > 1 else "dist/SHH_Image_Converter_v3.exe"
    validate_executable(exe_path)
```

## Build Process Checklist

### Pre-Build Validation
- [ ] Run `python download_models.py` to ensure models are downloaded
- [ ] Verify model files exist in `~/.u2net/u2net.onnx`
- [ ] Test rembg functionality in development environment
- [ ] Check for dependency conflicts: `pip check`

### Build Process
- [ ] Clean previous builds: `rmdir /s dist build`
- [ ] Build with verbose output: `pyinstaller --log-level DEBUG SHH_Image_Converter_v3.spec`
- [ ] Check build warnings for missing modules
- [ ] Validate executable with `validate_build.py`

### Post-Build Testing
- [ ] Test on machine without Python installed
- [ ] Test without internet connection
- [ ] Test background removal with sample images
- [ ] Monitor memory usage during operation
- [ ] Test with antivirus software enabled

## Common Build Failures & Solutions

### Error: "Module not found: onnxruntime"
**Solution**: Add to hiddenimports, check ONNX Runtime installation

### Error: "Model file not found"
**Solution**: Verify model paths in spec file, run download_models.py

### Error: "Import Error: cv2"
**Solution**: Add opencv-python to requirements.txt and hiddenimports

### Large Executable Size
**Solution**: Review datas section, exclude unnecessary packages

### Slow Startup
**Solution**: Reduce hiddenimports, optimize model loading
