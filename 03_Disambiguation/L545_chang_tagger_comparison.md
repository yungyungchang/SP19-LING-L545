L545 Tagger Comparison

Table 1. the performance of UDPipe for Finnish
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.64 |     94.64 |     94.64 |     94.64
XPOS       |     95.81 |     95.81 |     95.81 |     95.81
Feats      |     90.77 |     90.77 |     90.77 |     90.77
AllTags    |     89.75 |     89.75 |     89.75 |     89.75
Lemmas     |     84.52 |     84.52 |     84.52 |     84.52
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

Table 2. the performance of Perceptron-based tagger for Finnish
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     90.28 |     90.28 |     90.28 |     90.28
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     90.28 |     90.28 |     90.28 |     90.28
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

In Table 1, the precision score of XPOS shows that UPPipe for Finnish is 95.81% accurate out of the predicted positive, whereas in Table 2, Perceptron-based tagger is 90.28% accurate. Also, the percentage of the false positive (which means that the actual tag of a word is different from the one that the tagger is assigned) for UPpine is 4.19%, while the percentage of the false positive for Perceptron-based tagger is 9.72%. Consierding F1 scores in Table 1 and Table 2, the F1 score of UPOS for UDpipe is lower higher than the one for Perceptron-based tagger. It is close to 1, so it is a good F1 score that the UDpipe has low false negatives and low positives.
