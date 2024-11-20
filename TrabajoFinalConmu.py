import time
import paho.mqtt.client as mqtt
import serial

# Configuración del broker y temas MQTT
broker_address = "192.168.100.54"  # Dirección IP del broker MQTT
Luz = "Luz"  # Tópico para enviar la temperatura
Servo = "Servo"  # Tópico para recibir mensajes relacionados con el LED

# Crear el cliente MQTT
client = mqtt.Client()

# Crear instancia del puerto serial
ser = serial.Serial("/dev/ttyS0", baudrate=9600)

# Función de callback para manejar mensajes recibidos
def on_message(client, userdata, message):
    # Decodificar el mensaje recibido y mostrarlo
    recibido = message.payload.decode()
    print(f"Mensaje recibido en el tópico '{message.topic}': {recibido}")

# Asignar la función de callback al cliente MQTT
client.on_message = on_message

# Función para publicar datos de temperatura y humedad
def publicar():
    while True:
        try:
            data_read = ser.read_until(b'\n').decode().strip()
            if data_read.startswith('L'):  # Verificar si el dato comienza con 'L'
                luz = data_read[1:]
                client.publish(Luz, luz)
                print(f"Publicado: Luz {luz}")
            time.sleep(3)
        except Exception as e:
            print(f"Error al leer o publicar datos: {e}")

# Función para suscribirse a tópicos
def suscribir():
    client.subscribe(Servo)  # Suscribirse al tópico del LED
    print(f"Suscrito al tópico: {Servo}")

# Bloque principal del programa
try:
    # Conectar al broker MQTT
    client.connect(broker_address)
    
    # Iniciar el loop del cliente para manejar mensajes entrantes
    client.loop_start()
    
    # Iniciar suscripción al tópico
    suscribir()
    
    # Iniciar publicación de datos
    publicar()
    
except KeyboardInterrupt:
    print("Programa detenido por el usuario")
finally:
    # Detener el loop del cliente
    client.loop_stop()
    
    # Desconectar del broker MQTT
    client.disconnect()
    print("Cliente MQTT desconectado")
