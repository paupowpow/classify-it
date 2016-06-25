import os
import codecs

class Vocabulary:
    def __init__(self, classes):
        print("Vocabulary()")
        self.__classes = classes
        self.__texts = self.__get_texts(self.__classes)


    def __get_texts(self, classes):
        for c in classes:
            # concatenate path
            path = "data/" + c + "/train"

            # create empty dict for results
            texts = {}
            texts[c] = []

            # for each doc in /train
            for f in os.listdir(path):
                if f.endswith(".txt"):
                    path_to_file = path + "/" + f
                    open_file = codecs.open(path_to_file, "r", "utf-8")

                    string = open_file.read()

                    # get tokens and make set
                    # or just append string to dict
                    texts[c].append(string)
                    open_file.close()

        return texts
