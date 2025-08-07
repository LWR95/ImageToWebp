# SHH Image to WebP Converter

A simple desktop utility to batch-convert images to the WebP format, with options for resizing and quality control.

## Features

- **Batch Conversion**: Convert all images in a selected folder at once.
- **User-Friendly GUI**: A simple graphical interface for easy operation.
- **Resize and Pad**: Automatically resizes images to fit within a 500x500 pixel box and pads them with a white background to maintain a square aspect ratio.
- **Transparency Handling**: Correctly handles transparent PNGs by flattening them onto a white background.
- **Quality Control**: Adjust the WebP quality from 1 to 100 to balance file size and image fidelity.
- **Standalone Executable**: Packaged as a single `.exe` file that runs on Windows without needing Python or any other dependencies.

## How to Use

### Using the Executable

1.  Navigate to the `dist/` folder.
2.  Double-click `SHH_Image_Converter.exe` to run the application.
3.  Click the first **Browse...** button to select the folder containing your source images.
4.  Click the second **Browse...** button to select the folder where you want to save the converted WebP files.
5.  Adjust the **WebP Quality** slider to your desired level.
6.  Click the **Convert Images** button to start the process.
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
