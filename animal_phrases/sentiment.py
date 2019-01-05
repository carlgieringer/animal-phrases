import logging
import re
from collections import defaultdict

_logger = logging.getLogger()
_whitespace_re = re.compile(r'\s+')
_WORD_SENTIMENTS = None


def just_non_negative(words):
    word_sentiments = get_word_sentiments()
    non_negative = []
    misses = []
    for word in words:
        word_sentiment = word_sentiments.get(word, None)
        if word_sentiment is None:
            misses.append(word)
            # Error on the side of inclusiveness
            non_negative.append(word)
        elif word_sentiment.is_positive or not word_sentiment.is_negative:
            non_negative.append(word)
    return non_negative, misses


def get_word_sentiments():
    global _WORD_SENTIMENTS
    if _WORD_SENTIMENTS is None:
        _WORD_SENTIMENTS = _make_word_sentiments()
    return _WORD_SENTIMENTS


def _make_word_sentiments():
    word_sentiments = defaultdict(WordSentiment)
    _process_sentiment_file(word_sentiments, 'data/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt')
    _process_sentiment_file(word_sentiments, 'custom-data/custom-sentiments.txt')
    return word_sentiments


def _process_sentiment_file(word_sentiments, sentiment_file_path):
    with open(sentiment_file_path) as emotions_file:
        for line in emotions_file:
            line_parts = re.split(_whitespace_re, line.strip())
            # The beginning and end line are empty.  Some lines in our custom-sentiments are incomplete
            if len(line_parts) != 3:
                continue
            word, category, label = line_parts
            if category == 'positive':
                word_sentiments[word].is_positive = label == '1'
            elif category == 'negative':
                word_sentiments[word].is_negative = label == '1'

class WordSentiment:
    is_positive = None
    is_negative = None
