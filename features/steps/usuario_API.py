import requests, json
from behave import given, when, then
from pathlib import Path

# ---------- CRIAR USUÁRIO ----------
@given("que desejo cadastrar um novo usuário")
def step_given_create_user(context):
    user_json = Path(__file__).parent / "user.json"
    with open(user_json, "r", encoding="utf-8") as f:
        context.payload = json.load(f)
    context.url = "https://serverest.dev/usuarios"

@when("envio uma requisição POST para criar o usuário")
def step_when_post_user(context):
    context.response = requests.post(context.url, json=context.payload)

@then("o status da resposta deve ser 201")
def step_then_status_201(context):
    assert context.response.status_code == 201

@then("eu salvo o ID do usuário criado")
def step_then_save_user_id(context):
    json_data = context.response.json()
    context.user_id = json_data.get("_id") or json_data.get("id")
    assert context.user_id, "ID não encontrado na resposta da API"
    with open("user_id.json", "w", encoding="utf-8") as f:
        json.dump({"id": context.user_id}, f, indent=2)

# ---------- LOGIN USUÁRIO ----------
@given("que desejo logar com um usuário")
def step_given_login_user(context):
    user_json = Path(__file__).parent / "user.json"
    with open(user_json, "r", encoding="utf-8") as f:
        user_data = json.load(f)
    # Filtra apenas os campos necessários para login
    context.login_payload = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    context.login_url = "https://serverest.dev/login"
@when("envio uma requisição POST para login")
def step_when_post_login(context):
    context.login_response = requests.post(context.login_url, json=context.login_payload)

@then("o status do login deve ser 200")
def step_then_status_login(context):
    assert context.login_response.status_code == 200

@then("eu salvo o token de autenticação")
def step_then_save_token(context):
    json_data = context.login_response.json()
    context.token = json_data.get("authorization")
    assert context.token, "Token não encontrado na resposta de login"
    with open("token.json", "w", encoding="utf-8") as f:
        json.dump({"token": context.token}, f, indent=2)

# ---------- BUSCAR TODOS OS USUÁRIOS ----------
@when("eu buscar a lista de usuários")
def step_when_get_users(context):
    url = "https://serverest.dev/usuarios"
    context.response = requests.get(url)

@then("o status da resposta deve ser 200")
def step_then_status_200(context):
    assert context.response.status_code == 200

# ---------- BUSCAR USUÁRIO POR ID ----------
@when("eu buscar o usuário pelo ID")
def step_when_get_user_by_id(context):
    with open("user_id.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        context.user_id = data["id"]
    url = f"https://serverest.dev/usuarios/{context.user_id}"
    context.response = requests.get(url)

# ---------- ATUALIZAR USUÁRIO ----------
@given("que desejo atualizar um usuário")
def step_given_update_user(context):
    user_json = Path(__file__).parent / "user.json"
    with open(user_json, "r", encoding="utf-8") as f:
        context.payload = json.load(f)
    # Carrega o ID do usuário salvo após o cadastro
    with open("user_id.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        context.user_id = data["id"]
    context.url = f"https://serverest.dev/usuarios/{context.user_id}"

@when("envio uma requisição PUT para atualizar o usuário")
def step_when_put_user(context):
    context.response = requests.put(context.url, json=context.payload)

# ---------- DELETAR USUÁRIO ----------
@when("eu excluir o usuário pelo ID")
def step_when_delete_user(context):
    with open("user_id.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        context.user_id = data["id"]
    url = f"https://serverest.dev/usuarios/{context.user_id}"
    context.response = requests.delete(url)
