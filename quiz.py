import json
import sys
from random import randint

if __name__ == "__main__":
    questions_file = sys.argv[1]
    questions = json.loads(open(questions_file, 'r').read())

    correct = 0
    question_count = len(questions)

    while len(questions) > 0:
        q = questions.pop(randint(0, len(questions)-1))
        response = input(q['question']+"\n~# ")
        if response == q['answer']:
            correct += 1

    print("You scored {} out of {}.".format(correct, question_count))
