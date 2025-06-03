Feature: CRUD de usuários no Serverest

  Scenario: Criar, buscar, atualizar e deletar um usuário
    Given eu tenho os dados de um novo usuário
    When eu envio uma requisição POST para criar o usuário
    Then o status da resposta deve ser 201

    When eu envio uma requisição GET para buscar o usuário
    Then o status da resposta deve ser 200

    When eu envio uma requisição PUT para atualizar o usuário
    Then o status da resposta deve ser 200

    When eu envio uma requisição DELETE para deletar o usuário
    Then o status da resposta deve ser 200
