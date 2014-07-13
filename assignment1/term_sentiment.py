import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    term_scores = {}

    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        score = 0
        words = json.loads(line).get('text', '').split(" ")

        if len(words):

            for word in words:
                score += scores.get(word, 0)

            term_score = 0.0

            for word in words:
                if word not in scores:
                    term_score = float(score) / len(words)
                    print("%s %f" % (word.encode('utf-8'), term_score))

if __name__ == '__main__':
    main()
