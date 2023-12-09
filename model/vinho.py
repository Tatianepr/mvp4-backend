from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Pregnancies,Glucose,BloodPressure,SkinThickness,test,BMI,DiabetesPedigreeFunction,Age,Outcome

class Vinho(Base):
    __tablename__ = 'vinhos'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    type = Column("type", Integer)
    fixedacidity = Column("fixedacidity", Float)
    volatileacidity = Column("volatileacidity", Float)
    citricacid = Column("citricacid", Float)
    residualsugar = Column("residualsugar", Float)
    chlorides = Column("chlorides", Float)
    freesulfurdioxide = Column("freesulfurdioxide", Integer)
    totalsulfurdioxide = Column("totalsulfurdioxide", Integer)
    density = Column("density", Float)
    pH = Column("pH", Float)
    sulphates = Column("sulphates", Float)
    alcohol = Column("alcohol", Float)
    quality = Column("quality", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, name:str, type:int, fixedacidity:float, volatileacidity:float,
                 citricacid:float, residualsugar:float, chlorides:float, 
                 freesulfurdioxide:int, totalsulfurdioxide:int, density:float, pH:float,
                 sulphates:float, alcohol:float, quality:int, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Arguments:
            name: nome do vinho
            type: tipo de vinho (tinto=1, branco=2)
            fixedacidity: Acidez fixa
            volatileacidity: Acidez volátil
            citricacid: Ácido cítrico
            residualsuga: Acúcar redidual
            chlorides: Cloretos
            freesulfurdioxide: Dióxido de enxofre livre
            totalsulfurdioxide: Total dióxido de enxofre
            density: Densidade
            pH: PH
            sulphates: Sulfatos
            alcohol: Alcool
            outcome: diagnóstico da qualidade (1=fraco, 2=bom)
            data_insercao: data de quando o paciente foi inserido à base
        """

        self.name=name
        self.type = type
        self.fixedacidity = fixedacidity
        self.volatileacidity = volatileacidity
        self.citricacid = citricacid
        self.residualsugar = residualsugar
        self.chlorides = chlorides
        self.freesulfurdioxide = freesulfurdioxide
        self.totalsulfurdioxide = totalsulfurdioxide
        self.density = density
        self.pH = pH
        self.sulphates = sulphates
        self.alcohol = alcohol
        self.quality = quality

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao