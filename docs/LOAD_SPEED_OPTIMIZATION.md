# Load Speed Optimization Implementation Guide

## Current State
- **Startup Time**: 15-25 seconds (single-file PyInstaller)
- **File Size**: 147MB
- **Issue**: Full extraction + immediate AI library loading

## Target Goals
- **Phase 1**: 15-25s → 5-8s (Quick wins)
- **Phase 2**: 5-8s → 2-4s (Architecture changes)
- **Final**: 1-2s subsequent launches

## Implementation Phases

### Phase 1: Quick Wins (2-3 hours)
**Target**: Reduce to 5-8 seconds startup

#### 1.1 Remove Artificial Loading Delays
- **File**: `loading_screen.py`
- **Change**: Remove `time.sleep()` calls in `simulate_loading()`
- **Impact**: Immediate 8-10 second reduction

#### 1.2 Implement Lazy AI Loading
- **File**: `image_converter.py`
- **Change**: Move `from rembg import remove, new_session` to first use
- **Pattern**: Create `AIManager` class with lazy initialization
- **Impact**: 3-5 second reduction

#### 1.3 Optimize PyInstaller Excludes
- **File**: `SHH_Image_Converter_v4_SingleFile.spec`
- **Change**: Add comprehensive excludes list
- **Impact**: Smaller bundle, faster extraction

### Phase 2: Architecture Changes (4-6 hours)
**Target**: Reduce to 2-4 seconds startup

#### 2.1 Progressive Loading UI
- **Pattern**: Core UI loads first, AI loads in background
- **UI**: Show "AI features loading..." status when needed
- **Impact**: Perceived instant startup

#### 2.2 Smart Caching System
- **Location**: User AppData folder
- **Cache**: Extracted files + AI model sessions
- **Impact**: Subsequent launches 1-2 seconds

## Implementation Order

1. **Remove loading delays** (30 minutes)
2. **Lazy AI imports** (1 hour)
3. **PyInstaller optimization** (1 hour)
4. **Progressive loading** (2-3 hours)
5. **Caching system** (2-3 hours)

## Testing Checklist

- [ ] Core UI functionality without AI
- [ ] AI features work when enabled
- [ ] Settings persistence
- [ ] Build succeeds with optimizations
- [ ] Startup time measurement
- [ ] Cache invalidation works

## Rollback Plan
Keep current working spec file as backup:
- `SHH_Image_Converter_v4_SingleFile.spec.backup`
- Test thoroughly before committing changes
