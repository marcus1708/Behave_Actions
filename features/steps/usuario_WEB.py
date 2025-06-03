from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://front.serverest.dev/login"

@given("estou na página de login")
def step_impl(context):
    context.driver.get(base_url)

@when("eu clico em Cadastre-se")
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/small/a').click()

@when('eu cadastro o novo usuário com nome "{nome}", email "{email}" e senha "{senha}"')
def step_impl(context, nome, email, senha):
    context.driver.find_element(By.ID, "nome").send_keys(nome)
    context.driver.find_element(By.ID, "email").send_keys(email)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "administrador").click()
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[5]/button').click()
    wait = WebDriverWait(context.driver, 10)

@then("o usuario é cadastrado com sucesso")
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    pass

@when('eu realizo login com email "{email}" e senha "{senha}"')
def step_impl(context, email, senha):
    context.driver.find_element(By.ID, "email").send_keys(email)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/button').click()
    wait = WebDriverWait(context.driver, 10)
    
@then('o usuario é logado com sucesso')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    pass

@then('os usuarios sao exibidos')
def step_impl(context):
    context.driver.get('https://front.serverest.dev/admin/home')
    context.driver.find_element(By.XPATH, '//*[@id="navbarTogglerDemo01"]/ul/li[3]/a').click()
    wait = WebDriverWait(context.driver, 10)
    