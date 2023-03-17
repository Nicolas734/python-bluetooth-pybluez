import bluetooth
import logging




logging.basicConfig(filename="app.log", level=logging.ERROR)


print('Listagem de dispositivos\n')
devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
for addr, name, device_class in devices:
    print("Device:")
    print("Device Name: %s" % (name))
    print("Device MAC Address: %s" % (addr))
    print("Device Class: %s" % (device_class))
    print("\n")

addr = "COLOQUE SEU MAC ADRESS AQUI"
port = 1

print("\nTentando se conectar ao dispositiVo...")

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
try:
    sock.connect((addr, port))
    message = "Olá, mundo!"
    sock.send(message)
    print("\nConexão bem sucedida...\n")
    sock.close()
except Exception as error:
    print("\nNão foi possivel se comunicar com dispositivo...")
    logging.exception(str(error))





# O PyBluez suporta os seguintes protocolos Bluetooth:

# 1. RFCOMM: é um protocolo de comunicação por porta serial emulação que fornece um canal de comunicação simples e confiável entre dois dispositivos Bluetooth. Ele é geralmente usado para transmitir dados seriais, como dados de GPS ou sensores, entre dispositivos.

# 2. L2CAP: é um protocolo de camada de enlace de comunicação de ponto a ponto que permite que os dispositivos Bluetooth se comuniquem com outros dispositivos Bluetooth. É usado para transferir grandes quantidades de dados em um único pacote, como transmissões de áudio ou vídeo.

# 3. OBEX: é um protocolo de transferência de objeto que permite que dois dispositivos Bluetooth transfiram arquivos e objetos uns para os outros. É usado para transferir fotos, músicas, contatos e outros dados de um dispositivo para outro.

# 4. SDP: é um protocolo de descoberta de serviços que permite que dispositivos Bluetooth descubram quais serviços estão disponíveis em outros dispositivos Bluetooth. Ele é usado para encontrar dispositivos específicos e determinar quais serviços eles oferecem.

# Além desses protocolos, o PyBluez também suporta o uso de perfis Bluetooth específicos, como o perfil Hands-Free Profile (HFP) ou o perfil Advanced Audio Distribution Profile (A2DP).
