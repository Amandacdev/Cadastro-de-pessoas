listaNome = []
listaIdade = []
cadastro = []
ativo = True

#Função para exibir o menu
def menu():
  print('PARA CADASTRAR CONTATO: 1')
  print('PARA VISUALIZAR LISTA DE CONTATOS - ORGANIZADA POR IDADE: 2')
  print('PARA VISUALIZAR LISTA DE CONTATOS - ORGANIZADA POR ORDEM ALFABÉTICA : 3')
  print('PARA VISUALIZAR AS CATEGORIAS DOS CADASTRADOS: 4')
  print('PARA ENCERRAR O PROGRAMA: 5')
  numero = int(input('Digite um número:'))

  if(numero == 1):
    registrarContato()
  elif(numero == 2):
    visualizarContato(1)
  elif(numero == 3):
    visualizarContato(0)
  elif(numero == 4):
    categoriaContato()
  elif(numero == 5):
    return False
  return True

#Função para registro de contatos
def registrarContato():
  nome = input('Digite o nome:')
  idade = int(input('Digite a idade:'))

  if(idade<0):
    print('Idade inválida.')
  else:
    pessoa = (nome,idade) 
    cadastro.append(pessoa)

    listaNome.append(nome)
    listaIdade.append(idade)

#Função para mostrar lista organizada por idade(se o argumento for igual a 1) ou por ordem alfabética(se a argumento for igual a 0)
def visualizarContato(a):
  cadastroOrd = list(cadastro) 
  tam = len(cadastro)

  for k in range(tam-1):
    for i in range(tam-1):
      if(cadastroOrd[i][a]>cadastroOrd[i+1][a]):
        aux = cadastroOrd[i]
        cadastroOrd[i] = cadastroOrd[i+1]
        cadastroOrd[i+1] = aux
  print(cadastroOrd)

#Função para exibir contatos em categorias
def categoriaContato():
  categoriaCrianca = 'Pessoa(s) cadastrada(s) com idade(s) entre 0 e 12 anos (criança): \n'
  categoriaAdolescente = 'Pessoa(s) cadastrada(s) com idade(s) entre 13 e 19 anos (adolescente): \n'
  categoriaAdulto = 'Pessoa(s) cadastrada(s) com idade(s) entre 20 e 65 anos (adulta): \n'
  categoriaIdosa = 'Pessoa(s) cadastrada(s) com idade(s) maior que 65 anos (idosa): \n'

  for i in range(len(cadastro)):
    if(cadastro[i][1] <= 12):
      categoriaCrianca += cadastro[i][0] + '\n'
    elif(cadastro[i][1] <= 19):
      categoriaAdolescente += cadastro[i][0] + '\n'
    elif(cadastro[i][1] <= 65):
      categoriaAdulto += cadastro[i][0] + '\n'
    else:
      categoriaIdosa += cadastro[i][0] + ' \n'
    
  print('Gostaria de ver a lista de crinças(1), adolescentes(2), adultos(3) ou idosos(4)?')

  n = int(input('Informe um número:'))

  if(n == 1):
    print(categoriaCrianca)
  elif(n == 2):
    print(categoriaAdolescente)
  elif(n == 3):
    print(categoriaAdulto)
  elif(n == 4):
    print(categoriaIdosa)
  else:
    print('Número inválido.')
    
  '''
  Código para uma opção que fornece todas as categorias unidas

  categorias = []

  for i in range(len(cadastro)):
    if(cadastro[i][1] <= 12):
      print(cadastro[i][1])
      categorias += 'A pessoa chamada ' + cadastro[i][0] + ' é criança.\n'
    elif(cadastro[i][1] <= 19):
      categorias += 'A pessoa chamada ' + cadastro[i][0] + ' é adolescente.\n'
    elif(cadastro[i][1] <= 65):
      categorias += 'A pessoa chamada ' + cadastro[i][0] + ' é adulta.\n'
    else:
      categorias += 'A pessoa chamada ' + cadastro[i][0] + ' é idosa.\n'
  '''

#Função para iniciar o programa
while ativo==True:
  ativo = menu()

