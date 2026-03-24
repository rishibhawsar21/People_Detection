def create_counter(offset=15):
    return {
        "offset": offset,
        "prev_positions": {},
        "counted_in": set(),
        "counted_out": set(),
        "in_count": 0,
        "out_count": 0,
    }

def get_center(x1, y1, x2, y2):
    return ((x1 + x2) // 2, (y1 + y2) // 2)

def side_of_line(x1, y1, x2, y2, px, py):
    cross = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)
    return 1 if cross > 0 else -1

def clean_old_tracks(state, tracks):
    active_ids = {t[0] for t in tracks}
    state["prev_positions"] = {
        tid: pos for tid, pos in state["prev_positions"].items()
        if tid in active_ids
    }

def check_cross_in(prev_side, curr_side):
    return prev_side == -1 and curr_side == 1

def check_cross_out(prev_side, curr_side):
    return prev_side == 1 and curr_side == -1

def update_counter(state, tracks, line_points, width=640, height=480):
    if line_points is None or len(line_points) != 2:
        return state["in_count"], state["out_count"]

    (lx1, ly1), (lx2, ly2) = line_points
    clean_old_tracks(state, tracks)

    for tid, x1, y1, x2, y2 in tracks:
        cx, cy = get_center(x1, y1, x2, y2)
        curr_side = side_of_line(lx1, ly1, lx2, ly2, cx, cy)
        prev_side = state["prev_positions"].get(tid)

        if prev_side is None:
            state["prev_positions"][tid] = curr_side
            continue

        if check_cross_in(prev_side, curr_side) and tid not in state["counted_in"]:
            state["in_count"] += 1
            state["counted_in"].add(tid)

        elif check_cross_out(prev_side, curr_side) and tid not in state["counted_out"]:
            state["out_count"] += 1
            state["counted_out"].add(tid)

        state["prev_positions"][tid] = curr_side

    return state["in_count"], state["out_count"]
