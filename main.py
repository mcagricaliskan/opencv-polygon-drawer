import time
import cv2
import numpy as np


class PoligonDrawer:
    def __init__(self):
        self.polygon = []

    def mouse_callback(self, event, x, y, buttons, user_param):
        if event == cv2.EVENT_MOUSEMOVE:
            # triggers to every mouse movement
            pass
        elif event == cv2.EVENT_LBUTTONDOWN:
            # Left click
            print(f"""[{x}, {y}] saved to polygon list""")
            self.polygon.append([x, y])
            print(f"New Polygon List: {self.polygon}")

        elif event == cv2.EVENT_RBUTTONDOWN:
            # Right click
            pass

    def main(self):

        cap = cv2.VideoCapture("./traffic.mp4")
        start_time = time.time()
        while True:
            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (1280, 720))

                if len(self.polygon) > 1:
                    pts = np.array(self.polygon,
                                   np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    is_closed = True
                    # BGR: BLUE
                    color = (255, 0, 0)
                    # Line thickness of 2 px
                    thickness = 2

                    cv2.polylines(frame, [pts],
                                  is_closed, color, thickness)

                cv2.namedWindow("img", flags=cv2.WINDOW_AUTOSIZE)
                cv2.imshow("img", frame)
                cv2.setMouseCallback("img", self.mouse_callback)
                k = cv2.waitKey(1)
                if ord("q") == k:
                    cv2.destroyAllWindows()
                    cap.release()
                    break
            else:
                break

        print(
            f"Took {time.time() - start_time} Sec, Final Polygon List:\n{self.polygon}")


if __name__ == "__main__":
    pd = PoligonDrawer()
    pd.main()
