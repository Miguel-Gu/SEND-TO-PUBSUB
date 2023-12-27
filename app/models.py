from datetime import date
from pydantic import BaseModel


class DadosUsuario(BaseModel):
    nome: str
    email: str
    cpf: str
    datanascimento: date
    cep: str
    endereco: str
    numero: str
    complemento: str

class UsuarioEntrada(BaseModel):
    usuario: DadosUsuario
