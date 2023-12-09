from pydantic import BaseModel
from typing import Optional, List
from model.vinho import Vinho
import json
import numpy as np

class VinhoSchema(BaseModel):
    """ Define como um novo vinho a ser inserido deve ser representado
    """
    name: str = "Carbernet Miolo"
    type: int = 1
    fixedacidity: float = 11.2
    volatileacidity: float = 0.28
    citricacid: float = 0.56
    residualsugar: float = 1.9
    chlorides: float = 0.075
    freesulfurdioxide: int = 17
    totalsulfurdioxide: int = 60
    density: float = 0.998
    pH: float = 3.15
    sulphates: float = 0.58
    alcohol: float = 9.8
    
class VinhoViewSchema(BaseModel):
    """Define como um vinho será retornado
    """
    id: int = 1
    type: int = 1
    fixedacidity: float = 11.2
    volatileacidity: float = 0.28
    citricacid: float = 0.56
    residualsugar: float = 1.9
    chlorides: float = 0.075
    freesulfurdioxide: int = 17
    totalsulfurdioxide: int = 60
    density: float = 0.998
    pH: float = 3.15
    sulphates: float = 0.58
    alcohol: float = 9.8
    quality: int = None
    
class VinhoBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do vinho.
    """
    name: str = "Carbernet Miolo"

class ListaVinhosSchema(BaseModel):
    """Define como uma lista de vinhos será representada
    """
    vinhos: List[VinhoSchema]

    
class VinhoDelSchema(BaseModel):
    """Define como um vinho para deleção será representado
    """
    name: str = "Carbernet Miolo"
    
# Apresenta apenas os dados de um vinho    
def apresenta_vinho(vinho: Vinho):
    """ Retorna uma representação do vinho seguindo o schema definido em
        VinhoViewSchema.
    """
    return {
        "id": vinho.id,
        "name": vinho.name,
        "type": vinho.type,
        "fixedacidity": vinho.fixedacidity,
        "volatileacidity": vinho.volatileacidity,
        "citricacid": vinho.citricacid,
        "residualsugar": vinho.residualsugar,
        "chlorides": vinho.chlorides,
        "freesulfurdioxide": vinho.freesulfurdioxide,
        "totalsulfurdioxide": vinho.totalsulfurdioxide,
        "density": vinho.density,
        "pH": vinho.pH,
        "sulphates": vinho.sulphates,
        "alcohol": vinho.alcohol,
        "quality": vinho.quality
    }
    
# Apresenta uma lista de pacientes
def apresenta_vinhos(vinhos: List[Vinho]):
    """ Retorna uma representação do vinho seguindo o schema definido em
        VinhoViewSchema.
    """
    result = []
    for vinho in vinhos:
        result.append({
            "id": vinho.id,
            "name": vinho.name,
            "type": vinho.type,
            "fixedacidity": vinho.fixedacidity,
            "volatileacidity": vinho.volatileacidity,
            "citricacid": vinho.citricacid,
            "residualsugar": vinho.residualsugar,
            "chlorides": vinho.chlorides,
            "freesulfurdioxide": vinho.freesulfurdioxide,
            "totalsulfurdioxide": vinho.totalsulfurdioxide,
            "density": vinho.density,
            "pH": vinho.pH,
            "sulphates": vinho.sulphates,
            "alcohol": vinho.alcohol,
            "quality": vinho.quality
        })

    return {"vinhos": result}

