"""
usage:
  clientetftp.py <comando> <arquivo> <ip> <porta>
  clientetftp.py -h

opcoes:
  clientetftp.py rrq|wrq nome_arquivo end_IP porta
  clientetftp.py mkdir|rmdir nome_diretorio end_IP porta


"""

import socket
import sys
import poller
import msg_pb2
from docopt import docopt

argumentos = docopt(__doc__)
conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
conexao.settimeout(2.0)
end_conexao = (argumentos['<ip>'].lower(), int(argumentos['<porta>'].lower()))
arquivo = argumentos['<arquivo>'].lower()
comando = argumentos['<comando>'].lower()

#Conforme RFC, tamanho padrao = 512 bytes de dados + 4 bytes de identificação do bloco
tamanho_bloco_padrao = 516

#Lista de codigos das operacoes e, em seguida, detalhes dos erros
#Fonte: https://www.rfc-editor.org/rfc/rfc1350
codigos = {
    'rrq': 1,  #Solicitacao de leitura de arquivo
    'wrq': 2,  #Solicitacao de escrita de arquivo no servidor
    'dado': 3,  #Dados
    'ack': 4,  #ACK
    'erro': 5}  #Erro

mensagem_erro = {
    0: "Nao definido.",
    1: "Arquivo nao encontrado.",
    2: "Violacao de acesso.",
    3: "Disco cheio ou alocacao excedida.",
    4: "Operacao TFTP ilegal.",
    5: "ID de transferencia desconhecido.",
    6: "Arquivo ja existe.",
    7: "Usuario inexistente."
}

def envia_rrq(arquivo):
    '''
    Fonte: https://www.rfc-editor.org/rfc/rfc1350
          2 bytes    string   1 byte     string   1 byte
          -----------------------------------------------
    RRQ/  | 01/02 |  Filename  |   0  |    Mode    |   0  |
    WRQ    -----------------------------------------------
    '''

    #Protobuf:cria um objeto do tipo Mensagem
    mensagem = msg_pb2.Mensagem()
    #Define valores dos atributos do objeto
    mensagem2 = mensagem.rrq
    mensagem2.fname = arquivo
    mensagem2.mode = 1
    #Codifica o objeto, guardando o resultado numa string
    mensagem3 = mensagem.SerializeToString()
    #Debug
    #print(f"\nMensagem protobuf\n {mensagem} {mensagem3}")
    #Transmite a mensagem no formato protobuf
    conexao.sendto(mensagem3, end_conexao)

def envia_ack(dado_ack,servidor):
    '''
    Fonte: https://www.rfc-editor.org/rfc/rfc1350
    2 bytes     2 bytes
     ---------------------
    | 04 |   Block #  |
     ---------------------
    '''

    #Protobuf:cria um objeto do tipo Mensagem
    mensagem = msg_pb2.Mensagem()
    mensagem_aux = msg_pb2.Mensagem()
    #Leitura
    mensagem.ParseFromString(dado_ack)
    if (mensagem.HasField("data")):
        #debug
        #print(f"\nOK {mensagem.data.block_n}")
        #print("\nENTROU ACK\n")
        #Define valores dos atributos do objeto
        mensagem_aux.ack.block_n = mensagem.data.block_n #mensagem.data.block_n
        # Codifica o objeto, guardando o resultado numa string
        mensagem_aux2 = mensagem_aux.SerializeToString()
        #Debug
        print(f"\nMensagem protobuf ACK \n {mensagem_aux}\n {mensagem_aux2}")
        #Transmite a mensagem no formato protobuf
        conexao.sendto(mensagem_aux2, servidor)
        #retorna carga util
        return mensagem.data.message

def verifica_erro(dados):
    #Separa os bytes de interesse (codigo da operacao)
    #codigo_operacao = dados[:2]
    #Retorna 1 se for um erro
    #Protobuf:cria um objeto do tipo Mensagem
    mensagem = msg_pb2.Mensagem()
    #Leitura
    mensagem.ParseFromString(dados)
    if (mensagem.HasField("error")):
        return mensagem.error.errorcode

def envia_wrq(arquivo):
    # Protobuf:cria um objeto do tipo Mensagem
    mensagem = msg_pb2.Mensagem()
    # Define valores dos atributos do objeto
    mensagem2 = mensagem.wrq
    mensagem2.fname = arquivo
    mensagem2.mode = 1
    # Codifica o objeto, guardando o resultado numa string
    mensagem3 = mensagem.SerializeToString()
    # Debug
    # print(f"\nMensagem protobuf\n {mensagem} {mensagem3}")
    # Transmite a mensagem no formato protobuf
    conexao.sendto(mensagem3,end_conexao)

def envia_dados(arquivo_local,dados_rec,servidor):
    #Faz a leitura do arquivo local (max. 512 bytes)
    byte = arquivo_local.read(512)
    #Protobuf: objetos do tipo Mensagem
    mensagem = msg_pb2.Mensagem()
    mensagem_aux = msg_pb2.Mensagem()
    #Faz a leitura do, em tese, ack ao bloco 0
    mensagem_aux.ParseFromString(dados_rec)
    i = mensagem_aux.ack.block_n
    #Proteção caso o servidor envie um ack fora do padrão
    if (i!=0):
        print(f"Recebido ACK com valor inesperado ({i}). Reenviando WRQ...")
        envia_wrq(arquivo)

    while byte:
        i = i + 1
        #Debug
        #print(f"{byte}")
        #Monta a mensagem data
        mensagem.data.message = byte
        mensagem.data.block_n = i
        mensagem2 = mensagem.SerializeToString()
        #Debug
        #print(f"\nEnviando DATA\n{mensagem}")
        #Envia a mensagem contendo os bytes
        conexao.sendto(mensagem2, servidor)
        byte = arquivo_local.read(512)

        try:
            dados, servidor = conexao.recvfrom(600)
        except socket.timeout:
            print("\nServidor não respondeu a tempo. Finalizando...")
            break
        if verifica_erro(dados):
            print(mensagem_erro[verifica_erro(dados)])
            break

def main():
    #Debug
    #print(comando + ' ' + arquivo + ' ')
    #print(end_conexao)

    #Por padrao, modo ascii
    modo = "netascii"

    #envia a requisicao de leitura de arquivo
    if comando == 'rrq':
        #Variavel para que arquivo local seja sobrescrito
        aux = 0
        envia_rrq(arquivo)
        #Abrir arquivo localmente com o mesmo nome do arquivo solicitado
        #arquivo_local = open(arquivo, "wb")
        while (1):
            #Armazenar dados e endereço rec. pelo socket 'conexao'
            try:
                dados, servidor = conexao.recvfrom(600)
                print(f"{dados}")
            except socket.timeout:
                print("\nServidor não respondeu a tempo. Finalizando...")
                break
            #Debug
            #print(f"SERVIDOR {servidor}")
            #Tratar possiveis erros
            if verifica_erro(dados):
                print(mensagem_erro[verifica_erro(dados)])
                break
            #Caso seja primeira iteracao, sobrescreve
            if(aux == 0):
                arquivo_local = open(arquivo, "wb")
                #Debug
                #print("\nsobrescrevi\n")
            #Caso nao seja primeira iteracao, escreve no final
            else:
                arquivo_local = open(arquivo, "ab")
                #Debug
                #print("\nappend\n")
            aux = aux + 1
            #caso nao seja msg. de erro, envia ack de acordo com RFC e...
            #... armazena a carga util
            print("Chamar envia_ACK\n")
            carga_util = envia_ack(dados,servidor)
            #Escreve no arquivo local o conteudo util da mensagem
            arquivo_local.write(carga_util)
            #Debug
            #print(f"dados uteis: {dados} \n")
            #Verifica se eh fim de arquivo, conforme RFC
            if len(dados) < tamanho_bloco_padrao:
                print("\nFinalizando...\n")
                break

    elif comando == 'wrq':
        try:
            arquivo_local = open(arquivo, "rb")
        # stuff goes here
        except IOError:
            print("Arquivo inacessível localmente! Encerrando...")
            exit()
        #Debug
        envia_wrq(arquivo)
        #Armazenar dados e endereço rec. pelo socket 'conexao'
        try:
            dados_rec, servidor = conexao.recvfrom(600)
        except socket.timeout:
            print("\nServidor não respondeu a tempo. Finalizando...")
            exit()
        if verifica_erro(dados_rec):
            print(mensagem_erro[verifica_erro(dados_rec)])
            exit()
        envia_dados(arquivo_local,dados_rec,servidor)

    else:
        print("Comando inválido!\nExecute clientetftp -h")

if __name__ == '__main__':
    main()
