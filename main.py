from vocabulary import Vocabulary
import time
import os
import codecs

class Main:

    classes = ["politik", "sport", "wirtschaft"]

    def __init__(self):
        vocabularies = {}

        for c in self.classes:
            print(c)
            strings = self.__access_strings(c)
            vocabulary = Vocabulary(strings)

            curr_vocabulary = vocabulary.get_vocabulary()

            self.__write_vocabulary(c, curr_vocabulary)

            vocabularies[c] = curr_vocabulary

            print(vocabularies[c])

    def __write_vocabulary(self, c, vocabulary):
        filename = c + "_vocabulary" + ".txt"

        # if file does not exist, it will be created
        file = codecs.open(filename, 'w+', "utf-8")

        for item in vocabulary:
            file.write("%s " % item)

    def __access_strings(self, c):
        strings = []

        # concatenate path
        path = "data/" + c + "/train"

        # for each doc in /train
        for f in os.listdir(path):
            if f.endswith(".txt"):
                path_to_file = path + "/" + f
                open_file = codecs.open(path_to_file, "r", "utf-8")

                string = open_file.read()
                strings.append(string)

                open_file.close()

        return strings


start_time = time.time()
Main()
print('--------------------')
print("Execution time is %s seconds" % "%0.2f" % (time.time() - start_time))
