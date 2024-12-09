from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import threading
from Node import serverNode, clientNode
from Network import Network

# Classe para manipular requisições XML-RPC
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Inicializa a rede
network = Network()

# Configura o servidor principal
server = serverNode("http://localhost:8000", 10.0)  # O servidor inicia com horário 10.0
network.register_node(server.node_address)

rpc_server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler, allow_none=True, logRequests=True)
rpc_server.register_instance(server)
rpc_server.register_function(server.get_clock_time, "get_clock_time")
rpc_server.register_function(server.berkeley_synchronize, "berkeley_synchronize")

# Função para iniciar os servidores XML-RPC dos clientes em threads separadas
def start_client_server(client, port):
    client_server = SimpleXMLRPCServer(("localhost", port), requestHandler=RequestHandler, allow_none=True, logRequests=True)
    client_server.register_instance(client)
    client_server.register_function(client.get_clock_time, "get_clock_time")
    client_server.register_function(client.adjust_clock, "adjust_clock")
    
    thread = threading.Thread(target=client_server.serve_forever)
    thread.daemon = True
    thread.start()
    return thread

# Criação e registro dos clientes
client1 = clientNode("http://localhost:8001", 12.0)
client2 = clientNode("http://localhost:8002", 9.0)
client3 = clientNode("http://localhost:8003", 8.5)
client4 = clientNode("http://localhost:8004", 7.0)

network.register_node(client1.node_address)
network.register_node(client2.node_address)
network.register_node(client3.node_address)
network.register_node(client4.node_address)

# Inicia os servidores dos clientes
threads = []
threads.append(start_client_server(client1, 8001))
threads.append(start_client_server(client2, 8002))
threads.append(start_client_server(client3, 8003))
threads.append(start_client_server(client4, 8004))

# Inicia o servidor principal em uma thread separada
server_thread = threading.Thread(target=rpc_server.serve_forever)
server_thread.daemon = True
server_thread.start()

# Sincroniza os relógios após os servidores estarem ativos
import time
time.sleep(2)  # Aguarda os servidores iniciarem completamente
server.berkeley_synchronize(network.nodes)

# Mantém o script ativo
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nEncerrando servidores.")
