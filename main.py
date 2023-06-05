def cadastro():
  #CADASTRO PARA O APLICATIVO

  ra = []
  senhaApp = []
  pin = []
  n = 0


  qtde_usuarios = int(input("Quantos usuários você quer cadastrar?: "))
  while n < qtde_usuarios:
    cadastroRa = str(input("Qual o seu RA: "))
    cadastroSen = str(input("Qual senha você quer cadastrar para entrar no aplicativo da unimar: "))
    pinDoApp = str(input("Digite o Pin para fazer a chamada: "))
    pin.append(pinDoApp)
    ra.append(cadastroRa)
    senhaApp.append(cadastroSen)
    n+=1

  n=0
  with open('ra.txt','w') as arquivo_alunos:
    alunos = ra[n]
    arquivo_alunos.write(alunos)
    n+=1
    print('Alunos, gravados com sucesso!')

  n = 0
  with open('senhaApp.txt','w') as arquivo_senhas:
    senhas = senhaApp[n]
    arquivo_senhas.write(senhas)
    n+=1
    print('Senhas, gravadas com sucesso!')


def login_pc(qtde_usuarios, ra, pin):
  #LOGIN

  n=0
  with open('pin.txt','w') as arquivo_pinpin:
    pinpin = pin[n]
    arquivo_pinpin.write(pinpin)
    n+=1
    print('Pin gerado com sucesso!')

  #PC
  n = 0
  while n < qtde_usuarios:
    loginRa = str(input("Digite o seu RA: "))
    pinGerado = str(input("Digite o Pin: "))
    if(loginRa == ra[n] and pinGerado == pin[n]):
      print("Login aceito.")
    else:
      print("Login não aceito")
    n+=1

 
def login_app(pin, qtde_usuarios, senhaApp, ra):
  #LOGIN
  
  n=0
  with open('pin.txt','w') as arquivo_pinpin:
    pinpin = pin[n]
    arquivo_pinpin.write(pinpin)
    n+=1
    print('Pin gerado com sucesso!')

  #APP
  n = 0
  while n < qtde_usuarios:
    loginRa = str(input("Digite o seu RA: "))
    senha_app = str(input("Digite a Senha: "))
    if(loginRa == ra[n] and senha_app == senhaApp[n]):
      print("Login aceito.")
    else:
      print("Login não aceito")
    n+=1
    