from os import access
import cv2
import dropbox
import time
import random

start_time=time.time()

def takesnapshot():
    number=random.randint(0,200)
    videoObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoObject.read()
        image_name="Picture"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("SNAPSHOT HAS BEEN TAKEN")
    videoObject.release()
    cv2.destroyAllWindows()

def uploadfile(image_name):
    access_token="sl.A6Rhl5J3RPVr5_uUI2yk3cuzGk8cI4UWRDBGlneoZFUnTNHzhk9QTaBl6_XepyKghgQw0TUfiyRg6zNwAv9GeRIFlpKwV9qEMPjBdBx7Oq6s_x02SK8a6zepYSLtRzFicP_mBeA"
    file=image_name
    filefrom=file
    fileto="/testfolder/"+(image_name)
    dbx=dropbox.Dropbox(access_token)

    with open(filefrom,'r') as f:
        dbx.fileupload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("FILES UPLOADED")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=takesnapshot()
            uploadfile(name)

main()

