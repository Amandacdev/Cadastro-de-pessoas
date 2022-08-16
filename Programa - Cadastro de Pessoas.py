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
    visualizarContatoIdade()
  elif(numero == 3):
    categoriaContatoAlf()
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

#Função para exibir lista de contatos - organizada por Idade
def visualizarContatoIdade():
  cadastroIdade = list(cadastro)
  tam = len(cadastroIdade)
  for i in range(tam-1):
    for i in range(tam-1):
      if(cadastroIdade[i][1]>cadastroIdade[i+1][1]):
        aux = cadastroIdade[i]
        cadastroIdade[i] = cadastroIdade[i+1]
        cadastroIdade[i+1] = aux
  print(cadastroIdade)

#Função para exibir lista de contatos - organizada por Ordem Alfabética
def categoriaContatoAlf():
  tam = len(cadastro)
  for i in range(tam-1):
    for i in range(tam-1):
      nome1 = cadastro[i][0]
      nome2 = cadastro[i+1][0]
      letra1 = (nome1[0]).upper()
      letra2 = (nome2[0]).upper()
      if(ord(letra1)>ord(letra2)):
        aux = cadastro[i]
        cadastro[i] = cadastro[i+1]
        cadastro[i+1] = aux
  print(cadastro)

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

