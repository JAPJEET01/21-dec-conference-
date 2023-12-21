import socket
import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('SERVER_IP_ADDRESS', 8888))  # Replace SERVER_IP_ADDRESS with the server's IP

print("Connected to server")

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Streaming...")

while True:
    data = stream.read(CHUNK)
    client_socket.sendall(data)

stream.stop_stream()
stream.close()
p.terminate()
client_socket.close()
