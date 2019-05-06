from gensim.models import FastText
import numpy as np


class Fasttext(object):
    def __init__(self, path):
        self.model = FastText.load(path)

    def conver_list(self, phrase):
        if not isinstance(phrase, list):
            return list(phrase)
        return phrase

    def vectorize(self, token_list):
        vector_list = list()
        for token in token_list:
            try:
                vector_list.append(token)
            except KeyError:
                vector_list.append(np.zeros[300] + 1e-7)
        return vector_list

    def __call__(self, phrase):
        phrase = self.conver_list(phrase=phrase)
        return self.vectorize(token_list=phrase)
