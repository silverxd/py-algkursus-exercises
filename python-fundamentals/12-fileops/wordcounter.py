import string
import os

dirname = os.path.dirname(__file__)
datadict = dict()
alphabetsorteddict = dict()
finalsorteddict = dict()
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

alphabetsorteddict = dict(sorted(datadict.items()))     # we gotta do this, otherwise the output will not be alphabetically sorted and will look bad
finalsorteddict = dict(sorted(alphabetsorteddict.items(), key=lambda item: item[1], reverse=True))

with open(outputfile, '+w') as f:
    
    f.write(f'Total word count: {wordcount}\n')
    for key in list(finalsorteddict.keys()):
        f.write(str(key) + ':' + str(finalsorteddict[key]) + "\n")

    print(f'Total word count: {wordcount}\n')
    for key in list(finalsorteddict.keys()):
        print(str(key) + ':' + str(finalsorteddict[key]))
    
    
