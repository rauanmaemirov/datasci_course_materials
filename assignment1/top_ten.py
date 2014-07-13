import sys
import json
from collections import Counter

def main():
    tweet_file = open(sys.argv[1])

    hashtag_freqs = Counter()

    for line in tweet_file:
        tweet = json.loads(line)
        if 'entities' in tweet:
            hashtags = tweet['entities'].get('hashtags', [])

            if len(hashtags):
                for hashtag in hashtags:
                    hashtag_freqs[hashtag['text'].encode('utf-8')] += 1

    top_ten = hashtag_freqs.most_common(10)

    for trending in top_ten:
        print("%s %d" % trending)

if __name__ == '__main__':
    main()
