"""
    replace every space with a newline \n
    replace() to preprocess the text to add a space or after certain punctuation character like , : ''
    """
import sys, re
abbr = ['etc.', 'e.g.', 'i.e.', 'Ph.d.', 'U.S.A.', 'a.m.', 'p.m.']
def tokenise(line, abbr):
    line = re.sub(r'([\(\)"?:!;])', r' \g<1> ', line)
    line = re.sub(r'([^0-9]),', r'\g<1> ', line)
    line = re.sub(r',([^0-9])', r' \g<1>', line)
    line = re.sub(r'  +', ' ', line)

    output = []
    for token in line.split(' '):
        if token[-1] == '.' and token not in abbr:
            token = token[:-1] + ' .'
        output.append(token)
    return ' '.join(output)
line = sys.stdin.readline()
c = 1 # counting the number of sentences
wc = 1 # counting the words in one sentence
while line != '':
    print('sentence_id =', c)
    str = tokenise(line.strip('\n'), abbr)
    print('text:', str)
    list = str.split()
    for w in list:
        print(wc, w, '_ '*8)
        wc = wc + 1
    c = c + 1
    wc = 1
    line = sys.stdin.readline()
