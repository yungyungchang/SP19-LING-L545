L545 Yung-Yung Chang
Train, Parse, and Evaluate using UDPipe

I used UDPipe to train a model for Chinese UD treebank (Chinese-GSD). The evaluation of the performance of the parser is in Table 1.

Table 1. Evaluation of the performance of UDPipe parser for Chinese
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     82.87 |     82.87 |     82.87 |     82.87
LAS        |     79.98 |     79.98 |     79.98 |     79.98

The performance of UAS and LAS does not reach 90%. UAS measure how well HEAD match and LAS measures how well Head and Deprel match. The first interesting error I found is that the parser seems to be unable to determine a specific relation for a verb. For example, you 'to have' in Chinese can be a enistential verb or a possesive verb. The parser is not able to decide whether you 'to have' should be a root or not. Another interesting error is that the parser cannot decide whether a pronoun is a direct or indirect object. The reason might be that animate and inanimate pronouns share the same character. For example, the character 他 ta can mean she, he, or it.

