from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_criar_empresa():
    response = client.post("/empresas/", json={
        "nome": "Empresa Teste",
        "cnpj": "12345678000199",
        "endereco": "Rua Exemplo, 123",
        "email": "teste@email.com",
        "telefone": "123456789"
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Teste"

def test_listar_empresas():
    response = client.get("/empresas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    