import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def getSentimentTable(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # Print every (term, score) pair in the dictionary
    # print scores.items()
    return scores

def processTweets(tweet_file, sentiTable):
    unknownTerms = set()
    termPosCountTable = {}
    termNegCountTable = {}

    # for each line in tweet file
    tweetIndex = 0
    for line in tweet_file:
        tweets = json.loads(line)

        for dataKey in tweets:
            if dataKey == "text":
                text = tweets[dataKey]

                # compute the sum of sentiment for this tweet text
                score = 0
                for term in sentiTable:
                    # print text, type(text)
                    # print term, type(term)

                    if term in text.encode('utf8'):
                        score = score + sentiTable[term]

                # get all terms
                terms = text.split()

                if len(terms) > 0:
                    for term in terms:
                        term = term.strip()
                        # print "term:", unicode(json.dumps(term), "unicode-escape") 

                        # only consider the terms not found in sentiment table
                        if term not in sentiTable:
                            unknownTerms.add(term)

                            if score > 0:
                                if term not in termPosCountTable:
                                    termPosCountTable[term] = 1
                                else:
                                    termPosCountTable[term] = termPosCountTable[term] + 1
                            elif score < 0:
                                if term not in termNegCountTable:
                                    termNegCountTable[term] = 1
                                else:
                                    termNegCountTable[term] = termNegCountTable[term] + 1

                # print unicode(json.dumps(text), "unicode-escape")
            tweetIndex = tweetIndex + 1

    # compute predictive sentiment for all unknown terms
    for term in list(unknownTerms):
        posCount = termPosCountTable[term] if term in termPosCountTable else 0
        negCount = termNegCountTable[term] if term in termNegCountTable else 0

        # print "Term: ", unicode(json.dumps(term), "unicode-escape")
        # print "posCount: ", str(posCount)
        # print "negCount: ", str(negCount)

        # avoid divide by zero issue
        if negCount == 0:
          negCount = 1
        predictedScore = float(posCount / negCount)

        # print out for scoring
        print term + " " + str(predictedScore)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # lines(sent_file)
    # lines(tweet_file)

    # create a sentiment dictary with (term, score) pairs
    sentiTable = getSentimentTable(sent_file)

    # compute the sum of setiment for each tweet
    processTweets(tweet_file, sentiTable)

if __name__ == '__main__':
    main()
