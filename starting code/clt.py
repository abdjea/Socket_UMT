# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 05:11:15 2019

@author: u21501882
"""

import socket

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print ("Connection on {}".format(port))

socket.send(u"Hey my name is Olivier!")

print ("Close")
socket.close()