# Technical Implementation Guide

## AI Background Removal Implementation

### **Model Selection**
- **Chosen**: U²-Net architecture via rembg library
- **Reason**: Best balance of quality, size, and compatibility
- **Model Delivery**: Downloaded on first use (~176MB) via rembg/pooch and cached in the user profile (platformdirs). No manual setup required.
- **Performance**: 2-3 seconds warmup on first AI use; per-image time depends on hardware

### **Integration Approach**
- **Thread Safety**: Background processing in separate thread
- **Memory Management**: Session reuse (cached `new_session('u2net')`) to prevent model reloading
- **Error Handling**: Graceful degradation if AI fails; continue without AI and log a warning
- **UI Integration**: Checkbox toggle with automatic PNG output and quality slider disable for PNG

### **PyInstaller Configuration**
```python
# Key settings for successful build (see SHH_Image_Converter_v4_SingleFile.spec)
a = Analysis(
    ['image_converter.py'],
    datas=[('config.json', '.' )],  # persist settings in packaged app
    hiddenimports=[
        # UI
        'tkinter', 'tkinterdnd2', 'ttkthemes', 'PIL', 'PIL.Image', 'PIL.ImageTk',
        # AI & image processing
        'rembg', 'onnxruntime', 'numpy', 'cv2', 'scipy',
        # Model download plumbing used by rembg
        'requests', 'urllib3', 'pooch', 'platformdirs', 'filelock', 'tqdm', 'gdown',
    ],
    # ...other spec fields...
)
exe = EXE(..., console=False, upx=True)
```

### **Deployment Solutions**
- **Single-File Mode**: Eliminates dependency issues
- **Model Caching**: AI model auto-downloads once, then reused from cache
- **Fresh PC Testing**: Verified zero external runtimes required
- **Loading Screen**: Professional startup experience

### **Performance Optimization**
- **Lazy Loading**: AI model loads only when first used
- **Memory**: ~1.5GB peak during AI processing on CPU
- **Threading**: Non-blocking UI during AI processing
- **Resource Management**: Reuse session, avoid reallocation within loops

## Build Process

### **Requirements**
- Python 3.13.5
- PyInstaller 6.15.0
- All dependencies in requirements.txt (pinned)

### **Build Command (PowerShell)**
```powershell
python -m PyInstaller .\SHH_Image_Converter_v4_SingleFile.spec
```

### **Output**
- Single executable (~100–200MB)
- Works on fresh Windows 10/11 systems
- On first AI use, downloads model (~176MB) if not present in cache

## Robustness and UX Notes
- Safely parse numeric settings to avoid Tkinter TclError when fields are empty; invalid values fall back to sane defaults.
- Update Tk widgets only from the main thread; run conversions and AI in background threads.
