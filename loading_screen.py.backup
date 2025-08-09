"""
SHH Image Converter v4.0 - Loading Screen
Professional startup loading screen with progress indication
"""

import tkinter as tk
from tkinter import ttk
import threading
import time
import sys

class LoadingScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SHH Image Converter v4.0")
        self.root.geometry("450x280")
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Remove window decorations for splash effect
        self.root.overrideredirect(True)
        
        # Modern dark theme
        self.root.configure(bg='#1e1e1e')
        
        # Variables
        self.progress_var = tk.DoubleVar()
        self.status_var = tk.StringVar(value="Initializing SHH Image Converter...")
        
        # Create UI
        self.create_widgets()
        
        # Make window topmost
        self.root.attributes('-topmost', True)
        
        # Loading steps
        self.loading_steps = [
            ("Extracting application files...", 25),
            ("Loading Python runtime...", 45),
            ("Initializing image processing libraries...", 65),
            ("Setting up user interface...", 80),
            ("Preparing AI background removal...", 95),
            ("Ready to launch!", 100)
        ]
        self.current_step = 0
        
    def center_window(self):
        """Center the loading window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (450 // 2)
        y = (self.root.winfo_screenheight() // 2) - (280 // 2)
        self.root.geometry(f"450x280+{x}+{y}")
        
    def create_widgets(self):
        # Main frame with padding
        main_frame = tk.Frame(self.root, bg='#1e1e1e', padx=40, pady=30)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Logo/Title area
        title_frame = tk.Frame(main_frame, bg='#1e1e1e')
        title_frame.pack(pady=(0, 30))
        
        # App title with modern styling
        title_label = tk.Label(
            title_frame,
            text="SHH Image Converter",
            font=("Segoe UI", 20, "bold"),
            fg='#ffffff',
            bg='#1e1e1e'
        )
        title_label.pack()
        
        # Version with accent color
        version_label = tk.Label(
            title_frame,
            text="Version 4.0 • AI-Powered Background Removal",
            font=("Segoe UI", 11),
            fg='#4FC3F7',
            bg='#1e1e1e'
        )
        version_label.pack(pady=(5, 0))
        
        # Feature highlights
        features_label = tk.Label(
            title_frame,
            text="WebP • JPG • PNG • Batch Processing • Drag & Drop",
            font=("Segoe UI", 9),
            fg='#9e9e9e',
            bg='#1e1e1e'
        )
        features_label.pack(pady=(10, 0))
        
        # Progress section
        progress_frame = tk.Frame(main_frame, bg='#1e1e1e')
        progress_frame.pack(pady=20, fill=tk.X)
        
        # Progress bar with modern styling
        style = ttk.Style()
        try:
            style.theme_use('clam')
        except tk.TclError:
            # Fallback to default theme if clam is not available
            pass
            
        style.configure(
            "Modern.Horizontal.TProgressbar",
            background='#4FC3F7',
            troughcolor='#2d2d2d',
            borderwidth=0,
            lightcolor='#4FC3F7',
            darkcolor='#4FC3F7',
            focuscolor='none'
        )
        
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            variable=self.progress_var,
            maximum=100,
            style="Modern.Horizontal.TProgressbar",
            length=370
        )
        self.progress_bar.pack()
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            textvariable=self.status_var,
            font=("Segoe UI", 10),
            fg='#cccccc',
            bg='#1e1e1e',
            wraplength=370,
            justify='center'
        )
        self.status_label.pack(pady=(15, 0))
        
        # Loading dots animation
        self.dots_label = tk.Label(
            main_frame,
            text="●",
            font=("Segoe UI", 12),
            fg='#4FC3F7',
            bg='#1e1e1e'
        )
        self.dots_label.pack(pady=(10, 0))
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="Please wait while the application initializes...",
            font=("Segoe UI", 8),
            fg='#666666',
            bg='#1e1e1e'
        )
        footer_label.pack(side=tk.BOTTOM, pady=(10, 0))
        
    def animate_dots(self):
        """Animate loading dots"""
        dots = ["●", "●●", "●●●", "●●●●", "●●●●●"]
        current_dots = dots[int(time.time() * 2) % len(dots)]
        self.dots_label.config(text=current_dots)
        
        # Schedule next animation if still loading
        if self.progress_var.get() < 100:
            self.root.after(250, self.animate_dots)
    
    def update_progress(self, progress, status):
        """Update progress bar and status"""
        self.progress_var.set(progress)
        self.status_var.set(status)
        self.root.update_idletasks()
        
    def simulate_loading(self):
        """Simulate the loading process with realistic timing"""
        # Start dots animation
        self.animate_dots()
        
        # Simulate realistic loading steps
        for i, (status, progress) in enumerate(self.loading_steps):
            self.update_progress(progress, status)
            
            # Realistic timing for each step
            if i == 0:  # Extraction - longest step
                time.sleep(3.0)
            elif i == 1:  # Python runtime
                time.sleep(2.5)
            elif i == 2:  # Libraries
                time.sleep(2.0)
            elif i == 3:  # UI setup
                time.sleep(1.5)
            elif i == 4:  # AI prep
                time.sleep(1.0)
            else:  # Ready
                time.sleep(0.5)
        
        # Hold "Ready" state briefly
        time.sleep(0.5)
        
    def show_loading(self, callback):
        """Show loading screen and run callback when complete"""
        # Start loading simulation in background
        self.loading_thread = threading.Thread(target=self._loading_worker, args=(callback,))
        self.loading_thread.daemon = True
        self.loading_thread.start()
        
        # Show the loading window
        self.root.mainloop()
        
    def _loading_worker(self, callback):
        """Background worker for loading simulation"""
        try:
            self.simulate_loading()
            
            # Schedule callback on main thread
            self.root.after(0, lambda: self._finish_loading(callback))
            
        except Exception as e:
            print(f"Loading error: {e}")
            self.root.after(0, lambda: self._finish_loading(callback))
    
    def _finish_loading(self, callback):
        """Finish loading and launch main application"""
        # Close loading screen
        self.root.destroy()
        
        # Launch main application
        if callback:
            callback()

def show_loading_screen(main_app_callback):
    """
    Show loading screen and launch main application when complete
    
    Args:
        main_app_callback: Function to call when loading is complete
    """
    loading = LoadingScreen()
    loading.show_loading(main_app_callback)

if __name__ == "__main__":
    # Test the loading screen
    def test_main_app():
        print("Main application would launch here!")
        
    show_loading_screen(test_main_app)
