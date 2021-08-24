def CountWordFromFlie():
    FileName = input ("enter file name")
    WordCount = 0
    file = open(FileName,"r")
   
    for line in file:
        word = line.split()
        WordCount = WordCount + len(word)
    print(WordCount)
CountWordFromFlie()
