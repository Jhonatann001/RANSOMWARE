import os
import pyaes

# Solicitar o nome do arquivo criptografado
file_name = input("Arquivo a descriptografar: ")

if not os.path.exists(file_name):
    print("Arquivo não encontrado!")
    exit()

# Ler o arquivo criptografado
with open(file_name, "rb") as file:
    file_data = file.read()

# Remover o arquivo criptografado
os.remove(file_name)

# Chave de 16 bytes (deve ser a mesma usada para criptografar)
key = b"0ase9D3R1aV2eh3N"
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar os dados
decrypted_data = aes.decrypt(file_data)

# Salvar o arquivo recuperado
new_file_name = "resgatado.png"
with open(new_file_name, "wb") as new_file:
    new_file.write(decrypted_data)

print("Arquivo descriptografado e salvo como", new_file_name)
