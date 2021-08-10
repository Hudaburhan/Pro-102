import cv2
import time
import random
import dropbox

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result= True
    while(result):
        # read frames while the camera is on
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        result= False
    
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
    
def upload_file(img_name):
    access_token="sl.A15J9YDh4cKp2QBomWMcrHJmpbVGtV1VkhwE3Qgy5LGHAm1jje-1c5p4wlHn8_tkR_9y-y8tOaWHIaGpDAOE0QKDsF1FXIPvqsVtRTf_19Ri4S1oVheNv9j97AVdTC3hFj4FPbI"
    file = img_name
    file_from= file
    file_to="/newFolder1/"+(img_name)
    dbx= dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode= dropbox.files.WriteMode.overwrite)
        print("file_uploaded")


def main():
    while(True):
        if((time.time() - start_time)>=10):
            name= take_snapshot()
            upload_file(name)

main()
# take_snapshot()
# print(time.time())
print(random.randint(0,9))