import os
import codecs
import re

class Vocabulary:
    def __init__(self, classes):
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

                    # get tokens and make into set
                    tokens = self.__tokenize(string)
                    vocabulary = self.__vocabularize(tokens)

                    texts[c].append(vocabulary)
                    open_file.close()

        return texts

    def __tokenize(self, string):
        # removes interpunction, in this case "." and ","
        text = self.__remove_interpunction(string)

        # splits into separate words
        tokens = text.split()

        # if list not empty
        if tokens:
            tokens = self.__normalize_tokens(tokens)

        return tokens

    def __remove_interpunction(self, text):
        # filters out: 0-9 ! ? : , . ( ) " ' &
        text = re.sub(r'[0-9!?:,\.\(\)\"\'\&]', '', text)
        text = re.sub(r'[-]', ' ', text)
        return text

    def __normalize_tokens(self, tokens):
        tokens = [element.lower() for element in tokens]
        return tokens

    def __vocabularize(self, tokens):
        return set(tokens)