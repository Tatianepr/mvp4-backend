# Minha API

Este é o MVP da sprint 04 do curso de **Engenharia de Software** da **PUC-Rio**

O objetivo aqui é disponibilizar o projeto de backend, que foi desenvolvido para usar o modelo de predição da qualidade de vinhos.

Linkendin: https://www.linkedin.com/in/tatianepr/



## Principais APIs

1) DELETE - /vinho
2) GET - /vinho
3) POST -/vinho
4) PUT - /categoria 
5) GET - /vinhos

## Arquitetura do projeto

Foi desenvolvido um frontend em JavaScript que usa as APIs desenvolvidos em Python. 

- Frontend (porta 80) -> https://github.com/Tatianepr/mvp4-frontend
- Componente de APIs (porta 5000) -> https://github.com/Tatianepr/mvp4-backend (esse)
- Modelo desenvolvido no Colab - https://colab.research.google.com/drive/1cYrJVMw-cIkE1tmr9svY5e99cu8regeV?usp=sharing
- Também migrei o modelo para uma aplicação local - 

# testes

Foi desenvolvido conjunto de cenários para avaliar a qualidade do modelo.

```
pytest test_modelos.py

```

## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

PAra criar um ambiente virtual: 

```
python -m virtualenv env
.\venv\Scripts\activate
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.
```
pip install -r requirements.txt
```


Para executar a API  basta executar:

```
flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

