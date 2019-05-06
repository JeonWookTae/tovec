from tovec.vector import Vector
from tovec.analyzer.tokenizer import Tokenizer
import numpy as np

EMBEDDING_PATH = u''
TEST_SENTENCE = '형분을 부탁해!'

vector = Vector(path=EMBEDDING_PATH)
token = Tokenizer()
print(len(token(TEST_SENTENCE)))
print(np.shape(vector.vectorize(TEST_SENTENCE)))