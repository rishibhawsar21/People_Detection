import cv2
def draw(frame, tracks, in_count, out_count, total_count, current_count, fps):
    for tid, x1, y1, x2, y2 in tracks:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, tid, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.putText(frame, f"IN: {in_count}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, f"OUT: {out_count}", (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.putText(frame, f"TOTAL: {total_count}", (20, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.putText(frame, f"CURRENT: {current_count}", (20, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 200, 0), 2)

    cv2.putText(frame, f"FPS: {int(fps)}", (20, 250),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    return frame
