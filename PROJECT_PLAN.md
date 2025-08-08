# Project Plan: Image to WebP Converter

This document outlines the plan for creating a simple utility to convert images to the WebP format.

## 1. Project Goal

To create a user-friendly desktop tool that batch-converts images from a selected folder to WebP format, with specific resizing and padding rules.

## 2. Core Features

- **Graphical User Interface (GUI)**: The tool will have a simple window for all interactions.
- **Source Folder Selection**: A button to allow the user to select a folder containing the images they want to convert.
- **Destination Folder Selection**: A button to allow the user to choose where the converted WebP files will be saved.
- **Quality Control**: A slider (ranging from 1 to 100) to control the quality of the output WebP images.
- **Start Conversion**: A "Convert" button to begin the batch processing.

## 3. UI and User Experience

The application window will be designed for simplicity and clarity, guiding the user through the conversion process step-by-step.

- **Layout**: A single, non-resizable window organized vertically.
  - **Title Bar**: Displays the application name and version number (e.g., "SHH Image to WebP Converter v1.0").
  - **Source Selection**: A label, a non-editable text box for the path, and a `Browse...` button.
  - **Destination Selection**: A label, a non-editable text box for the path, and a `Browse...` button.
  - **Quality Setting**: A label and a horizontal slider (defaulting to 85).
- **User Flow**:
  - The `Convert Images` button will remain disabled until both a source and a destination folder are selected.
  - A status bar at the bottom will provide real-time feedback (e.g., "Ready", "Converting...", "Conversion Complete!").

## 4. Image Processing Logic

For each image processed, the tool will perform the following steps:

1.  **Handle Transparency**: Before processing, the tool will check if an image has a transparency channel (e.g., in a PNG). If it does, the image will be flattened onto a solid white background to prevent black backgrounds in the output.
2.  **Resize to Fit**: The image will be resized to fit within a 500x500 pixel boundary while maintaining its original aspect ratio.
3.  **Pad with White Background**: A new 500x500 pixel canvas with a white background will be created.
4.  **Center the Image**: The resized image will be pasted onto the center of the white canvas.
5.  **Convert to WebP**: The final 500x500 image will be saved in the WebP format in the user-specified destination folder.

## 5. Application Robustness

To ensure a smooth and reliable user experience, the following measures will be implemented:

- **Error Handling**:
  - The application will gracefully skip non-image files or corrupted images.
  - A user-friendly pop-up message will be displayed for critical errors (e.g., no write permissions).
  - The status bar will log the number of successfully converted and skipped files.
- **UI Responsiveness**:
  - The core conversion logic will run in a separate thread to prevent the GUI from freezing, especially when processing a large number of images.

## 6. Technology Stack

- **Language**: Python 3
- **GUI Library**: `tkinter`
- **Image Processing Library**: `Pillow`
- **Threading**: Python's built-in `threading` module.

## 7. File Structure

- `image_converter.py`: The main Python script containing the application code.
- `requirements.txt`: A file listing project dependencies (e.g., `Pillow`, `PyInstaller`).
- `PROJECT_PLAN.md`: This file.
- `PROGRESS_LOG.md`: A file to track development progress.
- `DEV_ENVIRONMENT.md`: Document listing project dependencies and system environment.

## 8. Deployment

After the script has been thoroughly tested and finalized, it will be packaged into a standalone executable (`.exe`) using PyInstaller. A `requirements.txt` file will be used to ensure a consistent and repeatable build process. This will allow the tool to be run on other Windows machines without requiring a Python installation.

---

## Version 2.0 - Planned Features

This section outlines the planned enhancements for Version 2.0 of the application.

### New Core Features

- **Settings Tab**: A new tab will be added to the interface to house advanced configuration options.
- **Customizable Output Dimensions**: Users will be able to specify the exact width and height of the output image.
- **Selectable Output Format**: Users will be able to choose the output format from a dropdown menu (WebP, JPEG, PNG).
- **Persistent Settings**: The application will save the user's settings (dimensions, format, quality) so they are remembered on the next launch.

### Updated UI and User Experience

- **Tabbed Interface**: The main window will be reorganized into two tabs:
  - **Converter**: Contains the primary workflow (source/destination selection, convert button).
  - **Settings**: Contains the new configuration options.
- **Dynamic Quality Slider**: The quality slider will be disabled when the "PNG" format is selected, as it is a lossless format.

### Updated Image Processing Logic

- The image processing engine will be updated to use the custom width, height, and format specified in the settings.
- The "Pad to Fit" logic will correctly resize and pad images to fit within any user-defined rectangular dimensions.

---

## Version 3.0 - Planned Features

This section outlines the planned UI/UX enhancements for Version 3.0.

### New UI/UX Features

- **Theme Selection**: A new option in the "Settings" tab will allow users to switch between a light and dark mode for the application interface. The chosen theme will be saved and loaded between sessions.
- **Drag and Drop**: Users will be able to drag a folder from their file explorer and drop it onto the application window to set the source directory, providing a faster workflow.
- **Live Preview**: A new "Preview" tab will be added. It will show a "before" and "after" thumbnail of the first image in the source folder, which will update in real-time as the user adjusts settings like dimensions and format.

### Updated Technology Stack

- **`ttkthemes`**: This library will be added to manage the light/dark theme switching.
- **`tkinterdnd2`**: This library will be integrated to enable drag-and-drop functionality.

---

## Version 4.0 - AI Background Removal (✅ COMPLETED)

This section outlines the completed features for Version 4.0, focusing on advanced AI-powered image processing capabilities.

### ✅ Implemented Core Features

- **🤖 AI-Powered Background Removal**: Successfully integrated the `rembg` library with U²-Net deep learning model for automatic background removal.
  - Available only when "PNG" is selected as the output format to support transparency.
  - Uses advanced U²-Net neural network for precise edge detection and background separation.
  - Thread-safe session management with lazy loading for optimal performance.
  - Model cache (~176MB) automatically downloaded on first use.

### ✅ Completed Image Processing Logic

- **Enhanced Processing Pipeline**: Updated workflow includes optional AI background removal step before resize/pad/convert operations.
- **Transparency Preservation**: Fixed critical issue where removed backgrounds were being flattened to white - now maintains true transparency.
- **Smart Format Handling**: Automatically switches to PNG format when background removal is enabled to preserve alpha channel.

### ✅ Implementation Results

- **UI Integration**: Added "Remove Background (PNG only)" checkbox in Settings tab with live preview support.
- **Performance Optimization**: Implemented lazy model loading - AI model only loads when feature is first used.
- **Error Resilience**: Comprehensive error handling allows batch processing to continue if background removal fails on individual images.
- **Settings Persistence**: Background removal preference saved automatically in config.json.
- **Live Preview**: Real-time preview shows background removal effects in Preview tab.
- **Build Integration**: Updated PyInstaller configuration to include all required AI dependencies.

### ✅ Technical Achievements

- **Zero Breaking Changes**: All existing functionality preserved while adding advanced AI capabilities.
- **Thread Safety**: Proper locking mechanism prevents concurrent access issues to AI model.
- **Memory Efficiency**: Single model session reused across entire batch processing operation.
- **Transparency Handling**: Proper RGBA channel management with alpha mask support in paste operations.
- **Version 4.0**: Successfully deployed with comprehensive documentation and testing.
