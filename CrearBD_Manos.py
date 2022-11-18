
# -*- coding: latin-1 -*-
#from this import s
from fileinput import filename
from pickle import TRUE
import cv2
import mediapipe as mp
import numpy as np
import numpy as mean
from math import sqrt
import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
import csv


def calcularDistancia (x1,y1,x2,y2): 
    return sqrt((x1-x2)**2 + (y1-y2)**2)

lis_nomb=[]
lis_Dis6=[]
lis_Dis61=[]
lis_Dis7=[]
lis_Dis71=[]
lis_Dis8=[]
lis_Dis81=[]
lis_Dis9=[]
lis_Dis91=[]
lis_Dis10=[]
lis_Dis101=[]


def dist_Hands (fileName,nameDir):
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:

        image_R = cv2.imread(personPath + "/" + fileName)
        image_R=cv2.resize(image_R,(400,400),interpolation=cv2.INTER_CUBIC)
        height, width, _ = image_R.shape
        image = cv2.flip(image_R, 1)

        image_rgb =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = hands.process(image_rgb)

        # HANDEDNESS
        print('Handedness:', results.multi_handedness)
    

        # HAND LANDMARKS
        #print('Hand landmarks:', results.multi_hand_landmarks)

        if results.multi_hand_landmarks is not None:
            for idx, hand_handedness in enumerate(results.multi_handedness): 
                if hand_handedness.classification[0].label == "Left": 
                    Resultados=[0]
                    
                            
                if hand_handedness.classification[0].label == "Right":
                    print('Dentro de right')
                    # Dibujando los puntos y las conexiones mediante mp_drawing  
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                            mp_drawing.DrawingSpec(color=(255,255,0), thickness=4, circle_radius=2), 
                            mp_drawing.DrawingSpec(color=(255,0,255), thickness=2))
                        x0 = int(hand_landmarks.landmark[0].x * width)
                        y0 = int(hand_landmarks.landmark[0].y * height)
                        x6 = int(hand_landmarks.landmark[20].x * width)
                        y6 = int(hand_landmarks.landmark[20].y * height)
                        x61 = int(hand_landmarks.landmark[17].x * width)
                        y61 = int(hand_landmarks.landmark[17].y * height)
                        x7 = int(hand_landmarks.landmark[16].x * width)
                        y7 = int(hand_landmarks.landmark[16].y * height)
                        x71 = int(hand_landmarks.landmark[13].x * width)
                        y71 = int(hand_landmarks.landmark[13].y * height)
                        x8 = int(hand_landmarks.landmark[12].x * width)
                        y8 = int(hand_landmarks.landmark[12].y * height)
                        x81 = int(hand_landmarks.landmark[9].x * width)
                        y81 = int(hand_landmarks.landmark[9].y * height)
                        x9 = int(hand_landmarks.landmark[8].x * width)
                        y9 = int(hand_landmarks.landmark[8].y * height)
                        x91 = int(hand_landmarks.landmark[5].x * width)
                        y91 = int(hand_landmarks.landmark[5].y * height)
                        x10 = int(hand_landmarks.landmark[4].x * width)
                        y10 = int(hand_landmarks.landmark[4].y * height)
                        x101 = int(hand_landmarks.landmark[2].x * width)
                        y101 = int(hand_landmarks.landmark[2].y * height)

                        dis6= calcularDistancia(x6,y6,x0,y0)
                        dis61= calcularDistancia(x61,y61,x0,y0)
                        print('dis6:', dis6)
                

                        dis7= calcularDistancia(x7,y7,x0,y0)
                        dis71= calcularDistancia(x71,y71,x0,y0)
                      

                        dis8= calcularDistancia(x8,y8,x0,y0)
                        dis81= calcularDistancia(x81,y81,x0,y0)
                      

                        dis9= calcularDistancia(x9,y9,x0,y0)
                        dis91= calcularDistancia(x91,y91,x0,y0)
                      

                        dis10= calcularDistancia(x10,y10,x0,y0)
                        dis101= calcularDistancia(x101,y101,x0,y0)
                        print('dis101:', dis101)
                        # Dibujando los puntos de interés
                        cv2.circle(image, (x0, y0), 3,(255,0,0),3)
                        cv2.circle(image, (x6, y6), 3,(255,0,0),3)
                        cv2.circle(image, (x61, y61), 3,(255,0,0),3)
                        cv2.circle(image, (x7, y7), 3,(255,0,0),3)
                        cv2.circle(image, (x71, y71), 3,(255,0,0),3)
                        cv2.circle(image, (x8, y8), 3,(255,0,0),3)
                        cv2.circle(image, (x81, y81), 3,(255,0,0),3)
                        cv2.circle(image, (x9, y9), 3,(255,0,0),3)
                        cv2.circle(image, (x91, y91), 3,(255,0,0),3)
                        cv2.circle(image, (x10, y10), 3,(255,0,0),3)
                        cv2.circle(image, (x101, y101), 3,(255,0,0),3)
             
                    lis_nomb.append(nameDir)   
                    lis_Dis6.append(dis6)
                    print('lis_Dis6:', lis_Dis6)
                    lis_Dis61.append(dis61)
                    lis_Dis7.append(dis7)
                    lis_Dis71.append(dis71)
                    lis_Dis8.append(dis8)
                    lis_Dis81.append(dis81)
                    lis_Dis9.append(dis9)
                    lis_Dis91.append(dis91)
                    lis_Dis10.append(dis10)
                    lis_Dis101.append(dis101)
                    Resultados=[lis_nomb,lis_Dis6,lis_Dis61,lis_Dis7,lis_Dis71,lis_Dis8,lis_Dis81,lis_Dis9,lis_Dis91,lis_Dis10,lis_Dis101]
                    print('Resultados: ', Resultados)

                    
        image = cv2.flip(image, 1)
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return (Resultados)
def cerrar():
    ventana.destroy()

ca=messagebox.askquestion(title= "Calculando datos de manos ", message="Tines escaner para obtener imagenes de las manos")
print (ca)
    
if (ca=="no"):
    ventana= tk.Tk()
    ventana.geometry('450x100')
    tk.Label(ventana,text='Necesita un escaner para crear la base de datos ', font = "Calibri 16").pack()
    #Botón para cerrar ventana una vez que el usuario introdujo su nombre y apellidos
    button1 = tk.Button(ventana, text = "OK", command = cerrar).pack(side= tk.BOTTOM)
    ventana.mainloop()



else: 
    #Se muestra una GUI para que el usuario entre su nombre y apellidos para identificalo
    ventana= tk.Tk()
    ventana.geometry('400x100')
    tk.Label(ventana,text='Entre nombre y apellidos', font = "Calibri 20").pack()

    nombre=tk.StringVar()
    nomb=tk.Entry(ventana, textvariable=nombre, font = "Calibri 12", width = 40).pack()

    #Se obtiene el nombre entrado por el usuario en personName
    # para crear la carpeta de imagenes para entrenar el modelo
    def obtTex():
        personName = str(nombre.get())
        print (personName)
        return (personName)

    #Botón para cerrar ventana una vez que el usuario introdujo su nombre y apellidos
    button1 = tk.Button(ventana, text = "OK", command = cerrar).pack(side= tk.BOTTOM)
    ventana.mainloop()
    
    #Se crea una carpeta con el nombre del usuario a reconocer, 
    #esta se creará dentro de la carpeta Data que ya se había creado previamente de forma manual. 
    # Finalmente personPath será la ruta completa.

    d_Path=os.environ['SECUREMIRROR_CAPTURES']
    dataPath = d_Path + '/' + 'DB_Manos' #Cambia a la ruta donde hayas almacenado Data
    personPath = dataPath + '/' + obtTex()

    if not os.path.exists(personPath):
        print('Carpeta creada: ',personPath)
        os.makedirs(personPath)


    
    '''d_Path=os.environ['SECUREMIRROR_CAPTURES']
    print (d_Path)
    dataPath = d_Path + '/' + 'DB_Manos' #Cambia a la ruta donde hayas almacenado Data
    with os.scandir(dataPath) as ficheros:
         personPath = [fichero.name for fichero in ficheros if fichero.is_dir()]
 
    print('Nombre carpeta: ',personPath)'''

    peopleList = os.listdir(dataPath)
    print('Lista de personas: ', peopleList)

    labels = []
    handsData = []
    label = 0

    resul=[]

    ventana= tk.Tk()
    ventana.geometry('650x150')
    tk.Label(ventana,text='Antes de pulsar OK guarde 5 imagenes escaneadas de la palma \n de tu mano derecha con diferentes posiciones en la ruta: \n ' + personPath, font = "Calibri 16").pack()
    #Botón para cerrar ventana una vez que el usuario introdujo su nombre y apellidos
    button1 = tk.Button(ventana, text = "OK", command = cerrar).pack(side= tk.BOTTOM)
    ventana.mainloop()


    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        #print('Leyendo las imagenes')

        for fileName in os.listdir(personPath):
            labels.append(label)
            handsData.append(cv2.imread(personPath+'/'+fileName,0))
            image = cv2.imread(personPath+'/'+fileName,0)
            resul.append(dist_Hands (fileName,nameDir))
            #print ("dist_Hands (fileName): ",distancias)

            label = label + 1 

    print("nameDir",nameDir)

    data= {'Nombre': [nameDir]
                  , 'Mean_Dist 20-0': [(np.mean (resul[0][1]))]
                  , 'Mean_Dist 17-0': [(np.mean (resul[0][2]))]
                  , 'Mean_Dist 16-0': [(np.mean (resul[0][3]))]
                  ,'Mean_Dist 13-0': [(np.mean (resul[0][4]))]
                  ,'Mean_Dist 12-0': [(np.mean (resul[0][5]))]
                  ,'Mean_Dist 9-0': [(np.mean (resul[0][6]))]
                  ,'Mean_Dist 8-0': [(np.mean (resul[0][7]))]
                  ,'Mean_Dist 5-0': [(np.mean (resul[0][8]))]
                  ,'Mean_Dist 4-0': [(np.mean (resul[0][9]))]
                  ,'Mean_Dist 2-0': [(np.mean (resul[0][10]))]}

    print (pd.DataFrame(data))
    # Creación DataFrame:
    tab_result = pd.DataFrame(data)

    # Guarda datos en CSV:
    tab_result.to_csv(d_Path + '/' + 'datos.csv', header=["NOMBRE","Mean_Dist 20-0", "Mean_Dist 17-0","Mean_Dist 16-0","Mean_Dist 13-0","Mean_Dist 12-0","Mean_Dist 9-0","Mean_Dist 8-0","Mean_Dist 5-0","Mean_Dist 4-0","Mean_Dist 2-0"], index=False)
