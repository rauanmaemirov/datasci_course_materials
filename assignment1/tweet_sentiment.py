import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}

    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        score = 0
        words = json.loads(line).get('text', '').split(' ')
        for word in words:
            score += scores.get(word, 0)

        print(score)

if __name__ == '__main__':
    main()
