import argparse
import logging
import pprint

from animal_phrases.animals import get_animals
from animal_phrases.adjectives import just_adjectives
from animal_phrases.literary_devices import get_alliterations, get_rhymes
from animal_phrases.sentiment import just_non_negative

_logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


def main():
    args = parse_args()
    animal_phrases, no_phrase_animals = get_animal_phrases(do_exclude_rhymes=args.no_rhymes,
                                                           do_include_alliterations=args.alliterations,
                                                           alliteration_phone_count=args.alliteration_phone_count,
                                                           only_nonnegative=args.no_negative)
    _logger.debug(f'{len(animal_phrases)} animal phrases!')
    for phrase in animal_phrases:
        print(phrase)
    _logger.debug(f'phraseless animals: {no_phrase_animals}')


def parse_args():
    parser = argparse.ArgumentParser(description='Finds rhyming and alliterative animal phrases',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--show-phraseless', action='store_true', help='output the animals that had no phrases')
    parser.add_argument('--no-rhymes', action='store_true', help='exclude rhymes')
    parser.add_argument('--alliterations', action='store_true', help='include alliterations')
    parser.add_argument('--alliteration-phone-count', type=int, default=2,
                        help='number of common initial phones to be an alliteration')
    parser.add_argument('--no-negative', action='store_true', help='exclude negative prefixes')
    return parser.parse_args()


def get_animal_phrases(
        do_exclude_rhymes=False,
        do_include_alliterations=True,
        alliteration_phone_count=2,
        only_nonnegative=False
):
    animals = get_animals()
    animals = sorted(animals)
    animal_phrases = []
    phraseless_animals = []
    sentiment_misses = set()
    for animal in animals:
        has_phrase = False

        if do_include_alliterations:
            alliterative_adjectives = just_adjectives(get_alliterations(animal, alliteration_phone_count))
            if only_nonnegative:
                alliterative_adjectives, curr_sentiment_misses = just_non_negative(alliterative_adjectives)
                sentiment_misses.update(curr_sentiment_misses)
            if len(alliterative_adjectives) > 0:
                has_phrase = True
            animal_phrases += [f'{aa} {animal}' for aa in alliterative_adjectives]

        if not do_exclude_rhymes:
            rhyming_adjectives = just_adjectives(get_rhymes(animal))
            if only_nonnegative:
                rhyming_adjectives, curr_sentiment_misses = just_non_negative(rhyming_adjectives)
                sentiment_misses.update(curr_sentiment_misses)
            if len(rhyming_adjectives) > 0:
                has_phrase = True
            animal_phrases += [f'{rhyme} {animal}' for rhyme in rhyming_adjectives]

        if not has_phrase:
            phraseless_animals.append(animal)

    if len(sentiment_misses) > 0:
        _logger.debug(f'sentiment misses: {sentiment_misses}')
        # print('sentiment misses:')
        # pprint.pprint(sorted(list(sentiment_misses)))
    return animal_phrases, phraseless_animals


if __name__ == '__main__':
    main()
