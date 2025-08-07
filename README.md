# SHH Image to WebP Converter

A simple desktop utility to batch-convert images to the WebP format, with options for resizing and quality control.

## Features (Version 3.0)

- **Responsive Live Preview**: See a real-time preview of your conversion settings. The preview images automatically scale to fit the viewing area, preventing overflow.
- **Theme Selection**: Choose from a variety of light and dark themes in the "Settings" tab to customize the application's appearance.
- **Drag and Drop**: Easily select your source folder by dragging it directly onto the application window.
- **Multi-Format Conversion**: Convert images to WebP, JPEG, or PNG.
- **Custom Dimensions**: Set custom output width and height for the converted images.
- **Adjustable Quality**: Control the quality setting for WebP and JPEG formats.
- **Settings Persistence**: Your chosen dimensions, format, quality, and theme are saved in a `config.json` file and loaded automatically on startup.
- **Batch Processing**: Convert all images in a selected folder at once.
- **Intelligent Transparency**: Preserves transparency when converting to PNG and flattens it onto a white background for other formats.
- **AI-Powered Background Removal**: For PNG outputs, you can choose to automatically remove the image background using a sophisticated AI model.
- **Standalone Executable**: Packaged as a single `.exe` file that runs on Windows without needing Python or any other dependencies.

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
    - **Preview**: Click the **Preview** tab to see a live preview of the first image with the current settings applied.
    - **Settings Tab**:
        - Set your desired **Output Width**, **Output Height**, and **Output Format**.
        - If you select **PNG** as the output, you can also check the **Remove Background** option.
        - Choose a new **Theme** for the application.
        - Click **Save Settings** to make them the new default.
6.  **Convert**:
    - On the **Converter** tab, adjust the **Quality** slider if needed.
    - Click the **Convert Images** button.
7.  A confirmation message will appear when the conversion is complete.

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
