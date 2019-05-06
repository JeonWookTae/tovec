from tovec.embedding.fasttext import Fasttext
from tovec.analyzer.tokenizer import Tokenizer


class Vector(object):
    def __init__(self, path):
        self.token = Tokenizer()
        self.model = Fasttext(path=path)

    def vectorize(self, phrase):
        phrase = self.token(phrase=phrase)
        return self.model(phrase=phrase)
