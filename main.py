import cv2
from util import get_limits
from PIL import Image

yellow = [0,255,255] # yellow in BGR
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImg = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    # print(bbox)
    if bbox is not None:
        x1,y1,x2,y2 = bbox

        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)

    print(bbox)
    cv2.imshow('fraame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
