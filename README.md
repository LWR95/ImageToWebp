# 🖼️ SHH Image Converter v4.0 - AI-Powered Edition

**Professional image conversion tool with AI background removal and loading screen**

[![Version](https://img.shields.io/badge/Version-4.0-blue.svg)](https://github.com/LWR95/ImageToWebp)
[![Python](https://img.shields.io/badge/Python-3.13-green.svg)](https://python.org)
[![AI](https://img.shields.io/badge/AI-U²Net%20Background%20Removal-orange.svg)](https://github.com/danielgatis/rembg)
[![Standalone](https://img.shields.io/badge/Deployment-Standalone%20EXE-red.svg)](https://pyinstaller.org)

## 🚀 **What's New in v4.0**

### ✨ **AI Background Removal**
- **Deep Learning Model**: U²-Net architecture (downloaded on first use, ~176MB cached)
- **One-Click Operation**: Simple checkbox to enable/disable AI processing
- **Professional Quality**: Maintains transparency and edge detail
- **Batch Processing**: Remove backgrounds from multiple images efficiently
- **Memory Optimized**: Smart session management for large batches

### 🎨 **Enhanced User Experience**
- **Professional Loading Screen**: Progress indicator during startup (15–25s for single-file EXE)
- **Modern UI**: Clean, intuitive interface with drag-and-drop support
- **Real-time Preview**: See changes before conversion
- **Status Updates**: Clear feedback during processing
- **Settings Persistence**: Remembers preferences between sessions

### 📦 **True Standalone Deployment**
- **Single File**: ~100–200MB executable with zero external runtimes
- **Fresh PC Ready**: Works on any Windows computer without installation
- **No Runtime Required**: Python or VC++ not required by user
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
- **Storage**: 200MB+ for app and cache; initial AI use downloads ~176MB model
- **Dependencies**: None - completely standalone

## 🚀 **Quick Start**

### **Using the Standalone Executable**

1. **Download**: Get `SHH_Image_Converter_v4_SingleFile.exe`
2. **Launch**: Double-click to start (shows professional loading screen)
3. **Select Source**: Drag folder onto window or use Browse button
4. **Select Destination**: Choose output folder for converted images
5. **Configure Settings**:
   - Set output dimensions and format
   - Enable AI background removal if needed (forces PNG, disables quality)
   - Adjust quality settings for WebP/JPEG
6. **Preview**: Check the Preview tab to see results before conversion
7. **Convert**: Click Convert Images to start batch processing

### **Run/Build from Source (PowerShell)**
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python image_converter.py
# Build single-file executable
python -m PyInstaller .\SHH_Image_Converter_v4_SingleFile.spec
```

## 📊 **Performance & Technical Details**

- **First Launch**: 15–25s (single-file extraction)
- **AI Warmup**: 2–3s on first AI use
- **Memory Usage**: ~1.5GB during AI processing
- **Safety**: Numeric fields are validated; empty/invalid width/height fall back to defaults

## 🗂️ **Project Structure**

```
ImageToWebp/
├── image_converter.py      # Main application code (GUI, preview, conversion, AI session caching)
├── loading_screen.py       # Startup loading screen
├── config.json             # User settings
├── requirements.txt        # Pinned dependencies
├── SHH_Image_Converter_v4_SingleFile.spec  # Build configuration
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

- **v4.0**: AI background removal + loading screen + single-file EXE
- Earlier versions: batch processing, themes, preview, basic conversion

## 🤝 **Contributing**

Contributions welcome. Follow PEP 8, add type hints for new functions, and keep UI work off the main thread.

---

**SHH Image Converter v4.0** - Professional image processing with AI-powered background removal
