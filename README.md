# 🖼️ SHH Image Converter v4.1.1 - AI-Powered Edition

**Professional image conversion tool with AI background removal and optimized startup**

[![Version](https://img.shields.io/badge/Version-4.1.1-blue.svg)](https://github.com/LWR95/ImageToWebp)
[![Python](https://img.shields.io/badge/Python-3.13-green.svg)](https://python.org)
[![AI](https://img.shields.io/badge/AI-U²Net%20Background%20Removal-orange.svg)](https://github.com/danielgatis/rembg)
[![Standalone](https://img.shields.io/badge/Deployment-Multi--File%20EXE-red.svg)](https://pyinstaller.org)

## 🚀 **What's New in v4.1.1**

### 🐛 **Critical Bug Fix**
- **Image Upscaling Fixed**: Small images now properly scale up to target dimensions
- **Preview Consistency**: Final output matches preview exactly for all image sizes
- **Quality Enhancement**: LANCZOS resampling for smooth, high-quality scaling
- **Aspect Ratio**: Maintains proper proportions during upscaling

### ⚡ **Previous v4.1 Achievements**

### ⚡ **Previous v4.1 Achievements**
- **Lightning Fast Startup**: 2-3 seconds (down from 15-25s)
- **Multi-File Distribution**: Optimized deployment for instant loading
- **Smart Build Options**: Choose between Complete (with AI) or Fast (without AI)
- **Lazy AI Loading**: Background removal loads only when needed

### ✨ **AI Background Removal**
- **Deep Learning Model**: U²-Net architecture (downloaded on first use, ~176MB cached)
- **One-Click Operation**: Simple checkbox to enable/disable AI processing
- **Professional Quality**: Maintains transparency and edge detail
- **Batch Processing**: Remove backgrounds from multiple images efficiently
- **Memory Optimized**: Smart session management for large batches

### 🎨 **Enhanced User Experience**
- **Optimized Loading Screen**: Minimal startup delay with professional appearance
- **Modern UI**: Clean, intuitive interface with drag-and-drop support
- **Real-time Preview**: See changes before conversion
- **Status Updates**: Clear feedback during processing
- **Settings Persistence**: Remembers preferences between sessions

### 📦 **Smart Distribution Options**
- **Complete Build**: ~360MB with full AI functionality (2-3s startup)
- **Fast Build**: ~70MB without AI for rapid deployment
- **Multi-File**: Optimized architecture for instant loading
- **Professional Distribution**: Enterprise-ready deployment

## 🎯 **Core Features**

### **Image Processing**
- **🔄 Multi-Format Support**: WebP, JPEG, PNG with intelligent handling
- **📏 Custom Dimensions**: Set output width/height with letterboxing
- **⚙️ Quality Control**: Adjustable compression (1-100) for WebP/JPEG; disabled for PNG
- **🔍 Transparency**: Preserves PNG transparency, flattens others to white
- **⚡ Batch Processing**: Convert entire folders with progress tracking

### **AI Background Removal**
- **🤖 Advanced AI**: U²-Net deep learning model for precise cutouts
- **🎯 Professional Results**: Clean edges with transparency preservation
- **💾 PNG Output**: Automatically switches to PNG for transparency
- **🚀 Fast Processing**: Optimized for speed and memory efficiency
- **🎨 Design Ready**: Perfect for compositing and graphic design

## 📋 **System Requirements**

- **Operating System**: Windows 10/11 (64-bit)
- **Memory**: 4GB RAM minimum, 8GB recommended for AI processing
- **Storage**: 
  - Complete Build: ~360MB (includes AI functionality)
  - Fast Build: ~70MB (basic conversion only)
  - AI Model Cache: ~176MB (downloaded on first AI use)
- **Dependencies**: None - completely standalone

## 🚀 **Quick Start**

### **Using the Standalone Executable**

1. **Download**: Get the `SHH_Image_Converter_v4_Complete` folder (recommended)
   - **Complete**: Full AI functionality (~360MB, 2-3s startup)
   - **Fast**: Basic conversion only (~70MB, instant startup)
2. **Launch**: Run `SHH_Image_Converter_v4_Complete.exe` (loads in 2-3 seconds)
3. **Select Source**: Drag folder onto window or use Browse button
4. **Select Destination**: Choose output folder for converted images
5. **Configure Settings**:
   - Set output dimensions and format
   - Enable AI background removal if needed (forces PNG, disables quality)
   - Adjust quality settings for WebP/JPEG
6. **Preview**: Check the Preview tab to see results before conversion
7. **Convert**: Click Convert Images to start batch processing

### **Build Options (PowerShell)**
```powershell
# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Run from source
python image_converter.py

# Build complete version (recommended - includes AI)
python -m PyInstaller .\SHH_Image_Converter_v4_Complete.spec

# Build fast version (no AI, smaller size)
python -m PyInstaller .\SHH_Image_Converter_v4_Fast.spec
```

## 📊 **Performance & Technical Details**

| Build Type | Startup Time | Size | AI Background Removal | Best For |
|------------|-------------|------|---------------------|----------|
| **Complete** | 2-3s | ~360MB | ✅ Full functionality | Production use |
| **Fast** | <1s | ~70MB | ❌ Not included | Quick deployment |
| Legacy Single-File | 15-25s | ~150MB | ✅ Included | Archive only |

- **AI Warmup**: 2–3s on first AI use (model loading)
- **Memory Usage**: ~1.5GB during AI processing
- **Safety**: Numeric fields are validated; empty/invalid width/height fall back to defaults
- **Threading**: UI remains responsive during conversion

## 🗂️ **Project Structure**

```
ImageToWebp/
├── image_converter.py      # Main application code (GUI, preview, conversion, AIManager)
├── loading_screen.py       # Optimized startup loading screen
├── config.json             # User settings
├── requirements.txt        # Pinned dependencies
├── SHH_Image_Converter_v4_Complete.spec    # Primary build (with AI)
├── SHH_Image_Converter_v4_Fast.spec        # Fast build (no AI)
├── SHH_Image_Converter_v4_SingleFile.spec  # Legacy build (deprecated)
├── .github/
│   ├── copilot-instructions.md
│   └── instructions/
│       ├── build.instructions.md
│       ├── gui.instructions.md
│       ├── docs.instructions.md
│       └── deps.instructions.md
├── docs/                   # User and technical docs
└── README.md
```

## 📈 **Version History**

- **v4.1**: Performance optimization (2-3s startup), multi-file builds, lazy AI loading
- **v4.0**: AI background removal + loading screen + single-file EXE
- Earlier versions: batch processing, themes, preview, basic conversion

## 🤝 **Contributing**

Contributions welcome. Follow PEP 8, add type hints for new functions, and keep UI work off the main thread.

---

**SHH Image Converter v4.1** - Professional image processing with AI-powered background removal and lightning-fast startup
