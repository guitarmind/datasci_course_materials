import sys
import json

def processFrequency(tweet_file):
    allTerms = set()
    allTermFreqCount = 0
    termFreqTable = {}

    # for each line in tweet file
    tweetIndex = 0
    for line in tweet_file:
        tweets = json.loads(line)

        for dataKey in tweets:
            if dataKey == "text":
                text = tweets[dataKey]

                # get all terms
                terms = text.split()

                if len(terms) > 0:
                    for term in terms:
                        term = term.strip()
                        # print "term:", unicode(json.dumps(term), "unicode-escape") 

                        if term not in termFreqTable:
                            termFreqTable[term] = 1
                        else:
                            termFreqTable[term] = termFreqTable[term] + 1


                        allTerms.add(term)
                        allTermFreqCount = allTermFreqCount + 1

                # print unicode(json.dumps(text), "unicode-escape")
            tweetIndex = tweetIndex + 1

    # compute predictive sentiment for all unknown terms
    for term in list(allTerms):
        termFreq = termFreqTable[term]

        # avoid divide by zero issue
        if allTermFreqCount == 0:
          allTermFreqCount = 1
        
        tfRatio = float(termFreq / allTermFreqCount)

        # print out for scoring
        print term + " " + str(tfRatio)

def main():
    tweet_file = open(sys.argv[1])

    # compute TF ratio for each term
    processFrequency(tweet_file)

if __name__ == '__main__':
    main()
