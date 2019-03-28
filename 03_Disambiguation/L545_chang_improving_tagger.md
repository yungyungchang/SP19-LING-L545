UD_Chinese-GSD was used to train the perceptron tagger, which was evaluated by 2017 CoNLL evaluation script. Table 1 is the performance of perceptron-based tagger before any improvement of features on the tagger.py file, and Table 2 is the performance of the revised perceptron-based tagger.

Table 1. The performance of perceptron-based tagger for Chinese before improvement of features on the tagger file
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     90.81 |     90.81 |     90.81 |     90.81
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     90.81 |     90.81 |     90.81 |     90.81
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

Table 2. The performance of perceptron-based tagger for Chinese after improvement of features on the tagger file 
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     91.08 |     91.08 |     91.08 |     91.08
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     91.08 |     91.08 |     91.08 |     91.08
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

I made the following changes in the section of get_features() in tagger.py:
1. define the word's suffix as the last character of the word: word[-3:0] -> word[-1]
2. do not add features of suffic in previous/following words

Generally speaking, Chinese does not have many suffixes and prefixes, but according to Chinese morphology, suffix or prefix in one compound word corresponds to the part-of-speech of that compound word. For example, dai 'generation' can be considered as a suffix of nian-dai 'year-generation; decade,' and both dai and nian-dai are nouns. Dai as a suffix can found in the following nouns: shi-dai 'time-generation; era,' gu-dai 'old-generation; ancient times,' jin-dai 'close-generation; modern times' and etc.
Most of words in Chinese are disyllabic, so the tagger first can acquire the part-of-speech of the suffix or prefix in one disyllabic word in training data and then use one of it to perdict the part-of-speech of compound words in the testing data to increase the accuracy of tagging.
