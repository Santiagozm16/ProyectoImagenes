
import cv2
import os
import imutils

#Genera la carpeta de la emocion

emotionName = 'Enojo'
dataPath = r"D:/Uni/Septimo Semestre/Procesamiento de imagenes/Proyecto/Data"
#Cambiar la dirección por la que tienen en su equipo, si no tienen la carpeta Data, por favor creenla
emotionPath = dataPath + '/' + emotionName

if not os.path.exists(emotionPath):
    print('Carpeta creada: ',emotionPath)
    os.makedirs(emotionPath)

#Permite acceder a la camara web

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
count = 0

while True:
    #Lee cada frame
    ret, frame = cap.read()
    if ret == False: break
    frame =  imutils.resize(frame, width=640)
    #Cambie el color del frame para clasificarlo
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()
    faces = faceClassif.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        #Genera el recuadro de identificación
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        #Guarda las fotos
        cv2.imwrite(emotionPath + '/rotro_{}.jpg'.format(count),rostro)
        count = count + 1
    cv2.imshow('frame',frame)
    k =  cv2.waitKey(1)
    #Contador para almacenar las 300 imagenes
    if k == 27 or count >= 300:
        break

    
cap.release()
cv2.destroyAllWindows()
