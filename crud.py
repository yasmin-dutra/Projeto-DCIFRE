from sqlalchemy.orm import Session
import models, schemas

def criar_empresa(db: Session, empresa: schemas.EmpresaCreate):
    nova_empresa = models.Empresa(**empresa.dict())
    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)
    return nova_empresa

def listar_empresas(db: Session):
    return db.query(models.Empresa).all()

def criar_obrigacao(db: Session, obrigacao: schemas.ObrigacaoCreate):
    nova_obrigacao = models.ObrigacaoAcessoria(**obrigacao.dict())
    db.add(nova_obrigacao)
    db.commit()
    db.refresh(nova_obrigacao)
    return nova_obrigacao
