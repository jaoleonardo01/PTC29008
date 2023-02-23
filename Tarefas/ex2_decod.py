#!/usr/bin/python3

import sys, time
import ex2_pb2

tipos = ('ativo','login')

m = ex2_pb2.Mensagem()

m.ParseFromString(open(sys.argv[1],'rb').read())

for tipo in tipos:
    if m.WhichOneof('msg') == tipo:
        print(f'Mensagem contem {tipo}:\n')
        print(m)
        break