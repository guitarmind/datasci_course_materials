import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def getSentimentTable(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # Print every (term, score) pair in the dictionary
    # print scores.items()
    return scores

def getPossibleState(full_name):
    predictState = None

    if len(full_name) > 0:
        tokens = full_name.split(',')
        if len(tokens) == 2:
            firstToken = tokens[0].strip()
            secondToken = tokens[1].strip()

            if secondToken in states:
                return secondToken

            for state in states:
                stateWords = states[state].split()
                for word in stateWords:
                    if word.lower() == firstToken.lower():
                        predictState = state

                if states[state].lower() == firstToken.lower():
                    predictState = state

    return predictState

def processHappiestState(tweet_file, sentiTable):
    stateTweetCount = {}
    statePosSentimentCount = {}
    happiestState = None
    happiestStateAvgSentiment = 0.0

    # for each line in tweet file
    for line in tweet_file:
        tweet = json.loads(line)

        state = None
        score = 0
        if "place" in tweet and tweet["place"] != None and "text" in tweet and tweet["text"] != None:

            place = tweet["place"]

            # only consider the tweet from U.S.
            if "country_code" not in place and "full_name" not in place:
                continue
            elif "country_code" in place and place["country_code"] != "US" and "full_name" in place:
                continue

            # print "country_code:", place["country_code"]
            # print "full_name:", place["full_name"]
            # print unicode(json.dumps(place), "unicode-escape")

            # guess for possible state of this tweet
            full_name = place["full_name"]
            state = getPossibleState(full_name)
            # print "Matched state:", state

            coordinates = None
            if "coordinates" in place:
                coordinates = place["coordinates"]

            text = tweet["text"]

            # compute the sum of sentiment for this tweet text
            for term in sentiTable:
                if term in text.encode('utf8'):
                    score = score + sentiTable[term]

            # print sentiment for grading
            # print score

            # print unicode(json.dumps(text), "unicode-escape")
         
        if state != None:
            if score > 0:
                if state not in statePosSentimentCount:
                    statePosSentimentCount[state] = 1
                else:
                    statePosSentimentCount[state] = statePosSentimentCount[state] + 1

            if state not in stateTweetCount:
                stateTweetCount[state] = 1
            else:
                stateTweetCount[state] = stateTweetCount[state] + 1

    # compute the state with highest averge positive sentiment
    for state in states:
        tweetCount = 0
        posCount = 0
        avgSentiment = 0.0

        if state in stateTweetCount:
            tweetCount = stateTweetCount[state]
        if state in statePosSentimentCount:
            posCount = statePosSentimentCount[state]

        if tweetCount > 0 and posCount > 0:
            avgSentiment = float(posCount / tweetCount)

            if happiestStateAvgSentiment < avgSentiment:
                happiestStateAvgSentiment = avgSentiment
                happiestState = state

        # print state
        # print "avgSentiment: ", avgSentiment

    # print out happiest state for grading
    print happiestState
    # print "happiestStateAvgSentiment: ", happiestStateAvgSentiment


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # create a sentiment dictary with (term, score) pairs
    sentiTable = getSentimentTable(sent_file)

    # compute the sum of setiment for each tweet
    processHappiestState(tweet_file, sentiTable)

if __name__ == '__main__':
    main()
