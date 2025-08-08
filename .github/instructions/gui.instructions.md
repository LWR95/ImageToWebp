---
applyTo: "image_converter.py"
---

GUI and conversion rules
- Keep UI responsive: run conversions in a background thread; avoid long work on the Tk main thread; use thread-safe UI updates.
- Respect format logic: PNG disables quality slider; AI toggle forces PNG; preserve transparency for PNG, flatten to white for non-PNG when needed.
- Preview: compute a processed copy (resize + letterbox) and display; do not stretch; center paste.
- Background removal: reuse a lazily created `new_session('u2net')` guarded by a lock; handle failures gracefully and continue without AI.
- Settings: persist `output_width`, `output_height`, `output_format`, `quality`, `theme`, `remove_background` to `config.json`; supply defaults if keys are missing.
- Themes: use `ttkthemes.ThemedStyle`; allow user to switch themes safely.
- Drag-and-drop: root must be `TkinterDnD.Tk()`; keep DND bindings on the drop frame stable.
