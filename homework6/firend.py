'''
def friendsOfFriends(d):
    # create a new dictionary
    newD =dict()
    for person in d:
        friends=d[person]
        #loop through all the people for every one find their firends
        for friend in friends:
            otherfriends = d[friend]
           # get undirected friends of on person
            undirectFL=(otherfriends-friends)-set(person)
           # for all undirected friends
            for val in undirectFL:
                #check the person has already a set in dictionary 
                # if so add val other wise create a new set
                if person in newD.keys():
                    newD[person].add(val)
                else:
                    newD[person]=set([val])
    for person in d:
      if person not in newD:
        newD[person]=set()
    return newD
'''

