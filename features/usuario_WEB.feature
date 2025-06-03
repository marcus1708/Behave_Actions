Feature: Autom Web no Serverest

  Scenario: Criar e Logar um usuário
    Given estou na página de login
    When eu clico em Cadastre-se
    When eu cadastro o novo usuário com nome "QA", email "qa@qa.io" e senha "123"
    Then o usuario é cadastrado com sucesso

    Given estou na página de login
    When eu realizo login com email "qa@qa.io" e senha "123"
    Then o usuario é logado com sucesso

    
