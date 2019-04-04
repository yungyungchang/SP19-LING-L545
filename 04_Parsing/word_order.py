IN = open('vi_vtb-ud-test.conllu')
sent = []
line = 'xxx'
vo_count = 0
ov_count = 0
while line:
    line = IN.readline()
    if len(line) >1:
        if line.startswith('1'):
            list = line.split()
            sent.append(list)
    else:
        for item in sent:
            if (item[7]) == 'obj':
                n1 = int(item[0])
                n2 = int(item[6])
                if n1 > n2:
                    vo_count += 1
                else:
                    ov_count += 1
        sent = []
print('UD Vietnamese-VTB treebank')
print('the number of vo word order: ', vo_count)
print('proportion of vo word order: ', vo_count/(vo_count + ov_count))
print('the number of ov word order: ', ov_count)
print('proportion of ov word order: ', ov_count/(vo_count + ov_count))
IN.close()
