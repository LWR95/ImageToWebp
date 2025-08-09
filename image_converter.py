import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
import threading
import os
import json

class AIManager:
    def __init__(self):
        self._rembg = None
        self._session = None
        self._session_lock = threading.Lock()
    
    def get_session(self):
        """Get or create background removal session (thread-safe)"""
        with self._session_lock:
            if self._session is None:
                # Load rembg library if not already loaded
                if self._rembg is None:
                    try:
                        import rembg
                        self._rembg = rembg
                    except ImportError as e:
                        print(f"AI libraries not available: {e}")
                        return None
                
                # Create session if library loaded successfully
                if self._rembg is not None:
                    try:
                        self._session = self._rembg.new_session('u2net')
                    except Exception as e:
                        print(f"Failed to create AI session: {e}")
                        return None
            return self._session
    
    def remove_background(self, image_bytes):
        """Remove background from image with error handling"""
        session = self.get_session()
        if session is None:
            return None
        try:
            return self._rembg.remove(image_bytes, session=session)
        except Exception as e:
            print(f"Background removal failed: {e}")
            return None

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.style = ThemedStyle(root)
        self.version = "4.1.1"
        self.root.title(f"SHH Image Converter v{self.version}")
        self.root.geometry("650x550")
        self.root.resizable(False, False)
        self.config_file = "config.json"

        # Variables
        self.source_dir = tk.StringVar()
        self.dest_dir = tk.StringVar()
        self.quality = tk.IntVar(value=85)
        
        # Settings Variables
        self.output_width = tk.IntVar(value=500)
        self.output_height = tk.IntVar(value=500)
        self.output_format = tk.StringVar(value="WebP")
        self.theme = tk.StringVar(value="arc") # Default theme
        self.remove_background = tk.BooleanVar(value=False)

        # Link variables to update preview
        self.output_width.trace_add("write", lambda *args: self.update_preview())
        self.output_height.trace_add("write", lambda *args: self.update_preview())
        self.quality.trace_add("write", lambda *args: self.update_preview())
        self.remove_background.trace_add("write", lambda *args: self.update_preview())

        # Background removal session management
        self.ai_manager = AIManager()

        # UI Elements
        self.create_widgets()
        self.load_settings()

    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Create a Notebook (tabbed interface)
        notebook = ttk.Notebook(main_frame)
        notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

        # Create frames for each tab
        converter_frame = ttk.Frame(notebook, padding="10")
        preview_frame = ttk.Frame(notebook, padding="10")
        settings_frame = ttk.Frame(notebook, padding="10")

        notebook.add(converter_frame, text='Converter')
        notebook.add(preview_frame, text='Preview')
        notebook.add(settings_frame, text='Settings')

        # --- Converter Tab Widgets ---
        # Drag and Drop Area
        self.drop_target_frame = ttk.Frame(converter_frame, relief="sunken", borderwidth=2, width=400, height=100)
        self.drop_target_frame.grid(row=0, column=0, columnspan=3, pady=5, sticky=(tk.W, tk.E))
        self.drop_target_frame.grid_propagate(False)
        
        self.drop_label = ttk.Label(self.drop_target_frame, text="Drag and Drop Source Folder Here", anchor=tk.CENTER)
        self.drop_label.pack(expand=True, fill=tk.BOTH)

        self.drop_target_frame.drop_target_register(DND_FILES)
        self.drop_target_frame.dnd_bind('<<Drop>>', self.handle_drop)
        self.drop_target_frame.dnd_bind('<<DragEnter>>', self.on_drag_enter)
        self.drop_target_frame.dnd_bind('<<DragLeave>>', self.on_drag_leave)

        # Source Directory
        ttk.Label(converter_frame, text="Source Folder:").grid(row=1, column=0, sticky=tk.W, pady=2)
        source_entry = ttk.Entry(converter_frame, textvariable=self.source_dir, width=50, state="readonly")
        source_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        ttk.Button(converter_frame, text="Browse...", command=self.select_source_dir).grid(row=2, column=2, sticky=tk.W, padx=5)

        # Destination Directory
        ttk.Label(converter_frame, text="Destination Folder:").grid(row=3, column=0, sticky=tk.W, pady=2)
        dest_entry = ttk.Entry(converter_frame, textvariable=self.dest_dir, width=50, state="readonly")
        dest_entry.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        ttk.Button(converter_frame, text="Browse...", command=self.select_dest_dir).grid(row=4, column=2, sticky=tk.W, padx=5)

        # Quality Slider
        self.quality_label_text = ttk.Label(converter_frame, text="Quality (1-100):")
        self.quality_label_text.grid(row=5, column=0, sticky=tk.W, pady=2)
        self.quality_slider = ttk.Scale(converter_frame, from_=1, to=100, orient=tk.HORIZONTAL, variable=self.quality, length=300)
        self.quality_slider.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        self.quality_label_value = ttk.Label(converter_frame, textvariable=self.quality)
        self.quality_label_value.grid(row=6, column=2, sticky=tk.W, padx=5)

        # Convert Button
        self.convert_button = ttk.Button(converter_frame, text="Convert Images", command=self.start_conversion_thread, state="disabled")
        self.convert_button.grid(row=7, column=0, columnspan=3, pady=10)

        # --- Preview Tab Widgets ---
        preview_frame.grid_columnconfigure(0, weight=1)
        preview_frame.grid_columnconfigure(1, weight=1)
        
        ttk.Label(preview_frame, text="Before:", font=("", 10, "bold")).grid(row=0, column=0, sticky=tk.W)
        self.preview_before_label = ttk.Label(preview_frame, text="No image selected", anchor=tk.CENTER, relief="sunken", borderwidth=2)
        self.preview_before_label.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        ttk.Label(preview_frame, text="After:", font=("", 10, "bold")).grid(row=0, column=1, sticky=tk.W)
        self.preview_after_label = ttk.Label(preview_frame, text="Settings will be applied here", anchor=tk.CENTER, relief="sunken", borderwidth=2)
        self.preview_after_label.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        
        preview_frame.grid_rowconfigure(1, weight=1)

        # Status Bar (placed outside the notebook to be persistent)
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)

        # --- Settings Tab Widgets ---
        settings_frame.grid_columnconfigure(1, weight=1)

        # Output Dimensions
        ttk.Label(settings_frame, text="Output Dimensions (pixels):").grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))
        
        ttk.Label(settings_frame, text="Width:").grid(row=1, column=0, sticky=tk.W, padx=5)
        width_entry = ttk.Entry(settings_frame, textvariable=self.output_width, width=10)
        width_entry.grid(row=1, column=1, sticky=tk.W, padx=5)

        ttk.Label(settings_frame, text="Height:").grid(row=2, column=0, sticky=tk.W, padx=5)
        height_entry = ttk.Entry(settings_frame, textvariable=self.output_height, width=10)
        height_entry.grid(row=2, column=1, sticky=tk.W, padx=5)

        # Output Format
        ttk.Label(settings_frame, text="Output Format:").grid(row=3, column=0, sticky=tk.W, pady=(10, 5))
        format_menu = ttk.Combobox(settings_frame, textvariable=self.output_format, values=["WebP", "JPEG", "PNG"], state="readonly")
        format_menu.grid(row=3, column=1, sticky=tk.W, padx=5)
        format_menu.bind("<<ComboboxSelected>>", self.on_format_change)

        # Theme Selection
        ttk.Label(settings_frame, text="Theme:").grid(row=4, column=0, sticky=tk.W, pady=(10, 5))
        theme_menu = ttk.Combobox(settings_frame, textvariable=self.theme, state="readonly")
        theme_menu['values'] = sorted(self.style.get_themes())
        theme_menu.grid(row=4, column=1, sticky=tk.W, padx=5)
        theme_menu.bind("<<ComboboxSelected>>", lambda e: self.set_theme())

        # Background Removal
        ttk.Label(settings_frame, text="Background Removal:").grid(row=5, column=0, sticky=tk.W, pady=(10, 5))
        bg_remove_check = ttk.Checkbutton(settings_frame, text="Remove Background (PNG only)", 
                                         variable=self.remove_background, command=self.on_bg_remove_change)
        bg_remove_check.grid(row=5, column=1, sticky=tk.W, padx=5)

        # Save Settings Button
        ttk.Button(settings_frame, text="Save Settings", command=self.save_settings).grid(row=6, column=0, columnspan=2, pady=10)

    def handle_drop(self, event):
        # The event.data is a string containing one or more file paths, possibly enclosed in braces
        path_str = event.data.strip('{}')
        if os.path.isdir(path_str):
            self.source_dir.set(path_str)
            self.check_paths()
        else:
            messagebox.showwarning("Invalid Drop", "Please drop a folder, not a file.")
        self.on_drag_leave(event) # Reset style after drop

    def on_drag_enter(self, event):
        self.drop_label.config(text="Drop it!")

    def on_drag_leave(self, event):
        self.drop_label.config(text="Drag and Drop Source Folder Here")

    def set_theme(self):
        self.style.set_theme(self.theme.get())

    def on_format_change(self, event=None):
        if self.output_format.get() == "PNG":
            self.quality_slider.config(state="disabled")
            self.quality_label_text.config(state="disabled")
            self.quality_label_value.config(state="disabled")
        else:
            self.quality_slider.config(state="normal")
            self.quality_label_text.config(state="normal")
            self.quality_label_value.config(state="normal")
        self.update_preview()

    def on_bg_remove_change(self):
        # Force PNG format when background removal is enabled
        if self.remove_background.get():
            if self.output_format.get() != "PNG":
                self.output_format.set("PNG")
                self.on_format_change()  # Update quality slider state
                messagebox.showinfo("Format Changed", "Output format changed to PNG for background removal.")
        self.update_preview()

    def save_settings(self):
        settings = {
            "output_width": self.output_width.get(),
            "output_height": self.output_height.get(),
            "output_format": self.output_format.get(),
            "quality": self.quality.get(),
            "theme": self.theme.get(),
            "remove_background": self.remove_background.get()
        }
        try:
            with open(self.config_file, 'w') as f:
                json.dump(settings, f, indent=4)
            messagebox.showinfo("Settings Saved", "Your settings have been saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings:\n{e}")
        self.update_preview()

    def load_settings(self):
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    settings = json.load(f)
                    self.output_width.set(settings.get("output_width", 500))
                    self.output_height.set(settings.get("output_height", 500))
                    self.output_format.set(settings.get("output_format", "WebP"))
                    self.quality.set(settings.get("quality", 85))
                    self.theme.set(settings.get("theme", "arc"))
                    self.remove_background.set(settings.get("remove_background", False))
            # Set theme regardless of whether settings were loaded, to ensure a theme is always applied
            self.set_theme()
            self.on_format_change() # Update UI based on loaded settings
            self.update_preview()
        except Exception as e:
            self.set_theme() # Ensure theme is set even on error
            messagebox.showerror("Error", f"Failed to load settings:\n{e}")

    def get_bg_removal_session(self):
        """Get or create a background removal session (thread-safe)"""
        return self.ai_manager.get_session()

    def select_source_dir(self):
        path = filedialog.askdirectory()
        if path:
            self.source_dir.set(path)
            self.check_paths()

    def select_dest_dir(self):
        path = filedialog.askdirectory()
        if path:
            self.dest_dir.set(path)
            self.check_paths()

    def check_paths(self):
        if self.source_dir.get() and self.dest_dir.get():
            self.convert_button.config(state="normal")
        self.update_preview()

    def _get_positive_int(self, var: tk.Variable, default: int) -> int:
        """Safely get a positive int from a Tk variable; fallback to default on empty/invalid."""
        try:
            val = int(var.get())
            return max(1, val)
        except (tk.TclError, ValueError, TypeError):
            return default

    def update_preview(self):
        source = self.source_dir.get()
        if not source or not os.path.isdir(source):
            self.preview_before_label.config(image='', text="No image selected")
            self.preview_after_label.config(image='', text="Settings will be applied here")
            self.preview_before_label.image = None
            self.preview_after_label.image = None
            return

        image_files = [f for f in os.listdir(source) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
        if not image_files:
            self.preview_before_label.config(image='', text="No images found in folder")
            self.preview_after_label.config(image='', text="Settings will be applied here")
            self.preview_before_label.image = None
            self.preview_after_label.image = None
            return

        first_image_path = os.path.join(source, image_files[0])
        
        try:
            # We need to update the UI to get correct widget sizes
            self.root.update_idletasks()
            original_image = Image.open(first_image_path)

            # --- Before Preview ---
            pad = 10 # Small padding
            w_before = self.preview_before_label.winfo_width() - pad
            h_before = self.preview_before_label.winfo_height() - pad
            
            if w_before < pad or h_before < pad: # Fallback if widget size isn't available
                w_before, h_before = 250, 250

            img_before_thumb = original_image.copy()
            img_before_thumb.thumbnail((w_before, h_before))
            self.photo_before = ImageTk.PhotoImage(img_before_thumb)
            self.preview_before_label.config(image=self.photo_before, text="")
            self.preview_before_label.image = self.photo_before

            # --- After Preview ---
            output_width = self._get_positive_int(self.output_width, 500)
            output_height = self._get_positive_int(self.output_height, 500)
            output_format = self.output_format.get()

            # Create the image as it would be after conversion settings are applied
            img_after_base = original_image.copy()
            
            # Apply background removal if enabled
            if self.remove_background.get():
                try:
                    session = self.get_bg_removal_session()
                    if session is not None:
                        # Convert to bytes for rembg processing
                        from io import BytesIO
                        img_bytes = BytesIO()
                        img_after_base.save(img_bytes, format='PNG')
                        img_bytes.seek(0)
                        
                        # Remove background
                        bg_removed_bytes = self.ai_manager.remove_background(img_bytes.getvalue())
                        if bg_removed_bytes is not None:
                            bg_removed_img = Image.open(BytesIO(bg_removed_bytes))
                            img_after_base = bg_removed_img
                            
                            # Ensure PNG format when background is removed
                            if output_format != "PNG":
                                output_format = "PNG"
                                self.output_format.set("PNG")
                        else:
                            print("Warning: Background removal failed, continuing without AI")
                    else:
                        print("Warning: Background removal session not available")
                except Exception as e:
                    print(f"Background removal failed in preview: {e}")
            
            # Handle transparency correctly for the conversion process
            # Skip transparency flattening if background removal is enabled (preserve transparency)
            if not self.remove_background.get():
                if output_format != "PNG" and (img_after_base.mode in ('RGBA', 'LA') or (img_after_base.mode == 'P' and 'transparency' in img_after_base.info)):
                    background_flatten = Image.new("RGB", img_after_base.size, (255, 255, 255))
                    img_rgba = img_after_base.convert("RGBA")
                    background_flatten.paste(img_rgba, mask=img_rgba)
                    img_after_base = background_flatten
                elif img_after_base.mode not in ("RGB", "RGBA"):
                    img_after_base = img_after_base.convert("RGB")
            else:
                # For background removal, ensure RGBA mode to preserve transparency
                if img_after_base.mode != "RGBA":
                    img_after_base = img_after_base.convert("RGBA")

            # Calculate scaling to fit within target dimensions while maintaining aspect ratio
            img_width, img_height = img_after_base.size
            scale_factor = min(output_width / img_width, output_height / img_height)
            
            # Only resize if we need to scale (either up or down)
            if scale_factor != 1.0:
                new_width = int(img_width * scale_factor)
                new_height = int(img_height * scale_factor)
                img_after_base = img_after_base.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Create a new background for pasting the scaled image (letterboxing)
            final_processed_image = Image.new('RGBA', (output_width, output_height), (255, 255, 255, 0))
            paste_x = (output_width - img_after_base.width) // 2
            paste_y = (output_height - img_after_base.height) // 2
            
            # Use appropriate paste method for transparency
            if img_after_base.mode == 'RGBA':
                final_processed_image.paste(img_after_base, (paste_x, paste_y), img_after_base)
            else:
                final_processed_image.paste(img_after_base, (paste_x, paste_y))

            if output_format != "PNG":
                final_processed_image = final_processed_image.convert("RGB")

            # Now, create a thumbnail of this final processed image for the preview display
            w_after = self.preview_after_label.winfo_width() - pad
            h_after = self.preview_after_label.winfo_height() - pad
            if w_after < pad or h_after < pad: # Fallback
                w_after, h_after = 250, 250

            display_thumb = final_processed_image.copy()
            display_thumb.thumbnail((w_after, h_after))

            self.photo_after = ImageTk.PhotoImage(display_thumb)
            self.preview_after_label.config(image=self.photo_after, text="")
            self.preview_after_label.image = self.photo_after

        except Exception as e:
            self.preview_before_label.config(image='', text="Error loading image")
            self.preview_after_label.config(image='', text="Preview Error")
            self.preview_before_label.image = None
            self.preview_after_label.image = None
            print(f"Preview Error: {e}")

    def start_conversion_thread(self):
        self.convert_button.config(state="disabled")
        self.status_var.set("Starting conversion...")
        thread = threading.Thread(target=self.convert_images)
        thread.start()

    def convert_images(self):
        try:
            source = self.source_dir.get()
            dest = self.dest_dir.get()
            quality = self.quality.get()
            width = self._get_positive_int(self.output_width, 500)
            height = self._get_positive_int(self.output_height, 500)
            output_format = self.output_format.get()
            
            image_files = [f for f in os.listdir(source) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
            total_files = len(image_files)
            converted_count = 0
            skipped_count = 0

            for i, filename in enumerate(image_files):
                self.status_var.set(f"Converting {i+1}/{total_files}...")
                try:
                    image_path = os.path.join(source, filename)
                    img = Image.open(image_path)
                    img_original_mode = img.mode

                    # Apply background removal if enabled
                    if self.remove_background.get():
                        try:
                            session = self.get_bg_removal_session()
                            if session is not None:
                                # Convert to bytes for rembg processing
                                from io import BytesIO
                                img_bytes = BytesIO()
                                img.save(img_bytes, format='PNG')
                                img_bytes.seek(0)
                                
                                # Remove background
                                bg_removed_bytes = self.ai_manager.remove_background(img_bytes.getvalue())
                                if bg_removed_bytes is not None:
                                    bg_removed_img = Image.open(BytesIO(bg_removed_bytes))
                                    img = bg_removed_img
                                    
                                    # Force PNG format when background is removed
                                    output_format = "PNG"
                                else:
                                    print(f"Warning: Background removal failed for {filename}, continuing without AI")
                            else:
                                print(f"Warning: Background removal session not available for {filename}")
                        except Exception as e:
                            print(f"Background removal failed for {filename}: {e}")

                    # Handle transparency
                    # Skip transparency flattening if background removal is enabled (preserve transparency)
                    if not self.remove_background.get():
                        if output_format == "PNG" and img_original_mode in ('RGBA', 'LA', 'P'):
                            img = img.convert("RGBA")
                        else:
                            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                                background_for_flattening = Image.new("RGB", img.size, (255, 255, 255))
                                img_rgba = img.convert("RGBA")
                                background_for_flattening.paste(img_rgba, mask=img_rgba)
                                img = background_for_flattening
                            else:
                                img = img.convert('RGB')
                    else:
                        # For background removal, ensure RGBA mode to preserve transparency
                        if img.mode != "RGBA":
                            img = img.convert("RGBA")

                    # Calculate scaling to fit within target dimensions while maintaining aspect ratio
                    img_width, img_height = img.size
                    scale_factor = min(width / img_width, height / img_height)
                    
                    # Only resize if we need to scale (either up or down)
                    if scale_factor != 1.0:
                        new_width = int(img_width * scale_factor)
                        new_height = int(img_height * scale_factor)
                        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    
                    # Create appropriate background based on whether we have transparency
                    if self.remove_background.get() or (output_format == "PNG" and img.mode == 'RGBA'):
                         background = Image.new('RGBA', (width, height), (255, 255, 255, 0))
                    else:
                        background = Image.new('RGB', (width, height), (255, 255, 255))
                    
                    paste_x = (width - img.width) // 2
                    paste_y = (height - img.height) // 2                    # Use appropriate paste method for transparency
                    if img.mode == 'RGBA' and background.mode == 'RGBA':
                        background.paste(img, (paste_x, paste_y), img)
                    else:
                        background.paste(img, (paste_x, paste_y))

                    base_filename, _ = os.path.splitext(filename)
                    output_extension = output_format.lower()
                    output_filename = f"{base_filename}.{output_extension}"
                    output_path = os.path.join(dest, output_filename)
                    
                    save_params = {'quality': quality} if output_format in ['WebP', 'JPEG'] else {}
                    background.save(output_path, output_format, **save_params)
                    converted_count += 1

                except Exception as e:
                    print(f"Skipping {filename}: {e}")
                    skipped_count += 1
                    continue
            
            self.status_var.set(f"Conversion complete! Converted: {converted_count}, Skipped: {skipped_count}")
            messagebox.showinfo("Success", f"Conversion complete!\n\nSuccessfully converted: {converted_count}\nSkipped: {skipped_count}")

        except Exception as e:
            self.status_var.set("Error!")
            messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")
        
        finally:
            self.convert_button.config(state="normal")


def launch_main_application():
    """Launch the main image converter application"""
    root = TkinterDnD.Tk()
    app = ImageConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Import loading screen
    try:
        from loading_screen import show_loading_screen
        # Show loading screen first, then launch main app
        show_loading_screen(launch_main_application)
    except ImportError:
        # Fallback if loading screen not available
        print("Loading screen not found, launching directly...")
        launch_main_application()
