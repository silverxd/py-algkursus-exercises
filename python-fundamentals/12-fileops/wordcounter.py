import string

datadict = dict()
wordcount = 0
text = open ("./12-fileops/data.txt", 'r')
    
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

with open('./12-fileops/finaldat.txt', '+w') as f:
    
    f.write(f'Total word count: {wordcount}\n')
    for key in list(datadict.keys()):
        f.write(str(key) + ':' + str(datadict[key]) + "\n")

    print(f'Total word count: {wordcount}\n')
    for key in list(datadict.keys()):
        print(str(key) + ':' + str(datadict[key]) + "\n")
    
    
