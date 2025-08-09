# Phase 1 Implementation Tasks

## Task 1: Remove Artificial Loading Delays (30 min)
**File**: `loading_screen.py`
**Priority**: HIGH - Immediate 8-10s improvement

### Changes Required:
1. Replace `time.sleep()` with actual work or minimal delays
2. Update progress steps to reflect real loading tasks
3. Keep visual progress for user feedback

### Code Pattern:
```python
# OLD: time.sleep(3.0) - fake delay
# NEW: time.sleep(0.1) - minimal UI update delay
```

---

## Task 2: Lazy AI Loading (1 hour)
**File**: `image_converter.py`
**Priority**: HIGH - 3-5s improvement

### Changes Required:
1. Remove `from rembg import remove, new_session` from top-level imports
2. Create `AIManager` class with lazy loading
3. Update all AI usage to go through manager
4. Add loading indicator when AI initializes

### Implementation Pattern:
```python
class AIManager:
    def __init__(self):
        self._rembg = None
        self._session = None
        self._loading = False
    
    def get_session(self):
        if self._session is None and not self._loading:
            self._loading = True
            # Show loading indicator
            import rembg
            self._session = rembg.new_session('u2net')
            self._loading = False
        return self._session
```

---

## Task 3: PyInstaller Optimization (1 hour)
**File**: `SHH_Image_Converter_v4_SingleFile.spec`
**Priority**: MEDIUM - Bundle size reduction

### Changes Required:
1. Add comprehensive excludes list
2. Optimize hidden imports
3. Test build with exclusions

### Excludes to Add:
```python
excludes=[
    'onnxruntime.providers.cuda',
    'onnxruntime.providers.dml',
    'cv2.gapi',
    'scipy.linalg.cython_blas',
    'scipy.linalg.cython_lapack',
    'scipy.sparse.csgraph._validation',
    'matplotlib',
    'pandas',
    'jupyter',
    'IPython',
]
```

---

## Testing Protocol:
1. Time startup with stopwatch
2. Test basic image conversion
3. Test AI background removal
4. Verify settings save/load
5. Check build size reduction

## Success Metrics:
- [ ] Startup time reduced to 5-8 seconds
- [ ] All features still functional
- [ ] No import errors or crashes
- [ ] Bundle size reduced by 20-30%
