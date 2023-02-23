#!/usr/bin/python3

import sys, time
import ex2_pb2

m = ex2_pb2.Mensagem()

msg = m.ativo
msg.tipo = 2
msg.id = "PETR4"
msg.valor = 195

data = m.SerializeToString()
print(f"teste {data}")
open('ativo2.data', 'wb').write(data)

msg = m.login
msg.nome = 'teste'
msg.senha = 'testesenha'

data = m.SerializeToString()
open('mensagem2.data','wb').write(data)