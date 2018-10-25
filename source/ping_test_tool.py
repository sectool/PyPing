#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import socket

def ping_test():
	ip_adres = str(raw_input("Ping testi için bir ip adresi giriniz : "))
	ping_adet = str(raw_input("Ping testi için kaç tane ping göndermek istiyorsunuz : "))
	paket_boyutu = str(raw_input("Ping testi için paket boyutunu belirleyiniz : "))
	os.system("ping" + " " + "-c" + ping_adet + " " + "-s" + " " + paket_boyutu + " " + ip_adres)

ping_test_ico = """
#########################################################
#       PYTHON - PING TEST T00L - GH0ST S0FTWARE        #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#########################################################
"""
	
print ping_test_ico	


star = "#########################################################";

print star

ping_test()

print star
