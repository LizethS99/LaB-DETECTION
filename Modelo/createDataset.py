import os
import random
import cv2
import shutil
import pandas as pd

EvaluateImages=[]
TrainImages=[]
df_PH2 = pd.read_excel("PH2_Extend.xlsx")
numImage=len(os.listdir("./DatasetTransformer"))
numEvaluate=int(numImage*.1)
if os.path.exists("./MelanomaEvaluate"):
    shutil.rmtree("./MelanomaEvaluate")
if os.path.exists("./MelanomaTrain"):
    shutil.rmtree("./MelanomaTrain")
os.mkdir("./MelanomaEvaluate")
os.mkdir("./MelanomaTrain")
print("Imagenes totales: "+str(numImage))
print("Train images: "+str(numImage*.7))
print("Evaluate images: "+str(numImage*.3))
cont=0
contEvaluate=0
for img in os.listdir('./DatasetTransformer'):
    cont+=1
    if contEvaluate < numEvaluate:
        if random.randint(1,15) < 3:
            #Crear imagen en la carpeta Evaluate
            EvaluateImages.append(img[:7])
            contEvaluate+=1
            imagen = cv2.imread(os.path.join('./DatasetTransformer', img))
            cv2.imwrite(os.path.join('./MelanomaEvaluate', img), imagen)
        else:
            #Crear imagen en la carpeta Train
            TrainImages.append(img[:7])
            imagen = cv2.imread(os.path.join('./DatasetTransformer', img))
            cv2.imwrite(os.path.join('./MelanomaTrain', img), imagen)
    else:
        #Crear imagen en la carpeta Train
        print("Train: "+img)
        TrainImages.append(img[:7])
        imagen = cv2.imread(os.path.join('./DatasetTransformer', img))
        cv2.imwrite(os.path.join('./MelanomaTrain', img), imagen)

EvaluateImgs_df = df_PH2[df_PH2['Image Name'].isin(EvaluateImages)]
with pd.ExcelWriter("PH2_Evaluate.xlsx",if_sheet_exists='replace',engine='openpyxl',mode="a") as writer:        
    EvaluateImgs_df.to_excel(writer, index=False)
TrainImgs_df = df_PH2[df_PH2['Image Name'].isin(TrainImages)]
with pd.ExcelWriter("PH2_Train.xlsx",if_sheet_exists='replace',engine='openpyxl',mode="a") as writer2:        
    TrainImgs_df.to_excel(writer2, index=False)
    
