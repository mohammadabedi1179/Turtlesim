import cv2
class opencv:
    def __init__(self):
        pass

    def to_binary(self,frame,lower,upper):

        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        binary=cv2.inRange(hsv,lower,upper)

        return binary

    def enhance_binary(self,binary_image,iterations_erode,iterations_dilate):

        ero = cv2.erode(binary_image,None,iterations=iterations_erode)
        dial = cv2.dilate(ero,None,iterations=iterations_dilate)

        return dial

    def ball_detection(self,image_binary,image_color):

        cnts , _ = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        center = (0,0)
        r=0

        for cnt in cnts:

         (x,y),r = cv2.minEnclosingCircle(cnt)

         r = int(r)
         center = (int(x),int(y))
         cv2.circle(image_color,center,r,(0,255,0),2)
         cv2.circle(image_color,center,3,(255,0,0),3)
         return(image_color,center,r)

        return(image_color,center,r)