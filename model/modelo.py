import numpy as np
import pickle
import joblib
from sklearn.preprocessing import MinMaxScaler

class Model:
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))

        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model

    def preditor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """
       
        
        X_input = np.array([
                            form.type,
                            form.fixedacidity,
                            form.volatileacidity,
                            form.citricacid,
                            form.residualsugar,
                            form.chlorides,
                            form.freesulfurdioxide,
                            form.totalsulfurdioxide,
                            form.density,
                            form.pH,
                            form.sulphates,
                            form.alcohol
                        ]).reshape(1, -1) # reshape

        scaler_in = open('ml_model/scaler_vinho.pkl', 'rb') 
        scaler_arq = pickle.load(scaler_in)
        scaler_in.close()

        rescaledX = scaler_arq.transform(X_input)
        diagnosis = model.predict(rescaledX)
       
        return int(diagnosis[0])