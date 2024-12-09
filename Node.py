from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
import threading
import random
import time

class Node:
    def __init__(self, node_address, initial_time):
        self.node_address = node_address
        self.clock_time = initial_time

    def get_clock_time(self):
        """Retorna o horário do relógio interno"""
        print(f"Nó {self.node_address}: Enviando horário {self.clock_time:.2f}")
        return self.clock_time

# Classe do Nó Cliente
class clientNode(Node):
    def adjust_clock(self, offset):
        """Ajusta o relógio do nó"""
        self.clock_time += offset
        print(f"Nó {self.node_address}: Ajuste aplicado, novo horário {self.clock_time:.2f}")
        return True   
     
# Classe do Nó Servidor
class serverNode(Node):
    def berkeley_synchronize(self, nodes_list):
        client_nodes = [address for address, node_type in nodes_list if node_type != "server"] #Recebe da lista de nós da Rede os seus Ip's
        print("\nIniciando sincronização...")
        if not client_nodes:
            print("Nenhum cliente registrado.")
            return False

        # Solicita horários de todos os nós(servidor e clientes)
        clock_times = [self.get_clock_time()]
        for node in client_nodes:
            with ServerProxy(node) as proxy:
                clock_times.append(proxy.get_clock_time())

        print(f"Relógios recebidos dos clientes: {clock_times}")

        # Calcula o horário médio
        avg_time = sum(clock_times) / len(clock_times)
        print(f"Horário médio calculado: {avg_time:.2f}")

        # Calcula os ajustes e envia para os clientes
        for client, clock_time in zip(client_nodes, clock_times):
            offset = avg_time - clock_time
            with ServerProxy(client) as proxy:
                proxy.adjust_clock(offset)

        print("Sincronização concluída.")
        return True


