class FileOpen:
    counter = 0  # загальний лічильник відкриттів
    print("FileOpen class")

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        FileOpen.counter += 1
        self.file = open(self.filename, self.mode)
        print(f"[DEBUG log] Opened {self.filename} (Attempt: {FileOpen.counter})")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"[DEBUG log] Closed {self.filename}")
        
        if exc_type:
            print(f"[DEBUG log] {exc_type.__name__}: {exc_val}")
        return False
file = "file.txt"
with FileOpen(file, "w") as f:
    f.write("Hello!")

with FileOpen(file, "a") as f:
    f.write("By!")

with FileOpen(file, "a") as f:
    f.write("By-by!")

with FileOpen(file, "r") as f:
    print(f.read())