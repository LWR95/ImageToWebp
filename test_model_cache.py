"""Test the _ensure_model_cache function in isolation."""
import os
import sys

# Add current directory to path
sys.path.insert(0, os.getcwd())

try:
    from image_converter import AIManager
    
    ai = AIManager()
    print("Testing _ensure_model_cache...")
    result = ai._ensure_model_cache()
    print(f"Result: {result}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
