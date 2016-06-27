import codecs
import os
import os.path
import time

from vocabulary import Vocabulary


class Main:

    classes = ["politik", "sport", "wirtschaft"]

    def __init__(self):
        self.__train(self.classes)

    def __train(self, classes):
        vocabularies = self.__extract_vocabularies_from_data(classes)
        number_of_all_docs = self.__count_docs(classes)
        prior = {}
        for c in classes:
            number_of_docs_in_c = self.__count_docs([c])
            prior[c] = number_of_docs_in_c/number_of_all_docs
            text_c = self.__concatenate_text_of_all_docs_in_class()

    def __extract_vocabularies_from_data(self, classes):
        vocabularies = {}
        for c in classes:
            print(c)
            strings = self.__access_strings(c)
            vocabulary = Vocabulary(strings)

            curr_vocabulary = vocabulary.get_vocabulary()

            self.__write_vocabulary(c, curr_vocabulary)

            vocabularies[c] = curr_vocabulary

            print(vocabularies[c])
        return vocabularies

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

    def __count_docs(self, classes):
        number_of_docs = 0
        for c in classes:
            DIR = 'data/'+c+'/train'
            number_of_docs += len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        return number_of_docs

    def __concatenate_text_of_all_docs_in_class(self):
        return 0

start_time = time.time()
Main()
print('--------------------')
print("Execution time is %s seconds" % "%0.2f" % (time.time() - start_time))
