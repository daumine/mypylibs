from mylib import has_sequence


def check_sequence(word):
    print('{} same chars: {}'.format(word, has_sequence(word, 3, 0)))
    print('{} ascending: {}'.format(word, has_sequence(word, 3, 1)))
    print('{} descending: {}'.format(word, has_sequence(word, 3, -1)))


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    check_sequence('aaa')
    check_sequence('abc')
    check_sequence('cba')
    check_sequence('zyx')
    check_sequence('111')
    check_sequence('123')
    check_sequence('12234')
    check_sequence('321')
    check_sequence('332')
    check_sequence('3321')