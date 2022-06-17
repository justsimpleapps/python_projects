import cv2

# import the local cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#to capture video, 0 to capture from webcam
cap= cv2.VideoCapture(0)

while True:
    _, img=cap.read() #read the frame

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grayscale

    faces = face_cascade.detectMultiScale(gray, 1.1, 4) #detect the faces

    for(x,y,w, h ) in faces:                                 #draw the rectangle around each face
        cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0), 2)

    cv2.imshow('img', img)  #display

    k=cv2.waitKey(30) & 0xff #stop if escape key is pressed
    if k==27:
        break

cap.release() #release the video capture object
cv2.destroyAllWindows()

