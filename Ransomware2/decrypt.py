import os 
import pyaes

file_name = "foto.png.encripted"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

chave = "0ase9D3R1aV2eh3NJsk92h331hsa"
aes = pyaes.AESModeOfOperationCTR(chave)
decripta_dados = aes.decrypt(file_data)

new_file_name = "resgatado.png"
new_file = open(new_file_name, "wb")
new_file_data = new_file.write(decripta_dados)
new_file.close()