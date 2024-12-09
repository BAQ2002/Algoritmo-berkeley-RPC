from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
import threading
import time
from Node import clientNode, serverNode

# Classe da rede onde
class Network:
    def __init__(self):
        self.nodes = []
        

    #Registra os nós na rede
    def register_node(self, node_address):
        """Registra um cliente na lista"""
        if node_address not in [node[0] for node in self.nodes]:
            if all("server" != node[1] for node in self.nodes): #Verifica se ja existe um nó servidor
                self.nodes.append((node_address, "server"))
                print(f"Servidor registrado: {node_address}")
            else:
                self.nodes.append((node_address, "client")) 
                print(f"Cliente registrado: {node_address}")          
        return True

