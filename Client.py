import socket
import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8888))
server_socket.listen(5)

print("Server listening...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

    data = client_socket.recv(1024)
    while data != b'':
        stream.write(data)
        data = client_socket.recv(1024)

    stream.stop_stream()
    stream.close()
    p.terminate()
    client_socket.close()
  
