from model.avaliador import Avaliador
from model.preprocessador import PreProcessador
from model.carregador import Carregador
from model.modelo import Model

# Instanciação das Classes
carregador = Carregador()
pre_processador = PreProcessador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/winequality-final_golden.csv"
colunas = ['type', 'fixedacidity', 'volatileacidity', 'citricacid', 'residualsugar', 'chlorides', 'freesulfurdioxide', 'totalsulfurdioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']
percentual_teste = 0.2

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Pré-processamento
X_train, X_test, Y_train, Y_test = pre_processador.pre_processar(dataset, percentual_teste)

# Separando em dados de entrada e saída
#X = dataset.iloc[:, 0:-1]
#Y = dataset.iloc[:, -1]
     
# Método para testar modelo KNN a partir do arquivo correspondente
def test_modelo_knn():
    # Importando modelo de KNN
    knn_path = 'ml_model/modelo_vinho_treinado.pkl'
    modelo_knn = Model.carrega_modelo(knn_path)

    # Obtendo as métricas do KNN
    acuracia_knn, recall_knn, precisao_knn, f1_knn = avaliador.avaliar(modelo_knn, X_train, Y_train)

    print (acuracia_knn)
    # Testando as métricas do KNN
    # Modifique as métricas de acordo com seus requisitoscls
    assert acuracia_knn >= 0.75 # 0.75
    assert recall_knn >= 0.5  # 0.5 
    assert precisao_knn >= 1 # 0.5 
    assert f1_knn >= 0.5 # 0.5 
    

