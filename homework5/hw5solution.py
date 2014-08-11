#
#question 
def linearRegression(points):
    xPts=[point[0] for point in points]
    yPts=[point[1] for point in points]
# get the first colum of 2dlist

    xAvg=average(xPts)
    yAvg=average(yPts)
    return none
# use to campare two letter

def letterCounts(word):
    numletters=26
    counts=[0]*numletters
    for c in word:
        coutns[ord(c)-ord('a')]+=1
    return counts
def canFormWord(word,hand):
    numberletters=26
    wordCounts,handCounts=letterCounts(word),letterCounts(hand)
    for i in xrange(numberletters):
        if(handCounts[i]<wordCounts[i]):return False
    return True
def getScore(word,letterCounts):
    

def bestScrabbleScore(dictionary,letterscores,hand):
    # step1 remove all un-formable words
    formableWords=[word for word in dictionary if canFormWord(word,hand)]
    '''
    for word in dictinary :
        if canformWord(word,hand)
            formableWords.appen(word)
    '''
    if (len(formableWords)==0): return None 
    #step2 find the score of every formable word
    scores = [getScore(word,letterScores) for word in formableWords]
    #step3 find the max score
    maxScore=max(scores)
    # find all the words that achieve the max score
    achieveWords=[word for word in formableWords if getScore(word,letterscores)==maxScore]

