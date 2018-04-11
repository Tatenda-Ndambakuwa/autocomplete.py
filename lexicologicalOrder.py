# code to get the first five words
def extract(query):
    # initializing
    nextString = "a"
    words=[]
    recentWord=str()
    database= []
    count =0
    keepGoing = True
# begin while
    while ( keepGoing):
        count +=1
        words= query(nextString)
        #print (words)
        #print (len (words))
        #lastWord= (words[-1])
        newWords = len(words)>0 and ((words[-1])not in database)
        if (newWords):
            database= database + words
            #getting rid of duplicates sets
            database= list(set(database))
            database.sort()
            # removing unnecessary iterations eg when less than five words are returned
            if (len(words)<5):
                nextString=(chr(ord(nextString[0:1]) + 1))
            else:
                nextString= (words[-1])
        elif (len(nextString)>1):
            nextString = (nextString[:-1])
        elif (nextString=="z"):
            keepGoing = False
        else:
            nextString= (chr(ord(nextString) + 1))
            # to look at what letters are being checked
            # print ('checking '+nextString)
    ## to check what words are returned
    #print (database)
    print(" Number of iterations "+ str(count) )
    return database # end while

##################################################################################
# start main method
##################################################################################

def main():
    # type: () -> object
    #"""Runs your solution -- no need to update (except to maybe try out different databases)."""
    # Sample implementation of the autocomplete API
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    # getting the first five words that match the query
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    # making sure what we get as results matches what we have in the database
    assert extract(query) == database

main() # call main
