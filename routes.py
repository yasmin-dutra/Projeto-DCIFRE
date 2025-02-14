from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter()

@router.post("/empresas/", response_model=schemas.EmpresaResponse)
def criar_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(database.get_db)):
    return crud.criar_empresa(db, empresa)

@router.get("/empresas/", response_model=list[schemas.EmpresaResponse])
def listar_empresas(db: Session = Depends(database.get_db)):
    return crud.listar_empresas(db)

@router.post("/obrigacoes/", response_model=schemas.ObrigacaoResponse)
def criar_obrigacao(obrigacao: schemas.ObrigacaoCreate, db: Session = Depends(database.get_db)):
    return crud.criar_obrigacao(db, obrigacao)