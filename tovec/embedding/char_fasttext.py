from gensim.models import FastText
import numpy as np


class CharFasttext(object):
    def __init__(self, path):
        self.model = FastText.load(path)
        self.size = 300

    def convert_list(self, phrase):
        if not isinstance(phrase, list):
            return list(phrase)
        return phrase

    def vectorize(self, token_list):
        """
        :param token_list: [word:[ch, ch, . . .,ch],. . .word]
        :return:
        """
        vector_list = list()
        for token in token_list:
            ch_list = list()
            for ch in token:
                ch_list.append(self.model[ch])
            vector_list.append(np.sum(ch_list, axis=1))
        return vector_list

    def trainer(self, corpus):
        """
        :param corpus: [sentence: [ch, ch, . . ., ch]]
        :return:
        """
        train_instance = FastText(sentences=corpus, size=self.size, window=8, min_count=1)
        self.model = train_instance

    def updater(self, corpus):
        if self.model:
            self.model.build_vocab(corpus, update=True)
            self.model.train(corpus, total_examples=len(corpus), epochs=10)

    def __call__(self, phrase):
        phrase = self.convert_list(phrase=phrase)
        return self.vectorize(token_list=phrase)

