import os

class Main:

    train_paths = ["data/politik/train", "data/sport/train", "data/wirtschaft/train"]

    vocabularies = []

    for path in train_paths:
        print(path)
        # for each doc in /train
            # get words and make set

        for f in os.listdir(path):
            if f.endswith(".txt"):
                path_to_file = path + "/" + f

                open_file = open(path_to_file)
                string = open_file.read(30)
                print(path_to_file + ": " + string)
                open_file.close()
