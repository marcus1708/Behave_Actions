Feature: Fluxo completo de usuário na API Serverest

  Scenario: Criar usuário
    Given que desejo cadastrar um novo usuário
    When envio uma requisição POST para criar o usuário
    Then o status da resposta deve ser 201
    And eu salvo o ID do usuário criado

  Scenario: Login do usuário
    Given que desejo logar com um usuário
    When envio uma requisição POST para login
    Then o status do login deve ser 200
    And eu salvo o token de autenticação

  Scenario: Buscar lista de usuários
    When eu buscar a lista de usuários
    Then o status da resposta deve ser 200

  Scenario: Buscar usuário por ID
    When eu buscar o usuário pelo ID
    Then o status da resposta deve ser 200

  Scenario: Atualizar usuário
    Given que desejo atualizar um usuário
    When envio uma requisição PUT para atualizar o usuário
    Then o status da resposta deve ser 200

  Scenario: Deletar usuário
    When eu excluir o usuário pelo ID
    Then o status da resposta deve ser 200
