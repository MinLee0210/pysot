import os
from glob import glob

import cv2


def get_frames(video_name: str = ""):
    match video_name:
        case "":
            cap = cv2.VideoCapture(0)
            # warmup
            for _ in range(5):
                cap.read()
            while True:
                ret, frame = cap.read()
                if ret:
                    yield frame
                else:
                    break
        case str():
            if video_name.endswith(".avi") or video_name.endswith(".mp4"):
                cap = cv2.VideoCapture(video_name)
                while True:
                    ret, frame = cap.read()
                    if ret:
                        yield frame
                    else:
                        break
            else:
                images = glob(os.path.join(video_name, "*.jp*"))
                images = sorted(
                    images, key=lambda x: int(x.split("/")[-1].split(".")[0])
                )
                for img in images:
                    frame = cv2.imread(img)
                    yield frame