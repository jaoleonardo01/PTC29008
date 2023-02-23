import asn1tools

# compila a especificação
spec = asn1tools.compile_files('msg.asn1', codec='der')

# Lê a mensagem codificada
data = open('msg.data','rb').read()

# Decodifica a mensagem
msg = spec.decode('Mensagem', data)

# Mostra a mensagem
print(msg)