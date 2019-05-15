from gensim.models import FastText
import numpy as np


class Fasttext(object):
    def __init__(self, path):
        self.model = FastText.load(path)
        self.size = 300

    def conver_list(self, phrase):
        if not isinstance(phrase, list):
            return list(phrase)
        return phrase

    def vectorize(self, token_list):
        vector_list = list()
        for token in token_list:
            try:
                vector_list.append(self.model[token])
            except KeyError:
                vector_list.append(np.zeros(self.size) + 1e-7)
        return vector_list

    @classmethod
    def trainer(cls, corpus, size):
        """
        :param corpus: [sentence: [word, word, . . ., word], . . ., sentence]
        :return:
        """
        train_instance = FastText(sentences=corpus, size=size, window=5, min_count=1)
        cls.model = train_instance

    def updater(self, corpus):
        if self.model:
            self.model.build_vocab(corpus, update=True)
            self.model.train(corpus, total_examples=len(corpus), epochs=10)

    def __call__(self, phrase):
        phrase = self.conver_list(phrase=phrase)
        return self.vectorize(token_list=phrase)

