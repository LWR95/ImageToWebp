"""Test script to simulate fresh PC by temporarily moving cache, then test bundled model."""
import os
import shutil
import tempfile
import sys

def test_offline_model():
    """Test that the application works without pre-existing model cache."""
    
    # Backup existing cache directories
    cache_backups = {}
    cache_dirs = [
        os.path.expanduser("~/.u2net"),
        os.path.expanduser("~/.cache/rembg"),
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "rembg"),
    ]
    
    print("Backing up existing model caches...")
    with tempfile.TemporaryDirectory() as temp_dir:
        for i, cache_dir in enumerate(cache_dirs):
            if os.path.exists(cache_dir):
                backup_path = os.path.join(temp_dir, f"cache_backup_{i}")
                print(f"Moving {cache_dir} to {backup_path}")
                shutil.move(cache_dir, backup_path)
                cache_backups[cache_dir] = backup_path
        
        try:
            print("Testing AI diagnostic without existing cache...")
            # Run the diagnostic
            import subprocess
            result = subprocess.run([sys.executable, "ai_diagnostic.py"], 
                                  capture_output=True, text=True, cwd=os.getcwd())
            
            print("=== AI Diagnostic Output ===")
            print(result.stdout)
            if result.stderr:
                print("=== STDERR ===")
                print(result.stderr)
            
            if result.returncode == 0:
                print("SUCCESS: AI diagnostic passed without pre-existing cache!")
                return True
            else:
                print(f"FAILED: AI diagnostic failed with return code {result.returncode}")
                return False
                
        finally:
            print("Restoring original cache directories...")
            for original_path, backup_path in cache_backups.items():
                if os.path.exists(backup_path):
                    print(f"Restoring {backup_path} to {original_path}")
                    shutil.move(backup_path, original_path)

if __name__ == "__main__":
    success = test_offline_model()
    sys.exit(0 if success else 1)
