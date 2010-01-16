class Tracker:
    def __init__(self):
        pass
    
    def track(self, frame, lastframe):
        threshold=64

        diff=cvCreateImage(cvSize(frame.width, frame.height), frame.depth, 3)
        bitimage=cvCreateImage(cvSize(frame.width, frame.height), frame.depth, 3)
                
        cvAbsDiff(frame,lastframe,diff)
        cvThreshold(diff,bitimage,threshold,255,CV_THRESH_BINARY)
        return bitimage
