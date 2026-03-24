import time
import cv2
import warnings

from src.counter import create_counter, update_counter
from src.detector import detect_persons
from src.tracker import update_tracks
from src.utils.visualization import draw

warnings.filterwarnings("ignore", category=UserWarning) 

VIDEO = "D:\\OB_practice\\People_detection\\videos\\test_20.mp4"
FPS = 10

cap = cv2.VideoCapture(VIDEO)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

line_points = [None]
drag_state = [False, None, None, None, None]



counter = create_counter(offset=15)
mouse_param = [line_points, drag_state, counter]

def on_mouse(event, x, y, flags, param):
    pts, drag, ctr = param
    if event == cv2.EVENT_LBUTTONDOWN:
        drag[0] = True
        drag[1], drag[2] = x, y
        drag[3], drag[4] = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        if drag[0]:
            start_x, start_y = drag[1], drag[2]
            if abs(x - start_x) > 5 or abs(y - start_y) > 5:
                pts[0] = [(start_x, start_y), (x, y)]
               
                ctr["prev_positions"] = {}
                ctr["counted_in"] = set()
                ctr["counted_out"] = set()
        drag[0] = False
        drag[1] = drag[2] = drag[3] = drag[4] = None
    elif event == cv2.EVENT_MOUSEMOVE and drag[0]:
        drag[3], drag[4] = x, y

cv2.namedWindow("People Counter")
cv2.setMouseCallback("People Counter", on_mouse, mouse_param)


frame_id = 0
while True:
    t0 = time.time()
    ret, frame = cap.read()
    if not ret:
        break

    frame_id += 5

    # print progress every 10 frames
    print(f"Processing frame {frame_id}...")

    if frame_id % 2 != 0:
        continue

    frame = cv2.resize(frame, (720, 480))
    h, w = frame.shape[:2]
    pts = line_points[0]
    is_dragging = drag_state[0]

    try:
        detections = detect_persons(frame)
        tracks = update_tracks(detections, frame)
        in_count, out_count = update_counter(counter, tracks, line_points=pts, width=w, height=h)
    except Exception as e:
        print(e)
        continue

    total_count = in_count + out_count
    current_count = in_count - out_count
    frame = draw(frame, tracks, in_count, out_count, total_count, current_count, 1 / (time.time() - t0))

    if is_dragging and drag_state[1] is not None and drag_state[3] is not None:
        cv2.line(frame, (drag_state[1], drag_state[2]), (drag_state[3], drag_state[4]), (255, 0, 0), 2)
    elif pts is not None and len(pts) == 2:
        cv2.line(frame, tuple(pts[0]), tuple(pts[1]), (255, 0, 0), 2)

    hint = "Drag to draw line" if not pts else "Drag to redraw line"
    cv2.putText(frame, hint, (10, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.imshow("People Counter", frame)

    if 1 / FPS > time.time() - t0:
        time.sleep(1 / FPS - (time.time() - t0))

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()