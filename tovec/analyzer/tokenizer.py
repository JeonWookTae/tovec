from konlpy.tag import Mecab


class Tokenizer(object):
    def __init__(self):
        self.mecab = Mecab()

    def __call__(self, phrase):
        return self.mecab.morphs(phrase=phrase)


if __name__ == '__main__':
    token = Tokenizer()
    print(token('지금 몇 시야'))
