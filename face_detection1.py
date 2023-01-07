import streamlit as st
import cv2

st.title("Face_Detection")

def face_detect():
    cap = cv2.VideoCapture(0)

    face_classifier = cv2.CascadeClassifier('face_cascade.xml') ## classifier model ko implement krne ke liye 
    ## face_classifier is a variable which stores the xml file of faces 

    while True:

        bt , frame = cap.read() ## bt and fro are two variables bt is a kind of boolean variable, and fro is a frame variable
        ## it will read the camera 
        bw=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## cvtColor is used for detecting colours.

        faces = face_classifier.detectMultiScale(bw, scaleFactor=1.1, minNeighbors = 5 )
        # faces = variable 

        for (x, y, w, h) in faces: ## for
            cv2.rectangle(frame, (x,y),(x+w, y+h), (255, 0, 0), 3) ##faces we
            ## x and y is a postion, w and h is a width and height ## 255,0,0 is a colour 
            ##3 is width of sides
        
        cv2.imshow('face detection', frame) ## imread is to read any image and fro_1 is basically data frame

        if cv2.waitKey(10) &  0xFF == ord('q'):
            st.header("A Face is detected")
            break
    cap.release()
    cv2.destroyAllWindows()
cb = st.button("Start Face Detection...............")
if cb:
    face_detect()
