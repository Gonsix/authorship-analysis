
import re

from .load_data import DocID

RED = '\033[31m'
GREEN = '\033[32m'
END = '\033[0m'

# This fuction search from query in specified datasets and print it out.
# Inputs
#   documents : The array of Documents, or Pandas DataSeries. One document consists of a list of tuple (word, POS).
#   query_string : Input query from User, may contain rejex (e.g "of JJ plan.*")
#   datasets : An array of Index of Datasets to be searched in. You can use DocID class for Macro-like symbol.
# NOTE Capital is not distinguished for searching.

def search(documents, query_string, datasets=[DocID.Q, DocID.K1, DocID.K2]):  
    query = query_string.split()
    print("query : ", query)
    for docId in datasets:
        document = documents[docId]
        for idx, (word, pos), in enumerate(document):

            try: 
                res = re.fullmatch(query[0].casefold() , word.casefold()) # If rejex matched, undistinguith Upper or Lower case
            except:
                res = None
            if res:
                # check the following words matche the sequence of words
                foundFlg = True

                if len(query)>1:

                    for i, query_following in enumerate(query[1:]):
                        try:
                            word_following = document[idx+1+i][0] # follwoing word in the document
                            pos_following = document[idx+1+i][1] # follwoing pos in the document
                        except: # if cannot access the index
                            break

                        try:
                            res2 = (re.fullmatch(query_following.casefold(),word_following.casefold()) or query_following == pos_following) # If rejex matched, undistinguith Upper or Lower case
                        except:
                            res2 = None

                        if res2:
                            continue
                        foundFlg = False
                    
                if foundFlg is True:
                    if docId == DocID.Q:
                        print("Q :  ", end="")
                    elif docId == DocID.K1:
                        print("K1:  ", end="")
                    elif docId == DocID.K2:
                        print("K2:  ", end="")


                    # # 前後6 文字　出力
                    for j in range(idx-6, idx+7):
                            if 0 <= j and  j < len(document):
                                if idx <= j and j < idx + len(query):  # within queried words
                                    print(GREEN + document[j][0] + END, end=" ")
                                else:    
                                    print(document[j][0], end=" ")
                            else:
                                print("    ", end="")

                    print()
                
