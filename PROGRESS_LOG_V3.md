# Progress Log: Version 3.0

This file tracks the development progress for Version 3.0 of the image conversion utility, focusing on UI/UX enhancements.

## ✅ Stage 1: Theme Selection (Light/Dark Mode)

- [x] Install the `ttkthemes` library and add it to `requirements.txt`.
- [x] Add a "Theme" option (e.g., a dropdown or toggle) to the "Settings" tab.
- [x] Implement the logic to switch the application's theme dynamically.
- [x] Update the `save_settings` and `load_settings` functions to handle the new theme preference in `config.json`.

## ✅ Stage 2: Drag and Drop Support

- [x] Install a suitable drag-and-drop library (e.g., `tkinterdnd2`) and add it to `requirements.txt`.
- [x] Integrate the library with the main application window.
- [x] Implement the logic to accept a dropped folder on the "Converter" tab and set it as the source directory.
- [x] Provide visual feedback when a user is dragging a folder over the window.

## ✅ Stage 3: Live Preview

- [x] Add a new "Preview" tab to the notebook.
- [x] Implement logic to load the first image from the selected source folder.
- [x] Display a "before" thumbnail of the original image.
- [x] Display an "after" thumbnail that updates in real-time when settings (dimensions, format) are changed.
- [x] Handle cases where no folder is selected or the folder contains no images.

## ✅ Stage 4: Finalization

- [x] Test all new UI/UX features thoroughly.
- [x] Update the version number to "3.0".
- [x] Update the `README.md` and other documentation to reflect the new features.
- [x] Build the new v3.0 executable using PyInstaller.
