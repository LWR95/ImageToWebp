import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import threading
import os
import json

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.version = "2.0"
        self.root.title(f"SHH Image Converter v{self.version}")
        self.root.geometry("500x350")
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
        settings_frame = ttk.Frame(notebook, padding="10")

        notebook.add(converter_frame, text='Converter')
        notebook.add(settings_frame, text='Settings')

        # --- Converter Tab Widgets ---
        # Source Directory
        ttk.Label(converter_frame, text="Source Folder:").grid(row=0, column=0, sticky=tk.W, pady=2)
        source_entry = ttk.Entry(converter_frame, textvariable=self.source_dir, width=50, state="readonly")
        source_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        ttk.Button(converter_frame, text="Browse...", command=self.select_source_dir).grid(row=1, column=2, sticky=tk.W, padx=5)

        # Destination Directory
        ttk.Label(converter_frame, text="Destination Folder:").grid(row=2, column=0, sticky=tk.W, pady=2)
        dest_entry = ttk.Entry(converter_frame, textvariable=self.dest_dir, width=50, state="readonly")
        dest_entry.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        ttk.Button(converter_frame, text="Browse...", command=self.select_dest_dir).grid(row=3, column=2, sticky=tk.W, padx=5)

        # Quality Slider
        self.quality_label_text = ttk.Label(converter_frame, text="Quality (1-100):")
        self.quality_label_text.grid(row=4, column=0, sticky=tk.W, pady=2)
        self.quality_slider = ttk.Scale(converter_frame, from_=1, to=100, orient=tk.HORIZONTAL, variable=self.quality, length=300)
        self.quality_slider.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        self.quality_label_value = ttk.Label(converter_frame, textvariable=self.quality)
        self.quality_label_value.grid(row=5, column=2, sticky=tk.W, padx=5)

        # Convert Button
        self.convert_button = ttk.Button(converter_frame, text="Convert Images", command=self.start_conversion_thread, state="disabled")
        self.convert_button.grid(row=6, column=0, columnspan=3, pady=10)

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

        # Save Settings Button
        ttk.Button(settings_frame, text="Save Settings", command=self.save_settings).grid(row=4, column=0, columnspan=2, pady=20)

    def on_format_change(self, event=None):
        if self.output_format.get() == "PNG":
            self.quality_slider.config(state="disabled")
            self.quality_label_text.config(state="disabled")
            self.quality_label_value.config(state="disabled")
        else:
            self.quality_slider.config(state="normal")
            self.quality_label_text.config(state="normal")
            self.quality_label_value.config(state="normal")

    def save_settings(self):
        settings = {
            "output_width": self.output_width.get(),
            "output_height": self.output_height.get(),
            "output_format": self.output_format.get(),
            "quality": self.quality.get()
        }
        try:
            with open(self.config_file, 'w') as f:
                json.dump(settings, f, indent=4)
            messagebox.showinfo("Settings Saved", "Your settings have been saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings:\n{e}")

    def load_settings(self):
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    settings = json.load(f)
                    self.output_width.set(settings.get("output_width", 500))
                    self.output_height.set(settings.get("output_height", 500))
                    self.output_format.set(settings.get("output_format", "WebP"))
                    self.quality.set(settings.get("quality", 85))
                self.on_format_change() # Update UI based on loaded settings
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load settings:\n{e}")

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
            width = self.output_width.get()
            height = self.output_height.get()
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

                    # Handle transparency
                    if output_format == "PNG" and img_original_mode in ('RGBA', 'LA', 'P'):
                        img = img.convert("RGBA") # Preserve transparency for PNG
                    else:
                        # For other formats, flatten onto a white background
                        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                            background_for_flattening = Image.new("RGB", img.size, (255, 255, 255))
                            img_rgba = img.convert("RGBA")
                            background_for_flattening.paste(img_rgba, mask=img_rgba)
                            img = background_for_flattening
                        else:
                            img = img.convert('RGB')

                    # Image processing logic
                    img.thumbnail((width, height))
                    
                    # Create background based on target format
                    if output_format == "PNG" and img_original_mode in ('RGBA', 'LA', 'P'):
                         background = Image.new('RGBA', (width, height), (255, 255, 255, 0))
                    else:
                        background = Image.new('RGB', (width, height), (255, 255, 255))
                    
                    paste_x = (width - img.width) // 2
                    paste_y = (height - img.height) // 2
                    
                    background.paste(img, (paste_x, paste_y))

                    # Save with selected format
                    base_filename, _ = os.path.splitext(filename)
                    output_extension = output_format.lower()
                    output_filename = f"{base_filename}.{output_extension}"
                    output_path = os.path.join(dest, output_filename)
                    
                    save_params = {'quality': quality} if output_format in ['WebP', 'JPEG'] else {}
                    background.save(output_path, output_format, **save_params)
                    converted_count += 1

                except Exception as e:
                    print(f"Skipping {filename}: {e}") # Log to console for now
                    skipped_count += 1
                    continue
            
            self.status_var.set(f"Conversion complete! Converted: {converted_count}, Skipped: {skipped_count}")
            messagebox.showinfo("Success", f"Conversion complete!\n\nSuccessfully converted: {converted_count}\nSkipped: {skipped_count}")

        except Exception as e:
            self.status_var.set("Error!")
            messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")
        
        finally:
            self.convert_button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
