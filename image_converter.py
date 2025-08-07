import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import threading
import os

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.version = "1.0"
        self.root.title(f"SHH Image to WebP Converter v{self.version}")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        # Variables
        self.source_dir = tk.StringVar()
        self.dest_dir = tk.StringVar()
        self.quality = tk.IntVar(value=85)

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Frame for padding
        main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Source Directory
        ttk.Label(main_frame, text="Source Folder:").grid(row=0, column=0, sticky=tk.W, pady=2)
        source_entry = ttk.Entry(main_frame, textvariable=self.source_dir, width=50, state="readonly")
        source_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        ttk.Button(main_frame, text="Browse...", command=self.select_source_dir).grid(row=1, column=2, sticky=tk.W, padx=5)

        # Destination Directory
        ttk.Label(main_frame, text="Destination Folder:").grid(row=2, column=0, sticky=tk.W, pady=2)
        dest_entry = ttk.Entry(main_frame, textvariable=self.dest_dir, width=50, state="readonly")
        dest_entry.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        ttk.Button(main_frame, text="Browse...", command=self.select_dest_dir).grid(row=3, column=2, sticky=tk.W, padx=5)

        # Quality Slider
        ttk.Label(main_frame, text="WebP Quality (1-100):").grid(row=4, column=0, sticky=tk.W, pady=2)
        quality_slider = ttk.Scale(main_frame, from_=1, to=100, orient=tk.HORIZONTAL, variable=self.quality, length=300)
        quality_slider.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        quality_label = ttk.Label(main_frame, textvariable=self.quality)
        quality_label.grid(row=5, column=2, sticky=tk.W, padx=5)

        # Convert Button
        self.convert_button = ttk.Button(main_frame, text="Convert Images", command=self.start_conversion_thread, state="disabled")
        self.convert_button.grid(row=6, column=0, columnspan=3, pady=10)

        # Status Bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)

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
        # This is where the core logic will go.
        # For now, it's just a placeholder.
        try:
            source = self.source_dir.get()
            dest = self.dest_dir.get()
            quality = self.quality.get()
            
            image_files = [f for f in os.listdir(source) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
            total_files = len(image_files)
            converted_count = 0
            skipped_count = 0

            for i, filename in enumerate(image_files):
                self.status_var.set(f"Converting {i+1}/{total_files}...")
                try:
                    image_path = os.path.join(source, filename)
                    img = Image.open(image_path)

                    # If image has transparency (like a PNG), flatten it onto a white background
                    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                        # Create a new image with a white background
                        background_for_flattening = Image.new("RGB", img.size, (255, 255, 255))
                        # Convert the image to RGBA to ensure it has an alpha channel for the mask
                        img_rgba = img.convert("RGBA")
                        background_for_flattening.paste(img_rgba, mask=img_rgba)
                        img = background_for_flattening
                    else:
                        # Ensure image is in RGB mode if it's not transparent
                        img = img.convert('RGB')

                    # Image processing logic
                    img.thumbnail((500, 500))
                    
                    background = Image.new('RGB', (500, 500), (255, 255, 255))
                    
                    paste_x = (500 - img.width) // 2
                    paste_y = (500 - img.height) // 2
                    
                    background.paste(img, (paste_x, paste_y))

                    # Save as WebP
                    base_filename, _ = os.path.splitext(filename)
                    output_filename = f"{base_filename}.webp"
                    output_path = os.path.join(dest, output_filename)
                    background.save(output_path, 'webp', quality=quality)
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
