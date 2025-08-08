# 🖼️ SHH Image Converter v4.0 - AI-Powered Edition

**Professional image conversion tool with AI background removal and loading screen**

[![Version](https://img.shields.io/badge/Version-4.0-blue.svg)](https://github.com/LWR95/ImageToWebp)
[![Python](https://img.shields.io/badge/Python-3.13-green.svg)](https://python.org)
[![AI](https://img.shields.io/badge/AI-U²Net%20Background%20Removal-orange.svg)](https://github.com/danielgatis/rembg)
[![Standalone](https://img.shields.io/badge/Deployment-Standalone%20EXE-red.svg)](https://pyinstaller.org)

## 🚀 **What's New in v4.0**

### ✨ **AI Background Removal**
- **Deep Learning Model**: U²-Net architecture (176MB) for professional results
- **One-Click Operation**: Simple checkbox to enable/disable AI processing
- **Professional Quality**: Maintains transparency and edge detail
- **Batch Processing**: Remove backgrounds from multiple images efficiently
- **Memory Optimized**: Smart session management for large batches

### 🎨 **Enhanced User Experience**
- **Professional Loading Screen**: Progress indicator during 15-25 second startup
- **Modern UI**: Clean, intuitive interface with drag-and-drop support
- **Real-time Preview**: See changes before conversion
- **Status Updates**: Clear feedback during processing
- **Settings Persistence**: Remembers preferences between sessions

### 📦 **True Standalone Deployment**
- **Single File**: 147MB executable with zero dependencies
- **Fresh PC Ready**: Works on any Windows computer without installation
- **No Runtime Required**: Python, Visual C++, or dependencies not needed
- **Professional Distribution**: Enterprise-ready deployment

## 🎯 **Core Features**

### **Image Processing**
- **🔄 Multi-Format Support**: WebP, JPEG, PNG with intelligent handling
- **📏 Custom Dimensions**: Set output width/height with letterboxing
- **⚙️ Quality Control**: Adjustable compression (1-100) for WebP/JPEG
- **🔍 Transparency**: Preserves PNG transparency, flattens others to white
- **⚡ Batch Processing**: Convert entire folders with progress tracking

### **AI Background Removal**
- **🤖 Advanced AI**: U²-Net deep learning model for precise cutouts
- **🎯 Professional Results**: Clean edges with transparency preservation
- **💾 PNG Output**: Automatically switches to PNG for transparency
- **🚀 Fast Processing**: Optimized for speed and memory efficiency
- **🎨 Design Ready**: Perfect for compositing and graphic design

### **User Interface**
- **📁 Drag & Drop**: Direct folder selection via drag-and-drop
- **🎨 Theme Selection**: Multiple light and dark themes
- **🖼️ Live Preview**: Real-time preview with all settings applied
- **📊 Progress Tracking**: Visual feedback during batch operations
- **💾 Auto-Save**: Settings automatically saved between sessions

## 📋 **System Requirements**

- **Operating System**: Windows 10/11 (64-bit)
- **Memory**: 4GB RAM minimum, 8GB recommended for AI processing
- **Storage**: 200MB free space for application and temp files
- **Dependencies**: None - completely standalone

## 🚀 **Quick Start**

### **Using the Standalone Executable**

1. **Download**: Get `SHH_Image_Converter_v4_SingleFile.exe` (147MB)
2. **Launch**: Double-click to start (shows professional loading screen)
3. **Select Source**: Drag folder onto window or use Browse button
4. **Select Destination**: Choose output folder for converted images
5. **Configure Settings**:
   - Set output dimensions and format
   - Enable AI background removal if needed
   - Adjust quality settings
6. **Preview**: Check the Preview tab to see results before conversion
7. **Convert**: Click Convert Images to start batch processing

### **AI Background Removal**

1. **Enable**: Check "Remove Background (PNG only)" in Settings
2. **Auto-Format**: Output automatically switches to PNG for transparency
3. **Preview**: See AI results in real-time preview
4. **Process**: Convert images with backgrounds automatically removed
5. **Results**: Professional transparent PNG files ready for use

## 🔧 **Advanced Usage**

### **Settings Optimization**
- **Quality**: Use 80-95 for WebP, 85-100 for JPEG
- **Dimensions**: Common sizes: 500x500, 1024x1024, 1920x1080
- **AI Processing**: Enable only when transparency needed (slower)
- **Themes**: Choose theme for comfortable extended use

### **Batch Processing Tips**
- **Large Batches**: AI processing uses ~1.5GB RAM per session
- **Mixed Formats**: Tool handles different input formats automatically
- **Progress Monitoring**: Status bar shows current file and overall progress
- **Error Handling**: Skipped files reported at completion

## 📊 **Performance & Technical Details**

### **Startup Performance**
- **First Launch**: 15-25 seconds with professional loading screen
- **Subsequent Launches**: 3-5 seconds (cached extraction)
- **AI Model Loading**: Additional 2-3 seconds when first used
- **Memory Usage**: ~1.5GB during AI processing, 200MB normal operation

### **Technical Specifications**
- **Python Runtime**: 3.13.5 embedded
- **AI Framework**: ONNX Runtime with U²-Net model
- **UI Framework**: tkinter with ttkthemes
- **Image Processing**: PIL, OpenCV, NumPy, SciPy
- **Build Tool**: PyInstaller 6.15.0 single-file mode

## 🗂️ **Project Structure**

```
ImageToWebp/
├── image_converter.py      # Main application code
├── loading_screen.py       # Professional startup screen
├── config.json            # User settings persistence
├── requirements.txt        # Python dependencies
├── SHH_Image_Converter_v4_SingleFile.spec  # Build configuration
├── dist/                  # Built executables
├── build-configs/         # Historical build configurations
├── docs/                  # Essential documentation (4 files)
└── README.md              # This file
```

## 📚 **Documentation**

- **[docs/USER_GUIDE.md](docs/USER_GUIDE.md)** - Complete user and deployment guide
- **[docs/TECHNICAL_GUIDE.md](docs/TECHNICAL_GUIDE.md)** - Technical implementation details
- **[docs/DEVELOPMENT_HISTORY.md](docs/DEVELOPMENT_HISTORY.md)** - Development progress and milestones
- **[docs/PROJECT_PLAN.md](docs/PROJECT_PLAN.md)** - Original project specifications

## 🔄 **Development**

### **Running from Source**

```bash
# Clone repository
git clone https://github.com/LWR95/ImageToWebp.git
cd ImageToWebp

# Install dependencies
pip install -r requirements.txt

# Run application
python image_converter.py
```

### **Building Standalone**

```bash
# Build single-file executable
pyinstaller SHH_Image_Converter_v4_SingleFile.spec

# Output: dist/SHH_Image_Converter_v4_SingleFile.exe
```

## 🎉 **Success Stories**

✅ **Enterprise Ready**: Zero-dependency deployment  
✅ **Professional UI**: Loading screen eliminates startup confusion  
✅ **AI Integration**: State-of-the-art background removal  
✅ **Batch Efficiency**: Process hundreds of images automatically  
✅ **User Friendly**: Intuitive interface with real-time preview  

## 📈 **Version History**

- **v4.0**: AI background removal + professional loading screen + standalone deployment
- **v3.0**: AI background removal integration
- **v2.0**: Batch processing and theme support
- **v1.0**: Basic image conversion functionality

## 🤝 **Contributing**

Contributions welcome! Please read the project documentation and submit pull requests for review.

## 📄 **License**

This project is open source. See project files for details.

---

**SHH Image Converter v4.0** - Professional image processing with AI-powered background removal
