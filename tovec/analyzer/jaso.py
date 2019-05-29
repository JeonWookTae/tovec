CHO = (
    u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ',
    u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ'
)

JOONG = (
    u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ',
    u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ'
)

JONG = (
    u'', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ',
    u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ',
    u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ'
)

NUM_CHO, NUM_JOONG, NUM_JONG = len(CHO), len(JOONG), len(JONG)

FIRST_HANGUL_UNICODE = ord("가")
LAST_HANGUL_UNICODE = ord("힣")

FIRST_LATIN1_UNICODE = 0x0000  # NUL
LAST_LATIN1_UNICODE = 0x00FF  # 'ÿ'


class JasoDecompose(type):
    def __call__(cls, text):
        result = u""
        compose_code = ""

        for c in list(text):
            if JasoIs.hangul(c):
                if JasoIs.jamo(c):
                    result = result + c + compose_code
                else:
                    result = result + cls._character_decompose(c) + compose_code

            else:
                if JasoIs.latin1(c):
                    result += c
                else:
                    result += c

        return result

    @staticmethod
    def _character_decompose(hangul_letter):
        _letter_check(hangul_letter)

        if hangul_letter in CHO:
            return hangul_letter, '', ''

        if hangul_letter in JOONG:
            return '', hangul_letter, ''

        if hangul_letter in JONG:
            return '', '', hangul_letter

        code = JasoIndex.hangul(hangul_letter)
        cho = JasoIndex.cho(code)
        joong = JasoIndex.joong(code)
        jong = JasoIndex.jong(code)

        try:
            return "".join((CHO[cho], JOONG[joong], JONG[jong]))
        except IndexError:
            raise IndexError("%s / %s " % (JOONG[joong].encode("utf8"), JONG[jong].encode('utf8')))


class Jaso(metaclass=JasoDecompose):
    @staticmethod
    def __init__(_):
        pass


class JasoIs(object):
    @staticmethod
    def jamo(letter):
        return letter in CHO + JOONG + JONG[1:]

    @staticmethod
    def hangul(phrase):
        for letter in phrase:
            code = ord(letter)
            if code < FIRST_HANGUL_UNICODE or code > LAST_HANGUL_UNICODE:
                if not JasoIs.jamo(letter):
                    return False
        return True

    @staticmethod
    def latin1(phrase):
        for unicode_value in map(lambda letter: ord(letter), phrase):
            if unicode_value < FIRST_LATIN1_UNICODE or unicode_value > LAST_LATIN1_UNICODE:
                return False
        return True


class JasoIndex(object):
    @staticmethod
    def jong(code):
        jong = int(code % NUM_JONG)
        return jong

    @staticmethod
    def joong(code):
        code /= NUM_JONG
        joong = int(code % NUM_JOONG)
        return joong

    @staticmethod
    def cho(code):
        code /= NUM_JONG
        code /= NUM_JOONG
        cho = int(code)
        if cho < 0:
            cho = 0
        return cho

    @staticmethod
    def hangul(letter):
        return ord(letter) - FIRST_HANGUL_UNICODE


def _letter_check(letter: str):
    if len(letter) < 1:
        assert NotImplementedError("string으로 입력해 주세요.")
    elif not JasoIs.hangul(letter):
        assert NotImplementedError("허용 범위를 넘어갔습니다.")


if __name__ == "__main__":
    a = Jaso("하이루루")
    print(a)
