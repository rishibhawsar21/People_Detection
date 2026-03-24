from deep_sort_realtime.deepsort_tracker import DeepSort

tracker = None

def _get_tracker():
    global tracker
    if tracker is None:
        tracker = DeepSort(max_age=30, n_init=3, max_cosine_distance=0.2, nn_budget=50)
    return tracker

def _valid(det):
    x, y, w, h = det[0]
    if w * h < 400:
        return False
    r = h / w if w > 0 else 0
    return 0.3 <= r <= 4.0

def update_tracks(detections, frame):
    if frame is None:
        return []

    detections = [d for d in detections if _valid(d)]
    tracks = _get_tracker().update_tracks(detections, frame=frame)
    h, w = frame.shape[:2]

    out = []
    for t in tracks:
        if not t.is_confirmed():
            continue
        x1, y1, x2, y2 = map(int, t.to_ltrb())
        x1 = max(0, min(x1, w - 1))
        y1 = max(0, min(y1, h - 1))
        x2 = max(0, min(x2, w))
        y2 = max(0, min(y2, h))
        if x2 <= x1:
            x2 = x1 + 1
        if y2 <= y1:
            y2 = y1 + 1
        out.append((str(t.track_id), x1, y1, x2, y2))
    return out