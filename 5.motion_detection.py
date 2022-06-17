import cv2 ,time

video= cv2.VideoCapture(0)
address='http://100.69.149.191:8080/video'
video.open(address)

first_frame=None

while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21), 0)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    threshold_frame=cv2.threshold(delta_frame,50,250,cv2.THRESH_BINARY)[1]
    threshold_frame=cv2.dilate(threshold_frame,None,iterations=2)

    (cntr,_)=cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cntr:
        if cv2.contourArea(contour)<1000:
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("motion_detection_frame", frame)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

video.release()
cv2.destroyAllWindows()

    




