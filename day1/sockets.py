__author__ = "Tremor"

import socket

Host = "127.0.0.1"
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))