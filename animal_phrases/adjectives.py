import itertools

import nltk

_BROWN_ADJECTIVES = None


def get_brown_adjectives():
    global _BROWN_ADJECTIVES
    if _BROWN_ADJECTIVES is None:
        _BROWN_ADJECTIVES = _make_brown_adjectives()
    return _BROWN_ADJECTIVES


def _make_brown_adjectives(limit=None):
    word_pos_tuples = nltk.corpus.brown.tagged_words(tagset='universal')
    adjectives = (t[0] for t in word_pos_tuples if t[1] == 'ADJ')
    if limit is not None:
        adjectives = itertools.islice(adjectives, limit)
    return set(adjectives)


def just_adjectives(words):
    return [w for w in words if w in get_brown_adjectives()]


if __name__ == '__main__':
    print(_make_brown_adjectives(1000))
