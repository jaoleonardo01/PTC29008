import asn1tools

# compila a especificação
spec = asn1tools.compile_files('msg.asn1', codec='der')

# cria uma mensagem na forma de um dicionário !
msg = {'tipo': 1, 'valor': 100, 'id': 'MSG1'}


# Codifica a mensagem
data = spec.encode('Mensagem', msg)

# Mostra a mensagem codificada
print(data)

# Grava a mensagem em um arquivo
open('msg.data','wb').write(data)
