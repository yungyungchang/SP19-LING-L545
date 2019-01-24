"""
replace full stop '.' followed by a space ' ' with a full stop and a newline character \n
line.split() separate words by whitespace
"""
import sys
line = sys.stdin.readline()
while line != '':
    for token in line.split():
        if token[-1] in ['?', '!', ';']:
            sys.stdout.write(token + '\n')
        elif token[-1] == '.':
            if token in ['etc.', 'i.e.', 'e.g.', 'a.m.', 'U.S.A', 'p.m.']:
                sys.stdout.write(token + ' ')
            else:
                sys.stdout.write(token + '\n')
        else:
            sys.stdout.write(token + ' ')
    line = sys.stdin.readline()
