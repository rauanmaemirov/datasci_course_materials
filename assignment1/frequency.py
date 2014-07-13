import sys
import json
from collections import Counter

def main():
    tweet_file = open(sys.argv[1])

    freqs = Counter()
    total = 0

    for line in tweet_file:
        words = json.loads(line).get('text', '').split(" ")

        if len(words):
            for word in words:
                freqs[word.strip()] += 1
                total += 1

    for term, freq in freqs.most_common():
        score = float(freq) / total
        print("%s %f" % (term, score))

if __name__ == '__main__':
    main()
