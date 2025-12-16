from threading import Thread
import time
counter = 0
rounds = 100000
class Counter(Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            #time.sleep(1)
            counter += 1

for i in range(10):
    counter = 0

    t1 = Counter()
    t2 = Counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    if counter != 200000:
        print(f"Iteration {i}: {counter}")
        break
else:
    print("All values are 200000")