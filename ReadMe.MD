### 🕒 O Algoritmo de Berkeley

O algoritmo de Berkeley é um método usado para sincronizar os relógios de todos os nós em uma rede. Ele funciona ajustando os relógios dos clientes e do servidor para um horário médio. O processo é simples:

1. **Servidor como Coordenador:**  
   O servidor assume o papel de coordenador e solicita os horários de todos os nós (inclusive o próprio).

2. **Cálculo do Horário Médio:**  
   O servidor calcula o horário médio com base nos relógios recebidos.

3. **Ajuste dos Relógios:**  
   O servidor calcula a diferença entre o horário médio e os horários individuais (offset) e envia os ajustes para os clientes.

4. **Sincronização:**  
   Cada nó aplica o ajuste para sincronizar seu relógio com o horário médio.

Este projeto implementa uma simulação do algoritmo de sincronização de relógios **Berkeley** utilizando o protocolo XML-RPC. O sistema é composto por um servidor e múltiplos clientes que sincronizam seus relógios internos com base no horário médio.

## 🛠️ Estrutura do Projeto

- **Network**: Gerencia a rede e registra os nós (servidor e clientes).
- **Node**: Classe base para representar os nós, com implementações específicas para:
  - **serverNode**: Implementa a lógica do servidor, incluindo o algoritmo de Berkeley.
  - **clientNode**: Representa os clientes e ajusta os relógios conforme os offsets recebidos.
- **run**: Arquivo responsável pela inicialização dos servidores e clientes utilizando o protocolo XML-RPC.

## 🚀 Funcionalidades

- Registro automático de nós como servidor ou cliente.
- Sincronização de relógios utilizando o algoritmo de Berkeley:
  - O servidor calcula o horário médio com base nos relógios dos nós.
  - Envia ajustes de offset para os clientes.
- Servidores (tanto principal quanto clientes) rodando em threads separadas.

## 🖥️ Execução

### Pré-requisitos

- Python 3.6 ou superior
- Bibliotecas padrão: `xmlrpc.server`, `xmlrpc.client`, `threading`

### Passos para executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio```
