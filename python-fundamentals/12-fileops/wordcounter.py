import string
import os

dirname = os.path.dirname(__file__)
datadict = dict()
sorteddict = dict()
wordcount = 0

basefile = os.path.join(dirname, 'data.txt')
outputfile = os.path.join(dirname, 'finaldat.txt')


text = open (basefile, 'r')
    
for line in text:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split(' ')

    for word in words:
        if word in datadict:
            datadict[word] = datadict[word] + 1
        else:
            datadict[word] = 1
        wordcount += 1

sorteddict = dict(sorted(datadict.items(), key=lambda item: item[1], reverse=True))

with open(outputfile, '+w') as f:
    
    f.write(f'Total word count: {wordcount}\n')
    for key in list(sorteddict.keys()):
        f.write(str(key) + ':' + str(sorteddict[key]) + "\n")

    print(f'Total word count: {wordcount}\n')
    for key in list(sorteddict.keys()):
        print(str(key) + ':' + str(sorteddict[key]))
    
    
