# Projeto CP_IoT

Este repositório contém dois conjuntos de experimentos de aprendizado de máquina e visão computacional:  
1. **Classificação e Regressão com Redes Neurais e Scikit-learn**  
2. **Detecção de Pessoas e Objetos em Imagens com YOLOv8 e Teachable Machine**

---
## Integrantes
CAIO NYIMI - RM556331
HENZO PUCHETTI - RM555179
LUANN MARIANO - RM558548

## Parte 1 – Classificação e Regressão

### Exercício 1 – Classificação Multiclasse
- **Dataset**: Wine Dataset  
- **Objetivo**: Classificar vinhos em 3 categorias.

**Modelos treinados**
- **Rede Neural (Keras)**  
  - 2 camadas ocultas com 32 neurônios cada  
  - Função de ativação: ReLU  
  - Camada de saída: 3 neurônios, Softmax  
  - Função de perda: categorical_crossentropy  
  - Otimizador: Adam
- **RandomForestClassifier (Scikit-learn)**  
  - Modelo padrão com hiperparâmetros default

**Resultados**
| Modelo                | Precisão |
|----------------------|----------|
| Rede Neural (Keras)   | 1.0000   |
| Random Forest         | 1.0000   |

**Análise:**  
Ambos os modelos obtiveram precisão perfeita, mostrando que os dados são bem separáveis.

---

### Exercício 2 – Regressão
- **Dataset**: California Housing Dataset  
- **Objetivo**: Prever o valor médio das casas.

**Modelos treinados**
- **Rede Neural (Keras)**  
  - 3 camadas ocultas: 64, 32, 16 neurônios  
  - Ativação ReLU  
  - Camada de saída: 1 neurônio, Linear  
  - Função de perda: MSE  
  - Otimizador: Adam
- **RandomForestRegressor (Scikit-learn)**  
  - Modelo padrão com hiperparâmetros default

**Resultados**
| Modelo                | RMSE   |
|----------------------|--------|
| Rede Neural (Keras)   | 0.5110 |
| Random Forest         | 0.5036 |

**Análise:**  
O Random Forest teve desempenho ligeiramente melhor, mas ambos modelos foram precisos.

---

## Parte 2 – Detecção de Pessoas e Objetos

### Objetivo
Comparar duas abordagens de detecção de objetos e pessoas em imagens:  
1. **YOLOv8** (pré-treinado)  
2. **Teachable Machine / TensorFlow** (modelo personalizado)

### Ferramentas Utilizadas
- **YOLOv8**  
- **TensorFlow / Keras**

### Dataset / Imagens
- Imagens de teste: `parte2/imagens/pessoas.jpg`  
- Dataset original: [INSIRA LINK AQUI - Roboflow, Kaggle ou Google Drive]  

### Hiperparâmetros e Configurações
**YOLOv8**
- Modelo: `yolov8n.pt` (nano)  
- Entrada: imagens estáticas  
- Saída: caixas delimitadoras e rótulos  

**Teachable Machine**
- Modelo: `keras_model.h5`  
- Entrada: imagens estáticas  
- Saída: classificação de acordo com categorias treinadas  
- Observação: Problemas de compatibilidade com TensorFlow 2.20.0

### Comparativo
| Abordagem          | Facilidade de uso | Precisão | Observações |
|-------------------|----------------|----------|-------------|
| YOLOv8             | Alta           | Alta     | Detecta múltiplos objetos rapidamente, pronto para uso |
| Teachable Machine  | Média          | Média/Alta | Requer conversão do modelo `.h5`, atualmente não funcional |

### Resultados
- **YOLOv8**: Funcionando corretamente, detectando pessoas na imagem de teste.  
- **Teachable Machine**: Não está funcionando devido a problemas de compatibilidade.

---

## Como Rodar

### Parte 1
1. Instalar dependências:
```bash
pip install -r requirements.txt
