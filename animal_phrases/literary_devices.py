import pronouncing


def get_alliterations(word, phone_count=2):
    pronunciations = pronouncing.phones_for_word(word)
    alliterations = set()
    for pronunciation in pronunciations:
        first_phones = pronunciation.split()[:phone_count]
        curr_alliterations = pronouncing.search('^' + ' '.join(first_phones))
        alliterations.update(curr_alliterations)
    return alliterations


def get_rhymes(word):
    pronunciations = pronouncing.phones_for_word(word)
    rhymes = set()
    for pronunciation in pronunciations:
        rhyming_part = pronouncing.rhyming_part(pronunciation)
        curr_rhymes = pronouncing.search(rhyming_part + "$")
        rhymes.update(curr_rhymes)
    return rhymes


if __name__ == '__main__':
    # preposterous rhinocerous?
    print(get_rhymes('rhinocerous'))
