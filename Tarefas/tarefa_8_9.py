#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:24:35 2018

@author: msobral
"""

import socket
import poller
import sys

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
end_conexao = (sys.argv[1], int(sys.argv[2]))

class CallbackStdin(poller.Callback):

    def __init__(self, cb):
        poller.Callback.__init__(self, sys.stdin, 0)
        self.disable_timeout()
        self.cb = cb

    def handle(self):
        l = sys.stdin.readline()
        #print('\n' + l + '1' + '\n')
        conexao.sendto(l.encode(), end_conexao)
        #print('\n' + l + '2' + '\n')
        self.cb.envia(l.encode())
        #print('\n' + l + '3' + '\n')

class CallbackCoisa(poller.Callback):

    def __init__(self, tout):
        poller.Callback.__init__(self, None, tout)
        self.disable_timeout()

    def envia(self, dado):
        dado2, servidor = conexao.recvfrom(600)
        print('Dado:', dado2.decode())
        self.enable_timeout()
        self.reload_timeout()

    def handle_timeout(self):
        print('Timeout !')
        self.disable_timeout()


obj = CallbackCoisa(3)
cb = CallbackStdin(obj)

sched = poller.Poller()
sched.adiciona(cb)
sched.adiciona(obj)

sched.despache()
