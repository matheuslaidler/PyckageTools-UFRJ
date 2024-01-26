import socket
import time
#import request

#import requests -> precisa instalar, como a gnt tinha no linux "sudo pip install requests" ou "py -m pip install requests" no cmd no windows
#ent infelizmente tlvz n seja aceito ent n da p usar aq pro trab, logo o brute force de diretório n pode entrar no projeto tb
#consequentemente n dará pra fzr brute force de login tbm



'''
Sockets são usados para enviar dados através da rede, um exemplo seria enviar um arquivo pelo Discord / Skype / Whats App, ou ainda podemos considerar até mesmo as próprias mensagens.'''
'''
Explicação do scan de portas
#!/usr/bin/python
Agora vamos importar a biblioteca socket que possui diversas configurações para conexões em redes, e que permite o acesso aos serviços da camada de transporte, como por exemplo os protocolos TCP e UDP
Salvamos o valor de entrada do nosso usuário em uma variável chamada ip
Salvamos o valor de entrada do nosso usuário em uma variável chamada port
Vamos atribuir a uma variável chamada s nossas opções de conexão e transferência de dados através do socket. Sockets usam endereços para fazer referências entre si, esses endereços são denominados domínios, AF_INET diz que vamos nos conectar a um domínio composto de um endereço de ip e uma porta (Ex: http://www.google.com na porta 80). SOCK_STREAM é a forma como os dados serão transferidos, e nesse caso, será através de uma stream de caracteres.
Utilizaremos a instrução if para verificar se nossa conexão foi bem sucedida. Entre parênteses, estamos passando como parâmetro para nossa função as variáveis ip e port, que serão os valores usados para estabelecer a conexão. Quando uma conexão falha, a função connect_ex retorna um código de erro, ao invés de uma exceção como a função connect. Se nossa conexão for bem sucedida o retorno será 0, e se falhar o retorno será 1.
Perceba que nós estamos recebendo uma resposta do tipo boolean, 0 ou 1, falso ou verdadeiro. De forma simplificada, é como se perguntássemos: A conexão falhou?

0 – Falso = Não, a conexão não falhou
1 – Verdadeiro = Sim, a conexão falhou

Por fim, caso nossa resposta seja 1, iremos imprimir que a porta esta fechada. E do contrário, o bloco de instrução else irá imprimir que a porta está aberta.

Se no lugar da função connect_ex colocarmos a função connect, quando a porta estiver fechada nossa saída no terminal sera assim:
socket.error:[ERRNO 111]Connection refused
'''

#IMPORTANTE -> socket.socket(socket.AF_INET, socket.SOCK_STREAM) #conexão e transf de dados
#como vamos setar uma variavel com esse valor em várias funções diferentes, seria melhor criar uma para todas elas?:
#conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #conexão e transf de dados com certo IP como stream de caracteres
#em condições normais sim, mas de qlqr maneira temos que add a variavel dnv pra ela funcionar corretamente, principalmente para fazer a conexão dnv nos loops;
#Ent deixei dentro das funções mesmo.

def host():
    ''' Função pra pegar o IP de qualquer site especificado'''
    site = input("Scanear IP de: ")
    ip = socket.gethostbyname(site)
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('O IP de',site,'é','**',ip,'**')
    time.sleep(1)
    print("                         ")
    print('Voltando ao menu...')
    time.sleep(2)
    home()
    
def scanPortas():
    ''' Função que scaneia qual das principais portas estão abertas'''
    ip = input("Qual ip: ")
    print("Espere até fazer todo o scan.")
    print("Isso pode levar uns minutos...")
    portas = [80,443,21,22,53,8080,3306,3389]
    for i in range(len(portas)):
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if conexao.connect_ex((ip,portas[i])) == 0:
            print("Porta",portas[i]," ** ABERTA! **")
        else:
            print("Porta",portas[i]," *  FECHADA  *")
    time.sleep(1)
    print("                         ")
    print('Voltando ao menu...')
    time.sleep(2)
    home()

def deepScanPortas():
    ''' Função que scaneia qual de todas as 65534 portas estão abertas'''
    ip = input("Qual ip: ")
    print("Espere até fazer todo o scan.")
    print("Isso pode levar um tempo...")
    ports = list(range(1,65535)) #de 1 a 65534 q são todas as portas (demora mt)
    for i in range(len(ports)):
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if conexao.connect_ex((ip,ports[i])) == 0:
            print("Porta",ports[i],"** ABERTA! **")
        else:
            print("Porta",ports[i],"*  FECHADA  *")
    time.sleep(1)
    print("                         ")
    print('Voltando ao menu...')
    time.sleep(2)
    home()


def bruteforceFTP():
    ''' Função que faz o ataque de força bruta num servidor FTP dado para quebrar a senha'''
    ftp = input('Qual o IP do server? ')
    usuario = input('Qual o usuário do login? ')
    lista = ['admin','123','adm123','asdf','Admin123@'] #senhas pro brute force ()podendo ser uma wordlist em arquivo, tendo q usar o open() -> file = open(wordlist.txt)
    for linha in range(len(lista)):
        prin("Testando> ",usuario,'::',lista[linha])
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao.connect((ftp,21)) #porta padrão 21
        conexao.send("Usuário: "+usuario+"\r\n")
        conexao.recv(1024)
        conexao.send("Senha: "+lista[linha]+"\r\n")
        resulta = conexao;recv(1024)
        conexao.send("Fim\r\n")
        if re.search("230",resulta):
            print("*SENHA ENCONTRADA!!* A senha é:",lista[linha])
            break
        else:
            print("Falha no acesso...\n")

#tirada funções que usam do request

"""
def bruteforceDir():
    ''' Função que faz um brute force no site indicado para saber
    se possui certos diretórios ou se o arquivo robots.txt existe,
    para saber quais diretórios não podem ser vistos por mecanismo
    de busca.'''
    site = input("qual site quer testar diretórios? (Colocar / no final) ")
    lista = ["home","adm","admin","login","register","robot.txt"]
    for i in range(len(lista)):
        site = site + lista[i]
        test = requests.get(site)
        status = site.status_code()
        if (status == 200):
            print("Página EXISTE")
        else:
            print("Página INXISTENTE ou INACESSÍVEL")
    time.sleep(1)
    print("                         ")
    print('Voltando ao menu...')
    time.sleep(2)
    home()


	

def banner():
    ''' Função de reconhecimento de informações trazendo o banner do serviço ftp'''
    ip = input("IP do serviço: ")
    porta = int(input("Porta: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,porta))
    banner = s.recv(1024)
    print(banner)
    time.sleep(1)
    print("                         ")
    print('Voltando ao menu...')
    time.sleep(2)
    home()
"""



def home():
    '''Função padrão: Menu do programa
'''
    print("=========================")
    print("                         ")
    print("-------------------------")
    print("pyScript de Matheus L V C")
    print("-------------------------")
    print("                         ")
    print("=========================")
    print("          MENU           ")
    print("=========================")
    print("                         ")
    print("-------------------------")
    print("                         ")
    print(" (a) DNS Resolver        ")
    print(" (b) Scan de portas      ")
    print(" (c) Descobrindo páginas ")
    print(" (d) Brute Force FTP     ")
    print("                         ")
    print("-------------------------")
    resp = input("> ")
    print("-------------------------")
    if resp == 'a':
        host()
    if resp == 'b':
        print("1- Scan de portas padrão?")
        print("2- Scan de 65534 portas? ")
        print("-------------------------")
        s = int(input(">"))
        if s == 1:
            scanPortas()
        elif s == 2:
            deepScanPortas()
        else:
            return "error"
            home()
    if resp == 'c':
        print('Brute Force de diretórios')
        print("-------------------------")
        bruteforceDir()
    if resp == 'd':
        print('Brute Force de Server FTP')
        print("-------------------------")
        bruteforceFTP()

home()
