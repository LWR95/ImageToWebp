# SHH Image to WebP Converter

A simple desktop utility to batch-convert images to the WebP format, with options for resizing and quality control.

## Features (Version 2.0)

- **Multi-Format Conversion**: Convert images to WebP, JPEG, or PNG.
- **Custom Dimensions**: Set custom output width and height for the converted images.
- **Adjustable Quality**: Control the quality setting for WebP and JPEG formats.
- **Settings Persistence**: Your chosen dimensions, format, and quality are saved in a `config.json` file and loaded automatically on startup.
- **Batch Processing**: Convert all images in a selected folder at once.
- **Intelligent Transparency**: Preserves transparency when converting to PNG and flattens it onto a white background for other formats.
- **Standalone Executable**: Packaged as a single `.exe` file that runs on Windows without needing Python or any other dependencies.

## How to Use

### Using the Executable

1.  Navigate to the `dist/` folder.
2.  Double-click `SHH_Image_Converter.exe` to run the application.
3.  **(Optional) Configure Settings**:
    - Click on the **Settings** tab.
    - Set your desired **Output Width**, **Output Height**, and **Output Format**.
    - Click **Save Settings** to make them the new default.
4.  **Convert Images**:
    - Click on the **Converter** tab.
    - Click the first **Browse...** button to select the folder containing your source images.
    - Click the second **Browse...** button to select the destination folder.
    - If applicable, adjust the **Quality** slider.
    - Click the **Convert Images** button.
5.  A confirmation message will appear when the conversion is complete.

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
