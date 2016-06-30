import re
# from collections import Counter

class Vocabulary:

    def __init__(self, strings):
        # print(type(strings))
        # print(strings)

        self.__vocabulary = self.__extract_vocabulary(strings)

        # print("===========")
        # print("vocabulary:")
        # print(Counter(vocabulary))
        #
        # print(vocabulary)


    def __extract_vocabulary(self, strings):
        all_tokens = []

        for s in strings:
            tokens = self.__tokenize(s)
            all_tokens.append(tokens)

        # flatten: list of list => list
        # think of it exactly like nested for loops:
        # for sublist in l: for item in sublist: yield item
        flattened_tokens = [item for sublist in all_tokens for item in sublist]

        # print("----------")
        # print("flattened_tokens:")
        # print(Counter(flattened_tokens))

        return set(flattened_tokens)


    def __tokenize(self, string):
        text = self.__remove_interpunction(string)

        # splits into separate words
        tokens = text.split()

        # if list not empty
        if tokens:
            tokens = self.__normalize_tokens(tokens)

        return tokens

    def __remove_interpunction(self, text):
        # filters out: 0-9 ! ? + - : , ; . ( ) " ' &
        text = re.sub(r'[0-9!?+-:,;\.\(\)\"\'\&]', '', text)

        return text

    def __normalize_tokens(self, tokens):
        tokens = [element.lower() for element in tokens]
        return tokens

    def __vocabularize(self, tokens):
        return set(tokens)

    def get_vocabulary(self):
        return self.__vocabulary