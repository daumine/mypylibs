# -*- coding:utf8 -*-


def has_sequence(word: str, times: int, by: int):
    assert type(word) is str
    assert times > 0

    if len(word) < times:
        return False

    cnt = 1
    prev = ord(word[0])

    for w in word[1:]:
        cur = ord(w)
        if prev + by == cur:
            if cnt == times-1:
                return True
            cnt += 1
        else:
            cnt = 1

        prev = cur
    else:
        return False