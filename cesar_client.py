import socket

HOST = "127.0.0.1"
PORT = 65432

def send_message(key, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f"{key}\n{message}".encode())
        data = s.recv(1024)
        print("Encrypted:", data.decode())
    return data.decode()


if __name__ == "__main__":
    import unittest

    class TestClientServer(unittest.TestCase):
        def test_encryption(self):
            # Перед запуском цього тесту сервер повинен бути запущений!
            encrypted = send_message(3, "Hello World")
            self.assertEqual(encrypted, "Khoor Zruog")  # очікуваний результат шифру
            encrypted = send_message(2, "Hello World")
            self.assertEqual(encrypted, "Jgnnq Yqtnf")  # очікуваний результат шифру            

    unittest.main(exit=False)
