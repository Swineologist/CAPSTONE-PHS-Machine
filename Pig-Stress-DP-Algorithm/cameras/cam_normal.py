import cv2
ds_factor=0.6
class Cam_Norm(object):
    def __init__(self):
       self.video = cv2.VideoCapture(0)
       self.video.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        #extracting frames
            ret, frame = self.video.read()
            #frame=cv2.resize(frame,(500,500),fx=ds_factor,fy=ds_factor, interpolation=cv2.INTER_AREA)                    
            ret, jpeg = cv2.imencode('.jpg', frame)
            byts = jpeg.tobytes()
            return frame, byts