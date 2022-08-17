# Projeto Cadastro de Pessoa

A funcionalidade do programa é o armazenamento de dados cadastrais de pessoas.


## 🚀 Como rodar o programa

Execute o programa:

`
$ python "Programa - Cadastro de Pessoas.py"
`

## 📋 Começando

O programa inicia com um Menu, nele o usuário pode escolher que ação gostaria de realizar adicionando uma entrada da seguinte maneira:

- Com a entrada 1: Será chamada a função para registro de contato
- Com a entrada 2: Será chamada a função para visualização da lista de contato ordenada por idade
- Com a entrada 3: Será chamada a função para visualização da lista de contato em ordem alfabética
- Com a entrada 4: Será chamada a função para visualização dos contatos ordenados por categoria(criança/adolescente/adulto/idoso)
- Com a entrada 5: Será chamada a função para finalização do programa

## ⚙️ Executando os testes

As funcionalidades pedidas estão inclusas no menu fornecido e podem ser testadas através dele, utilizando todas as opções do Menu e observando as saídas fornecidas. 

### 🔩 Exemplos de entrada e saídas


Com a entrada 1 no menu => exempo de entradas fornecidas: 
> Ana
90

Com a entrada 1 no menu => exempo de entradas fornecidas: 
> Pedro
95

Após registro de pessoas no programa, temos a lista de cadastro a seguir:

- cadastro = [('Ana',90),('Pedro',95),('Lucas',45),('Amanda',17),('Julia',1)]

Nesse caso, as **saídas esperadas** são:

-   Com a entrada 2 no menu: 
> [('Julia', 1), ('Amanda', 17), ('Lucas', 45), ('Ana', 90), ('Pedro', 95)]
-   Com a entrada 3 no menu: 
> [('Amanda', 17), ('Ana', 90), ('Julia', 1), ('Lucas', 45), ('Pedro', 95)]
-  Com a entrada 4 no menu:
      - Com a entrada 1(crianças): 
      > Julia
      - Com a entrada 2(adolescente): 
      > Amanda
      - Com a entrada 3(adultos): 
      > Lucas
      - Com a entrada 4(idosos):  
      > Ana
      Pedro

