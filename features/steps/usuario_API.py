import requests
import json
from behave import given, when, then

base_url = "https://serverest.dev/usuarios"

@given("eu tenho os dados de um novo usuário")
def step_given_user_data(context):
    context.payload = {
        "nome": "Marcus Teste",
        "email": f"marcus{str(hash(context))[:6]}@qa.io",
        "password": "123456",
        "administrador": "true"
    }

@when("eu envio uma requisição POST para criar o usuário")
def step_post_user(context):
    context.response = requests.post(base_url, json=context.payload)
    context.user_id = context.response.json().get("_id")

@when("eu envio uma requisição GET para buscar o usuário")
def step_get_user(context):
    url = f"{base_url}/{context.user_id}"
    context.response = requests.get(url)

@when("eu envio uma requisição PUT para atualizar o usuário")
def step_put_user(context):
    update_payload = {
        "nome": "Marcus Atualizado",
        "email": context.payload["email"],
        "password": "123456",
        "administrador": "true"
    }
    url = f"{base_url}/{context.user_id}"
    context.response = requests.put(url, json=update_payload)

@when("eu envio uma requisição DELETE para deletar o usuário")
def step_delete_user(context):
    url = f"{base_url}/{context.user_id}"
    context.response = requests.delete(url)

@then("o status da resposta deve ser {status_code:d}")
def step_check_status(context, status_code):
    assert context.response.status_code == status_code, f"Esperado {status_code}, mas retornou {context.response.status_code}"
