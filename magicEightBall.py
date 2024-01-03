#slightly revamped version of my "famous" 8th grade program
#magic 8 ball
import random

negativeResponses = ["no", "nope", "nah", "not really", "n"]
randomResponses = ["yes", "of course", "it is certain", "obviously",
                   "ask me later", "im too lazy", "definitely",
                   "only if its vrinda", "clearly", "no",
                   "dont even bring this horrible topic up",
                   "the answer is no", "definitely NOT",
                   "WHY WOULD YOU EVEN ASK THIS",
                   "you know that im a bot right",
                   "i cant answer your life questions"]

while True:
    input("Ask a yes or no question. ")
    print(random.choice(randomResponses))
    if input("Would you like to ask another question? ") in negativeResponses:
        break
