import cv2
def takesnapshot():
    videoObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoObject.read()
        cv2.imwrite("Picture1.jpg",frame)
        result=False
    videoObject.release()
    cv2.destroyAllWindows()

takesnapshot()