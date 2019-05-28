# Code = 0xAC00 + (Chosung_index * NUM_JOONG * NUM_JONG) + (Joongsung_index * NUM_JONG) + (Jongsung_index)
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


def is_hangul(phrase):  # TODO: need tuning!!
    for letter in phrase:
        code = ord(letter)
        if code < FIRST_HANGUL_UNICODE or code > LAST_HANGUL_UNICODE:
            if not is_jamo(letter):
                return False

    return True


def is_jamo(letter):
    return letter in CHO + JOONG + JONG[1:]


def is_latin1(phrase):
    for unicode_value in map(lambda letter: ord(letter), phrase):
        if unicode_value < FIRST_LATIN1_UNICODE or unicode_value > LAST_LATIN1_UNICODE:
            return False
    return True


def hangul_index(letter):
    return ord(letter) - FIRST_HANGUL_UNICODE


def decompose_index(code):
    jong = int(code % NUM_JONG)
    code /= NUM_JONG
    joong = int(code % NUM_JOONG)
    code /= NUM_JOONG
    cho = int(code)

    return cho, joong, jong


def ch_decompose(hangul_letter):
    if len(hangul_letter) < 1:
        print()
    elif not is_hangul(hangul_letter):
        print()

    if hangul_letter in CHO:
        return hangul_letter, '', ''

    if hangul_letter in JOONG:
        return '', hangul_letter, ''

    if hangul_letter in JONG:
        return '', '', hangul_letter

    code = hangul_index(hangul_letter)
    cho, joong, jong = decompose_index(code)

    if cho < 0:
        cho = 0

    try:
        return "".join((CHO[cho], JOONG[joong], JONG[jong]))
    except:
        print("%d / %d  / %d" % (cho, joong, jong))
        print("%s / %s " % (JOONG[joong].encode("utf8"), JONG[jong].encode('utf8')))
        raise Exception()


def decompose(text, compose_code="_"):
    result = u""

    for c in list(text):
        if is_hangul(c):
            if is_jamo(c):
                result = result + c + compose_code
            else:
                result = result + ch_decompose(c) + compose_code

        else:
            if is_latin1(c):
                result += c
            else:
                result += c

    return result


if __name__ == "__main__":
    a = decompose("하이루루")
    print(a)
