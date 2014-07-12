import sys
import json
from operator import itemgetter

def processTopTenHashtag(tweet_file):
    allHashtag = set()
    hashtagFreqTable = {}

    # for each line in tweet file
    for line in tweet_file:
        tweet = json.loads(line)

        hashtags = None
        if "entities" in tweet and tweet["entities"] != None:
            entities = tweet["entities"]
            if "hashtags" in entities and entities["hashtags"] != None and len(entities["hashtags"]) > 0:
                hashtags = entities["hashtags"]

                for entry in hashtags:
                    if "text" in entry and entry["text"] != None:
                        hashtag = entry["text"].strip()

                        # print "hashtag: ", hashtag

                        if hashtag not in hashtagFreqTable:
                            hashtagFreqTable[hashtag] = 1
                        else:
                            hashtagFreqTable[hashtag] = hashtagFreqTable[hashtag] + 1

                        allHashtag.add(hashtag)


    # sort to get top-10 frequent hastags
    sortedHashtagFreqTable = sorted(hashtagFreqTable.iteritems(), key=itemgetter(1), reverse=True)

    count = 0
    for pair in sortedHashtagFreqTable:
        hashtag = pair[0]
        freq = pair[1]

        # print out for grading
        if count < 10:
            print hashtag + " " + str(freq)
            # print unicode(json.dumps(hashtag), "unicode-escape") + " " + str(freq)

        count = count + 1

def main():
    tweet_file = open(sys.argv[1])

    # compute top-10 hash tag
    processTopTenHashtag(tweet_file)

if __name__ == '__main__':
    main()
