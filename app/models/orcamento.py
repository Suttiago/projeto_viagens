from pydantic import BaseModel
from datetime import date

class Orcamento(BaseModel):
    destino : str 
    check_in : date
    check_out : date
    adultos: int
    criancas : int