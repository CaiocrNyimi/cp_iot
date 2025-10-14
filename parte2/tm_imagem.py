import os
from tensorflow.keras.models import load_model
import numpy as np
import cv2

base_path = os.path.dirname(os.path.abspath(__file__))

modelo_path = os.path.join(base_path, 'teachable_machine', 'keras_model.h5')
labels_path = os.path.join(base_path, 'teachable_machine', 'labels.txt')
imagem_path = os.path.join(base_path, 'imagens', 'pessoas.jpg')

modelo = load_model(modelo_path)

with open(labels_path, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

img = cv2.imread(imagem_path)
img_resized = cv2.resize(img, (224, 224))
img_normalized = img_resized / 255.0
img_input = np.expand_dims(img_normalized, axis=0)

pred = modelo.predict(img_input)
classe_idx = np.argmax(pred)
classe_label = labels[classe_idx]
confianca = pred[0][classe_idx]

cv2.putText(img, f"{classe_label} ({confianca:.2f})", (10,30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
saida_path = os.path.join(base_path, 'imagens', 'resultado_tm.jpg')
cv2.imwrite(saida_path, img)
print(f"Imagem salva em {saida_path}")
