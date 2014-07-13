import sys
import json
from collections import Counter

states_list = {
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

def state_by_name(state_name):
    for code, name in states_list.items():
        if name == state_name:
            return code
    return None

def find_state(tweet):

    place = tweet.get('place')
    state = None

    # TODO Try finding state from user location info
    if not place or not place.get('country', '') == 'United States':
        return None

    state_name, state_code = place.get('full_name', '').split(',')
    state_code = state_code.strip()

    if state_code == 'USA':
        state = state_by_name(state_name)
    elif state_code == 'Puerto Rico':
        state = 'PR'

    return state

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    states_sent = Counter()

    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        score = 0

        tweet = json.loads(line)
        words = tweet.get('text', '').split(' ')

        state = find_state(tweet)

        # Calculate tweet sentiment score
        for word in words:
            score += scores.get(word.strip(), 0)

        if state:
            states_sent[state] += score

    happiest_state, happiest_score = states_sent.most_common(1)[0]
    print(happiest_state)

if __name__ == '__main__':
    main()
