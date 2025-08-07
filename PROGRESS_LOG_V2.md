# Progress Log: Version 2.0

This file tracks the development progress for Version 2.0 of the image conversion utility.

## ✅ Stage 1: UI Refactoring

- [x] Restructure the main window to use a `ttk.Notebook` for a tabbed interface ("Converter" and "Settings").
- [x] Move the existing converter widgets into the "Converter" tab.
- [x] Create the "Settings" tab.

## ✅ Stage 2: Settings Implementation

- [x] Add input boxes for "Output Width" and "Output Height" to the Settings tab.
- [x] Add a dropdown menu for "Output Format" (WebP, JPEG, PNG).
- [x] Implement logic to disable the quality slider when "PNG" is selected.
- [x] Implement a mechanism to save settings to a configuration file (e.g., `config.json`).
- [x] Implement logic to load settings from the configuration file on application startup.

## ✅ Stage 3: Core Logic Update

- [x] Modify the `convert_images` function to read the width, height, and format from the saved settings.
- [x] Update the image processing logic to correctly resize and pad images to custom rectangular dimensions.
- [x] Update the save logic to use the selected output format and file extension.

## ✅ Stage 4: Testing and Finalization

- [x] Test the new dimension and format settings thoroughly.
- [x] Verify that settings are saved and loaded correctly between sessions.
- [x] Update the version number to "2.0".
- [x] Update the `README.md` and other documentation to reflect the new features.
- [x] Build the new executable using PyInstaller.
