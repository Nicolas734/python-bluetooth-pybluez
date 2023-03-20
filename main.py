import bluetooth
import logging


logging.basicConfig(filename="app.log", level=logging.ERROR)

print('\nLista de dispositivos\n')
devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)



for addr, name, device_class in devices:
    print("Dispositivo:")
    print("Nome do Dispositivo: %s" % (name))
    print("Endereço MAC do Dispositivo: %s" % (addr))
    print("Classe do Dispositivo: %s" % (device_class))
    print("\n")

    services = bluetooth.find_service(address=addr)
    if len(services) > 0:
        print(f"Serviços disponíveis do dispositivo {name}:")
        for svc in services:
            print(f"\tNome do Serviço: {svc['name']}")
            print(f"\t    Host: {svc['host']}")
            print(f"\t    Description: {svc['description']}")
            print(f"\t    Provided by: {svc['provider']}")
            print(f"\t    Protocol: {svc['protocol']}")
            print(f"\t    Service classes: {svc['service-classes']}")
            print(f"\t    Profiles: {svc['profiles']}\n")



while True:

    print("\nQual o endereço MAC que deseja conectar ?")
    addr = str(input(': '))
    port = 3

    if bluetooth.is_valid_address(addr):
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.settimeout(15.0)

        print("\nTentando se conectar ao dispositivo...\n")

        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((addr, port))
            conexao = sock.getpeername()
            print("Conexão estabelecida com sucesso!\n")
            print(conexao)
            response = sock.send("Hello World")
            print(response)
            sock.close()
            break

        except Exception as error:
            print(f"Não foi possivel se conectar ao dispositivo {addr}")
            logging.exception(str(error))
            print("n\Erro armazenado no arquivo de log....\n")
            break

    else: 
        print(f"Endereço mac {addr} não é valido")


# O PyBluez suporta os seguintes protocolos Bluetooth:

# 1. RFCOMM: é um protocolo de comunicação por porta serial emulação que fornece um canal de comunicação simples e confiável entre dois dispositivos Bluetooth. Ele é geralmente usado para transmitir dados seriais, como dados de GPS ou sensores, entre dispositivos.

# 2. L2CAP: é um protocolo de camada de enlace de comunicação de ponto a ponto que permite que os dispositivos Bluetooth se comuniquem com outros dispositivos Bluetooth. É usado para transferir grandes quantidades de dados em um único pacote, como transmissões de áudio ou vídeo.

# 3. OBEX: é um protocolo de transferência de objeto que permite que dois dispositivos Bluetooth transfiram arquivos e objetos uns para os outros. É usado para transferir fotos, músicas, contatos e outros dados de um dispositivo para outro.

# 4. SDP: é um protocolo de descoberta de serviços que permite que dispositivos Bluetooth descubram quais serviços estão disponíveis em outros dispositivos Bluetooth. Ele é usado para encontrar dispositivos específicos e determinar quais serviços eles oferecem.

# Além desses protocolos, o PyBluez também suporta o uso de perfis Bluetooth específicos, como o perfil Hands-Free Profile (HFP) ou o perfil Advanced Audio Distribution Profile (A2DP).
