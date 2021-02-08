# retirado da decriptografia direta
'''
linhas reservadas para creditos ou possiveis alterações
'''

import math
import sys
import random
import os
from os import system
import getpass

#Somente para checagem do diretório atual
diretorioatual = os.getcwd()
print(diretorioatual)

# ---------------------- FUNÇÕES -------------------- #
def arquivamento(chave_secreta_interna, mensagem_interna):
    chave_arquivada = open(r'C:\Users\eike_\Desktop\Facul\2° Semestre\IPE-Python-2019\APS-Final\criptografiaMessage.txt', 'w', encoding='UTF-8')
    escrita = 'Chave secreta: ' + str(chave_secreta_interna) + '\n' + 'Mensagem criptografada: ' + mensagem_interna
    chave_arquivada.write(str(escrita))
    chave_arquivada.close()


# ---------------------------- TESTE DE DESCRIPTO SOLO ---------------------
def arquivamento2():
    arquivamento_lista_msg = open(r'C:\Users\eike_\Desktop\Facul\2° Semestre\IPE-Python-2019\APS-Final\criptografiaSK.txt', 'w+', encoding='UTF-8')
    arquivamento_lista_msg.close()

    arquivamento_lista_msg = open(r'C:\Users\eike_\Desktop\Facul\2° Semestre\IPE-Python-2019\APS-Final\criptografiaSK.txt', 'a+', encoding='UTF-8')

    for letra_na_lista in msg_criptografada:
        char_da_msg_zerado = str(letra_na_lista) + '.'  
        arquivamento_lista_msg.write(char_da_msg_zerado) 

    arquivamento_lista_msg.close()


def desarquivamento():
    chave_secreta_arquivada = open(r'C:\Users\eike_\Desktop\Facul\2° Semestre\IPE-Python-2019\APS-Final\criptografiaMessage.txt', 'r', encoding='UTF-8')
    linha = chave_secreta_arquivada.readline()
    conteudo_linha = []
    for c in linha:
        
        conteudo_linha.append(c)
    pos_da_chave = str(conteudo_linha[15]) + str(conteudo_linha[16])
    secret_key = int(pos_da_chave)
    chave_secreta_arquivada.close()
    return secret_key


def desarquivamento_direto(): 
    mensagem_inteiro = [] 

    numeros_descriptografados = [] 

    
    mensagem_criptografada = open(r'C:\Users\eike_\Desktop\Facul\2° Semestre\IPE-Python-2019\APS-Final\criptografiaSK.txt', 'r', encoding='UTF-8')
    # -------- LEITURA MENSAGEM ------- # 
    mensagem_lida = mensagem_criptografada.readline()
    mensagem_separada = mensagem_lida.split('.')
    mensagem_separada.remove('') 
    for c in mensagem_separada:
        
        mensagem_inteiro.append(int(c))
        
    

    # -------------- Leitura chave secreta ----------- #
    chave_secreta_arquivada = open(r'C:\Users\eike_\Desktop\Facul\2° Semestre\IPE-Python-2019\APS-Final\criptografiaMessage.txt', 'r', encoding='UTF-8')
    linha = chave_secreta_arquivada.readline()
    conteudo_linha = [] 

    for c in linha:
        conteudo_linha.append(c)

    pos_da_chave = str(conteudo_linha[15]) + str(conteudo_linha[16])
    secret_key = int(pos_da_chave)
    chave_secreta_arquivada.close()

    # ----------- Descriptografia processo final -------------- #
    for numero in mensagem_inteiro:
        num_decript = (numero) ** (1 / secret_key)
        if (num_decript % 2 !=0) and (secret_key != 5) and (secret_key != 10) and (secret_key != 11) and (secret_key != 13): # Colocar and != dos numeros que da erro se pa vai servir tbm
            num_decript2 = math.ceil(num_decript)
            numeros_descriptografados.append(chr(int(num_decript2)))
        else:
            numeros_descriptografados.append(chr(int(num_decript)))

    mensagem_dec_final = ''
    for letra_descripto in numeros_descriptografados:
        mensagem_dec_final = mensagem_dec_final + letra_descripto


    return mensagem_dec_final


def leitura_mensagem():
    leitura_da_criptografada = open(r'C:\Users\eike_\Desktop\Facul\2° Semestre\IPE-Python-2019\APS-Final\criptografiaMessage.txt', 'r', encoding='UTF-8'); # Mudar de acordo com o diretorio do arquivo de texto
    arquivos_das_linhas = leitura_da_criptografada.readlines()
    leitura_da_criptografada.close()
    
    ultima_linha = arquivos_das_linhas [ len (arquivos_das_linhas) -1]
    print()
    print(ultima_linha)


def retorno():
    comando3 = input('''Deseja voltar a tela inicial?
[S]Sim
[N]Não
''').upper()
    if(comando3 == 'S'):
        resposta_retorno = 'ok'
        print()
    elif(comando3 == 'N'):
        resposta_retorno = 'saia' 
    else:
        resposta_retorno = ''
        print('Por favor digite apenas uma das informações fornecidas')

    return resposta_retorno


# ----------------------- LISTAS ------------------
lista_caracter_asc = []
caracteres_msg = []
caracteres_como_numeros = [] # DE ACORDO COM ASCII
msg_criptografada = []
mensagem_descriptografada = []
numeros_descriptografados = [] #Numeros ja feito a raiz Atualização para decript direta


# ---------------------- DICIONARIOS --------------------
cadastros = {
    'funcionario1' : '1010'
}

# -- Preenchimento com valores da tabela ACII --
for c in range(127):
    letras_asc = chr(c)
    lista_caracter_asc.append(letras_asc)

# ---------------------- INICIO DO PROGRAMA PRINCIPAL ----------------------

print('PROGRAMA DE CRIPTOGRAFIA E DESCRIPTOGRAFIA')
print()

inicio = input('''Você deseja iniciar o programa de criptografia?
[S]Sim
[N]Não
''').upper()

chave_publica = '123' # Ainda a definir

if (inicio == 'S'):
    system('cls')
    for c in range(1,4):
        print('LIMITE 3 TENTATIVAS')
        print()
        print('tentativa numero:', c)
        login = input('Digite seu login: ')
        senha = getpass.getpass('Digite sua senha: ')
        if (login in cadastros) and (senha == cadastros[login]):
            system('cls')
            while (True):
                comando1 = input('''Bem vindo ao programa de criptografia e descriptografia, o que deseja fazer?
[C]Criptografia
[D]Descriptografia
[S]Mostrar mensagem criptografada
[E]Sair
''').upper()
                if (comando1 == 'C'):
                    system('cls')
                    print('Lembre-se para criptografar você precisa da nossa chave publica')
                    mensagem = input('Digite a mensagem a ser criptografada: ')
                    chave_publica_digitada = input('Digite a chave publica padrão: ')
                    if (chave_publica == chave_publica_digitada):

                        caracteres_msg.clear() #Adicionados os clears para que não aja sobreposição de outra msg por cima oq pode causar erros
                        caracteres_como_numeros.clear()
                        msg_criptografada.clear()


                        for letras in str(mensagem):
                            caracteres_msg.append(letras)
                            num_dos_caracteres = ord(letras)
                            caracteres_como_numeros.append(num_dos_caracteres)

                        chave_secreta = random.randint(1, 15)
                        print('Sua chave secreta para esta mensagem:', chave_secreta)

                        for pos, letter in enumerate(caracteres_msg):
                            conta = caracteres_como_numeros[pos]
                            msg_cripto = conta ** chave_secreta
                            msg_criptografada.append(msg_cripto)

                        valor_cripto_inicial = '' # Ainda ver se dxo ou não
                        for letra_cripto in msg_criptografada:
                            valor_cripto_inicial = valor_cripto_inicial + str(letra_cripto)
                                
                        print("Sua mensagem criptografada =", valor_cripto_inicial)
                        print()
                        print('SUA MENSAGEM FOI CRIPTOGRAFADA!')
                        arquivamento2()

                        arquivamento(chave_secreta, valor_cripto_inicial)

                        print('Lembre-se forneça sua chave secreta apenas para a pessoa que deseja que leia a mensagem!')
                        print()

                        comando_geral = retorno() # Função de retorno para tela inicial
                        if (comando_geral == 'ok'):
                            system('cls')
                            print()
                        elif (comando_geral == 'saia'):
                            sys.exit()
                        else:
                            system('cls')
                            retorno()
                    else:
                        system('cls')
                        print('CHAVE PUBLICA INCORRETA')
                        print()
                elif (comando1 == 'D'):

                    system('cls')
                    chave_secreta_definida = desarquivamento()
                    mensagem_digitada_criptografada = input('Digite a mensagem a ser descriptografada: ')
                    chave_secreta_digitada = int(getpass.getpass('Digite a chave secreta fornecida para está mensagem: '))

                    if(chave_secreta_digitada == chave_secreta_definida):
                        mensagem_descriptografada.clear() # Zerando a lista

                        for pos1, letter2 in enumerate(msg_criptografada): # Testar se esse pos1 e letter precisa mesmo ou posso tirar um dos dois
                            conta_inversa = msg_criptografada[pos1]

                            msg_decript = (conta_inversa) ** (1/ chave_secreta)

                        print()
                        print('Mensagem descriptografada:',desarquivamento_direto())
                        print()

                        comando_geral = retorno()
                        if (comando_geral == 'ok'):
                            system('cls')
                            print()
                        elif (comando_geral == 'saia'):
                            sys.exit() # Encerramento do programa
                        else:
                            system('cls')
                            retorno()
                    else:
                        system('cls')
                        print('CHAVE SECRETA INCORRETA')
                        print()
                elif (comando1 == 'S'):
                    print()
                    system('cls')
                    leitura_mensagem()
                    comando_geral = retorno()
                    if (comando_geral == 'ok'):
                        system('cls')
                        print()
                    elif (comando_geral == 'saia'):
                        sys.exit() # Encerramento do programa
                    else:
                        system('cls')
                        retorno()
                elif (comando1 == 'E'):
                    print('Obrigado por usar nosso programa')
                    sys.exit()
                else:
                    print('Por favor digite apenas uma das opções fornecidas')
        else:
            system('cls')
            print('SENHA OU LOGIN INCORRETOS')
    #fim for
elif (inicio != 'N') and (inicio != 'S'):
    print('Por favor digite apenas uma das opções fornecidas')
else:
    print()






'''
    - FUNCIONA SOMENTE SE FOR CRIPTOGRAFADA A MENSAGEM NA HRA EM QUE O PROGRAMA É ABERTO
     +Solucionar fazendo com que consiga ler o arquivo
     +Não funciona do mesmo jeito pois temos que armazenar valor na lista a partir da leitura ja feita tbm 
      * ERRO MAIS IMPORTANTE /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\*
      * RESOLVIDO * 

    - ao digitar o valor da chave secreta diferente de numeros ele da erro pois não espera, (AINDA NÃO RESOLVIDO)

    - Ao escolher não deseja voltar a tela inicial temos q manter na tela (NÃO NECESSARIAMENTE) mas esta saindo e voltando mesmo assim, alem de pedir uma opção das deixadas para ele
'''