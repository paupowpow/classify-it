from vocabulary import Vocabulary
import time

class Main:

    classes = ["politik", "sport", "wirtschaft"]

    def __init__(self):
        vocab = Vocabulary(self.classes)

start_time = time.time()
Main()
print('--------------------')
print("Execution time is %s seconds" % "%0.2f" % (time.time() - start_time))
