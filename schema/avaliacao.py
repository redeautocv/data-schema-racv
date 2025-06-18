from dataclasses import dataclass, asdict, field

@dataclass
class Avaliacao:
    limpeza : int
    estado_viatura : int
    comentario : str
    model : int
    localizacao : int
    foto : str
    Audit_user : str
    audit_timestamp : str 

