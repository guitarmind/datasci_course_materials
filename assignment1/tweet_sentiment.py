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

                # print sentiment for grading
                print score

                # print unicode(json.dumps(text), "unicode-escape")
            tweetIndex = tweetIndex + 1

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
