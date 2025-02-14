from pydantic import BaseModel, EmailStr
from typing import List, Optional

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaResponse(EmpresaBase):
    id: int
    class Config:
        orm_mode = True

class ObrigacaoBase(BaseModel):
    nome: str
    periodicidade: str

class ObrigacaoCreate(ObrigacaoBase):
    empresa_id: int

class ObrigacaoResponse(ObrigacaoBase):
    id: int
    empresa: EmpresaResponse
    class Config:
        orm_mode = True