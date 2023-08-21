import cv2
from cvzone.FaceDetectionModule import FaceDetector 

cap = cv2.VideoCapture(1)

detector = FaceDetector(minDetectionCon = 0.75 )

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img,draw=True)

    if bboxs:
        for idx, bbox in enumerate(bboxs):
            x, y, w, h = bbox['bbox']
            if x < 0: x = 0
            if y < 0: y = 0

            img_crop = img[y:y+h, x:x+w]
            img_blur = cv2.blur(img_crop, (45, 45 ))
            #cv2.imshow(f'Img cropped: {idx}', img_crop)
            #img[y:y+h, x:x+w] = img_blur

            
            img[y:y + h, x:x + w] = img_blur

            cv2.putText(img, "Who??", ((x+x+w-10)//2, (y+y+w)//2), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 3)

    cv2.imshow('img',img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    

cv2.destroyAllWindows()
cap.release()

    