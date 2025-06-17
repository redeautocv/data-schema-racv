from dataclasses import dataclass
from datetime import datetime
@dataclass
class  Anuncio :
    marca : str
    modelo : str
    numero_passageiro : str
    combustivel : str
    ano : str
    preco : str
    caucao : str
    fotografia : str
    caixa_velocidade : str
    ar_condicionado : str
    data : datetime
    gps : str 
    disponibilidade : str 
    audit_user : str 
    audit_timestamp : str 
    
