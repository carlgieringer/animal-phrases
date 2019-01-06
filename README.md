# Animal Phrase Generator

Several years ago, some friends stood around looking at each other awkwardly 
at the end of standup, uncertain if we were done or not.  One team member said,
"awesome possum".  Thus begun a daily ritual of ending our standup with an animal
phrase to confirm that standup was over with a laugh.
This library is an exploration in automatically generating rhyming or alliterative 
phrases based on animals.

## Animal Phrase Rules

1. The phrase must be of the form `<adjective> <animal>`
2. The phrase must contain some literary device such as a rhyme or an alliteration.
3. The adjective should have a positive connotation (we want to start the day on 
   the right foot, after all!)
   
   
### Examples

"rococo buffalo", "profuse moose", "astute newt", and "plausible platypus"

## Running

```
# requires python 3.6
pip install -r requirements.txt
bin/get-nrc-emotions.sh
PYTHONPATH=. python animal_phrases/main.py -h
PYTHONPATH=. python animal_phrases/main.py --no-negative --alliterations
```

### How it works

The scripts works roughly by:

1. Compile a list of animals (currently it scrapes https://a-z-animals.com/animals/)
2. Compile a list of adjectives by filtering the Brown corpus to words having part-of-speech of `ADJ`
3. For each animal, find its adjective rhymes and alliterations using the 
   [`pronouncing`](https://pypi.org/project/pronouncing/) library.
    1. For rhymes, return the intersection of adjectives with the rhymes found by searching 
       for the 
       [rhyming_part](https://pronouncing.readthedocs.io/en/latest/pronouncing.html#pronouncing.rhyming_part).
    2. For alliterations, return the intersection of adjectives with the words sharing the first
       `--alliteration-phone-count` phones.
4. If `--no-negative` is present, filter the adjectives to exclude those with negative connotations, as
  reported by the [NRC Emotion Lexicon](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)

## Ideas for Further Improvements

- Enhance alliteration to work similarly to `pronouncing`'s rhyming: both words must match
  sounds up until the first vowel sound (e.g. "axial Akbash")
- Alliterations tend to be pretty common, and the same adjective will appear with multiple animals
  sharing the first initial phone.  Try ranking alliterations by the number of common
  initial phones and then output the best ones.
- finish manually labeling custom-sentiments.txt to increase sentiment precision
- log animals lacking pronunciations in the CMU library; manually provide pronunciations.
- create a model for inferring pronunciation of animals
 