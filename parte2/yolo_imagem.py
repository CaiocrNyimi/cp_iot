from ultralytics import YOLO
import cv2

# Carrega o modelo pré-treinado YOLOv8 (versão nano, mais leve)
modelo = YOLO('yolov8n.pt')

# Caminho da imagem local
imagem_path = 'C:\\Users\\labsfiap\\Downloads\\cp_iot\\parte2\\imagens\\pessoas.jpg'

# Faz a predição
resultados = modelo(imagem_path)

# Exibe o resultado com as detecções
for resultado in resultados:
    imagem = resultado.plot()  # desenha as caixas e rótulos
    cv2.imshow("Detecção YOLOv8", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
