import codecs
import collections
import math
import os
import os.path
import time
import re

from vocabulary import Vocabulary

class Main:

    classes = ["politik", "sport", "wirtschaft"]
    concatenated_text_of_all_classes = {}

    def __init__(self):
        train_results = self.__train(self.classes, self.concatenated_text_of_all_classes)
        self.__classify_all_files(self.classes, train_results.prior, train_results.condprob)

    def __train(self, classes, concatenated_text_of_all_classes):
        prior = {}
        condprob = {}

        vocabularies = self.__extract_vocabularies_from_data(classes)
        number_of_all_docs = self.__count_docs(classes)
        concatenated_text_of_all_classes = self.__concatenate(concatenated_text_of_all_classes)
        for c in classes:
            t_ct = {}
            number_of_docs_in_c = self.__count_docs([c])
            prior[c] = number_of_docs_in_c/number_of_all_docs
            for t in vocabularies:
                t_ct[t] = self.__count_tokens_of_term(concatenated_text_of_all_classes[c], t)

            number_of_all_tokens_in_class = len(concatenated_text_of_all_classes[c].split())
            for t in vocabularies:
                if (t in condprob) == False:
                    condprob[t] = {}
                condprob[t][c] = (t_ct[t]+1)/(number_of_all_tokens_in_class + len(vocabularies))
        return self.__return_multiple_values(vocabularies, prior, condprob)

    def __classify_all_files(self, classes, prior, condprob):
        for c in classes:
            path = "data/" + c + '/test'

            # for each doc in /train
            for d in os.listdir(path):
                if d.endswith(".txt"):
                    result = self.__apply_multinomial_nb(d, path, classes, prior, condprob)
                    print(d+': '+ result)

    def __apply_multinomial_nb(self, d, path, classes, prior, condprob):
        score = {}
        tokens = self.__extract_tokens_from_doc(d, path)
        for c in classes:
            score[c] = math.log(prior[c])
            for t in tokens:
                if t in condprob:
                    score[c] += math.log(condprob[t][c])
        return max(score, key=score.get)

    def __extract_tokens_from_doc(self, d, path):
        doc_content = self.__read_doc(path, d)
        doc_content = self.__prettify_string(doc_content)
        tokens = doc_content.split()
        return tokens

    def __extract_vocabularies_from_data(self, classes):
        vocabularies = set()
        for c in classes:
            strings = self.__access_strings(c, '/train')
            vocabulary = Vocabulary(strings)

            curr_vocabulary = vocabulary.get_vocabulary()

            self.__write_vocabulary(c, curr_vocabulary)

            vocabularies |= curr_vocabulary #append set

        return sorted(vocabularies)

    def __write_vocabulary(self, c, vocabulary):
        filename = c + "_vocabulary" + ".txt"

        # if file does not exist, it will be created
        file = codecs.open(filename, 'w+', "utf-8")

        for item in vocabulary:
            file.write("%s " % item)

    # gets all content from all training docs from one class and stores it all into a list of strings.
    def __access_strings(self, c, subfolder):
        strings = []

        # concatenate path
        path = "data/" + c + subfolder

        # for each doc in /train
        for f in os.listdir(path):
            if f.endswith(".txt"):
                string = self.__read_doc(path, f)
                strings.append(string)

        self.concatenated_text_of_all_classes[c] = strings
        return strings

    def __read_doc(self, path, filename):
        path_to_file = path + "/" + filename
        open_file = codecs.open(path_to_file, "r", "utf-8")
        string = open_file.read()
        open_file.close()
        return string

    def __count_docs(self, classes):
        number_of_docs = 0
        for c in classes:
            DIR = 'data/'+c+'/train'
            number_of_docs += len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        return number_of_docs

    def __concatenate(self, concatenated_text_of_all_classes):
        result = {}
        string = ''
        for c in concatenated_text_of_all_classes:
            for doc in concatenated_text_of_all_classes[c]:
                string += self.__prettify_string(doc)
            result[c] = string
            string = ''
        return result

    def __prettify_string(self, string):
        string = re.sub(r'[0-9!?+:,;\.\(\)\"\'\&]', '', string)
        string = re.sub(r'[-]', ' ', string)
        string = re.sub(r'[\n\s]+', ' ', string)
        return string.lower()

    def __count_tokens_of_term(self, text, t):
        return text.count(' '+t+' ')

    def __return_multiple_values(self, vocabularies, prior, condprob):
        results = collections.namedtuple('Results', ['vocabularies', 'prior', 'condprob'])
        results = results(vocabularies, prior, condprob)
        return results

start_time = time.time()
Main()
print('--------------------')
print("Execution time is %s seconds" % "%0.2f" % (time.time() - start_time))
