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

                    # get tokens and make set
                    tokens = self.__tokenize(string)

                    # or just append string to dict
                    texts[c].append(tokens)
                    open_file.close()

        return texts

    def __tokenize(self, string):
        # removes interpunction, in this case "." and ","
        text = self.__remove_interpunction(string)

        # splits into separate words
        token_list = text.split()

        # if list not empty
        if token_list:
            token_list = self.__normalize_tokens(token_list)

        print(token_list)

        return token_list

    def __remove_interpunction(self, text):
        text = re.sub(r'[?:,\.]', '', text)
        text = re.sub(r'[-]', ' ', text)
        return text

    def __normalize_tokens(self, token_list):
        token_list = [element.lower() for element in token_list]
        return token_list