import cv2
cap= cv2.VideoCapture(-1)
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow("Frame",frame)
    if ret == False:
        break
    key=cv2.waitKey(100)
    if key==27:
        cv2.imwrite('Hich.PNG',frame)
        break



cap.release()
cv2.destroyAllWindows()



