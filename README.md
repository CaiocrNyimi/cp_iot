# Classificação e Regressão com Redes Neurais e Scikit-learn

Este repositório contém dois experimentos de aprendizado de máquina utilizando redes neurais com Keras e modelos clássicos com Scikit-learn. Os experimentos foram realizados com datasets disponíveis via Scikit-learn.

---

## Exercício 1 – Classificação Multiclasse

**Dataset:** Wine Dataset
**Objetivo:** Classificar vinhos em 3 categorias.

### Modelos treinados

#### Rede Neural (Keras)
- 2 camadas ocultas com 32 neurônios cada
- Função de ativação: ReLU
- Camada de saída com 3 neurônios e ativação Softmax
- Função de perda: `categorical_crossentropy`
- Otimizador: `Adam`

#### RandomForestClassifier (Scikit-learn)
- Modelo padrão com hiperparâmetros default

### Resultados

| Modelo                       | Precisão |
|------------------------------|----------|
| Rede Neural (Keras)          | 1.0000   |
| Random Forest (Scikit-learn) | 1.0000   |

### Análise

Os dois modelos tiveram precisão perfeita no teste, indicando que o problema de classificação é bem definido e os dados são separáveis. A rede neural e o Random Forest foram igualmente eficazes.

---

## Exercício 2 – Regressão

**Dataset:** California Housing Dataset
**Objetivo:** Prever o valor médio das casas.

### Modelos treinados

#### Rede Neural (Keras)
- 3 camadas ocultas com 64, 32 e 16 neurônios
- Função de ativação: ReLU
- Camada de saída com 1 neurônio e ativação Linear
- Função de perda: `mse`
- Otimizador: `Adam`

#### RandomForestRegressor (Scikit-learn)
- Modelo padrão com hiperparâmetros default

### Resultados

| Modelo                       | RMSE     |
|------------------------------|----------|
| Rede Neural (Keras)          | 0.5110   |
| Random Forest (Scikit-learn) | 0.5036   |

### Análise

Ambos apresentaram desempenho semelhante, com o Random Forest obtendo um RMSE ligeiramente menor. Isso mostra que ele conseguiu capturar melhor as variações dos dados, embora a rede neural também foi bastante precisa.

---

## Como rodar os experimentos

1. Clone o repositório:
   ```bash
   git clone https://github.com/CaiocrNyimi/cp_iot.git
   cd cp_iot
   ```

2. Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```

3. Execute os notebooks e confira os resultados.

## Requisitos

- Python 3.10

- Pacotes:
  - tensorflow
  - scikit-learn
  - pandas
  - numpy

## Estrutura do repositório
  ´´´
  ├── exercicio_classificacao.ipynb
  ├── exercicio_regressao.ipynb
  ├── README.md
  └── requirements.txt
  ´´´