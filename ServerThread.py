# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.3.141.145", 1111))

print("Le nom du fichier que vous voulez récupérer:")
file_name ="logAbhiecg.txt" # utilisez raw_input() pour les anciennes versions python
s.send(file_name.encode())
file_name = '%s' % (file_name,)
r = s.recv(9999999)
with open(file_name,'wb') as _file:
    _file.write(r)
print("Le fichier a été correctement copié dans : %s." % file_name)
