# compute the best score for all the score records
def bestQuiz(a):
    if a==[]:return None
    for c in a:
        if c==[]:return None
    (rows,cols)=(len(a),len(a[0]))
    scoreList=computeScore(a)
    if scoreList==None :return None
    maxScore=max(scoreList)
    index=scoreList.index(maxScore)
    return index
#return average score for all the score records
def computeScore(a):
    (rows,cols)=(len(a),len(a[0]))
    scoreList=[]
    for col in xrange(cols):
        colList=[a[i][col] for i in xrange(rows)]
        colSum=0
        counter=0
        for e in colList:
            if e==-1:
                continue
            colSum+=e
            counter+=1
        if counter==0:return None
        scoreList.append(float(colSum)/float(counter))
    return scoreList
print bestQuiz([[-1,-1],[-1,-1]])