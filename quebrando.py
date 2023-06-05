from dataclasses import dataclass

#Cadastro
def ler_quantidade_alunos():
    return int(input("Quantos usuários você quer cadastrar?: "))

def ler_ra():
    return str(input("Qual o seu RA: "))

def ler_senha():
    return str(input("Qual senha você quer cadastrar para entrar no aplicativo da unimar: "))

def ler_pin():
    return str(input("Digite o Pin para fazer a chamada: "))

@dataclass
class Aluno:
    ra: str
    senha: str
    pin: str


def ler_aluno(senha = True):
    aluno = Aluno(
        ra=ler_ra(),
        senha=ler_senha() if senha else None,
        pin=ler_pin()
    )
    return aluno



#PC DESKTOP
def login_ra():
    return str(input("Digite o seu RA: "))

def gerar_pin():
    return str(input("Digite o Pin: "))


#Login APP
def login_App_ra():
    return str(input("Digite o seu RA: "))

def login_App_senha():
    return str(input("Digite a Senha: "))
