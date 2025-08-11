"""
Model preparation script for SHH Image Converter.
Run this before building to ensure the AI model is available for bundling.
"""
import os
import sys
import shutil
from pathlib import Path

def prepare_model():
    """Prepare the AI model for bundling in the executable."""
    print("SHH Image Converter - Model Preparation")
    print("=" * 50)
    
    # Standard cache locations where rembg stores the model
    cache_locations = [
        os.path.expanduser("~/.u2net"),
        os.path.expanduser("~/.cache/rembg"),
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "rembg"),
    ]
    
    model_file = "u2net.onnx"
    source_model = None
    
    # Look for existing model in cache
    for cache_dir in cache_locations:
        cache_file = os.path.join(cache_dir, model_file)
        if os.path.exists(cache_file) and os.path.getsize(cache_file) > 100_000_000:
            source_model = cache_file
            print(f"Found cached model: {cache_file}")
            break
    
    if not source_model:
        print("No cached model found. Downloading...")
        print("This will happen automatically on first AI use.")
        
        # Try to trigger download by importing rembg and creating session
        try:
            import rembg
            print("Creating rembg session to download model...")
            session = rembg.new_session('u2net')
            print("Model downloaded successfully!")
            
            # Try to find it again
            for cache_dir in cache_locations:
                cache_file = os.path.join(cache_dir, model_file)
                if os.path.exists(cache_file):
                    source_model = cache_file
                    break
                    
        except Exception as e:
            print(f"Error downloading model: {e}")
            print("Model will be downloaded on first AI use in the built application.")
            return False
    
    if source_model:
        # Create models directory structure
        models_dir = Path("models/u2net")
        models_dir.mkdir(parents=True, exist_ok=True)
        
        target_file = models_dir / model_file
        
        # Copy model to local models directory
        print(f"Copying model to {target_file}...")
        shutil.copy2(source_model, target_file)
        
        size_mb = os.path.getsize(target_file) / (1024 * 1024)
        print(f"Model prepared successfully! Size: {size_mb:.1f} MB")
        print(f"Location: {target_file}")
        
        return True
    
    return False

def main():
    success = prepare_model()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Model preparation complete!")
        print("You can now run: python -m PyInstaller .\\SHH_Image_Converter_v4_Complete.spec")
    else:
        print("⚠️  Model not prepared, but build will still work.")
        print("The AI model will be downloaded on first use of the application.")
    
    print("\nNote: The models/ directory is git-ignored to avoid repository bloat.")

if __name__ == "__main__":
    main()
