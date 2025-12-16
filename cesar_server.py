import socket

def cesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server is running...")
    
    conn, addr = s.accept()
    with conn:
        print("Connected:", addr)
        data = conn.recv(1024).decode()
        lines = data.split("\n")
        key = int(lines[0])
        text = lines[1]

        encrypted = cesar_cipher(text, key)

        conn.sendall(encrypted.encode())
        print("Encrypted message sent.")        

if __name__ == "__main__":
    import unittest

    class TestCaesarCipher(unittest.TestCase):
        def test_lowercase(self):
            self.assertEqual(cesar_cipher("abc", 1), "bcd")
        
        def test_uppercase(self):
            self.assertEqual(cesar_cipher("XYZ", 2), "ZAB")
        
        def test_mixed(self):
            self.assertEqual(cesar_cipher("Hello, World!", 3), "Khoor, Zruog!")
        
        def test_negative_shift(self):
            self.assertEqual(cesar_cipher("bcd", -1), "abc")

    unittest.main(exit=False)