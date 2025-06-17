from dataclasses import dataclass,field
from datetime import datetime, timezone

@dataclass
class Utilizador :
    nome : str
    sobrenome : str
    sexo : str
    telefone : str
    email : str
    foto : str
    nome_empresa : str
    descricao : str
    hora_funcionamento : str
    concelho : str
    ilha : str
    endereco : str
    tipo : str

class Autenticacao :
    password : str
    email : str
    token_social_media : str
    user_name : str
    audit_user : str
    audit_timestamp : field(default_factory=lambda: datetime.now(timezone.utc)) # type: ignore
    utilizador : Utilizador
