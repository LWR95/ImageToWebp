# SHH Image to WebP Converter

A powerful desktop utility for batch image conversion with AI-powered background removal, supporting WebP, JPEG, and PNG formats with intelligent quality control and live preview.

## Features (Version 3.0 with AI Background Removal)

- **🤖 AI-Powered Background Removal**: Automatically remove backgrounds from images using advanced U²-Net deep learning models, producing transparent PNG outputs perfect for compositing and design work.
- **🖼️ Responsive Live Preview**: See real-time previews of your conversion settings, including background removal effects. Preview images automatically scale to fit the viewing area.
- **🎨 Theme Selection**: Choose from a variety of light and dark themes in the "Settings" tab to customize the application's appearance.
- **📁 Drag and Drop**: Easily select your source folder by dragging it directly onto the application window.
- **🔄 Multi-Format Conversion**: Convert images to WebP, JPEG, or PNG with intelligent format handling.
- **📏 Custom Dimensions**: Set custom output width and height for converted images with letterboxing support.
- **⚙️ Adjustable Quality**: Control quality settings for WebP and JPEG formats (1-100 scale).
- **💾 Settings Persistence**: Your chosen dimensions, format, quality, theme, and background removal preferences are saved automatically.
- **⚡ Batch Processing**: Convert all images in a selected folder at once with progress tracking.
- **🔍 Intelligent Transparency**: Preserves transparency for PNG outputs and flattens to white background for other formats.
- **📦 Standalone Executable**: Packaged as a single `.exe` file that runs on Windows without dependencies.

## How to Use

### Using the Executable

1.  Navigate to the `dist/` folder.
2.  Double-click `SHH_Image_Converter_v3.exe` (or the latest version) to run the application.
3.  **Select Source**:
    - **Drag and Drop**: Drag the folder containing your source images directly onto the main window.
    - **Browse**: Alternatively, click the **Browse...** button to select the folder.
4.  **Select Destination**:
    - Click the second **Browse...** button to select the destination folder for the converted images.
5.  **(Optional) Adjust Settings**:
    - **Preview**: Click the **Preview** tab to see a live preview of the first image with current settings applied, including background removal effects.
    - **Settings Tab**:
        - Set your desired **Output Width**, **Output Height**, and **Output Format**.
        - **🔥 NEW**: Check **Remove Background (PNG only)** to automatically remove image backgrounds using AI. This automatically switches output format to PNG to preserve transparency.
        - Choose a new **Theme** for the application.
        - Click **Save Settings** to make them the new default.
6.  **Convert**:
    - On the **Converter** tab, adjust the **Quality** slider if needed (disabled for PNG format).
    - Click the **Convert Images** button to start batch processing.
7.  A confirmation message will appear when conversion is complete, showing successfully converted and skipped file counts.

### Running from Source

If you want to run the application from the source code, you will need Python 3 and the dependencies listed in `requirements.txt`.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/LWR95/ImageToWebp.git
    cd ImageToWebp
    ```

2.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```sh
    python image_converter.py
    ```

## Project Documentation

For more detailed information about the project's architecture, features, and development process, please see the following documents:

-   `PROJECT_PLAN.md`: Outlines the project goals, features, and technical specifications.
-   `PROGRESS_LOG.md`: Tracks the development progress and milestones.
-   `DEV_ENVIRONMENT.md`: Lists the development tools and environment setup.
