#!/usr/bin/env python3

import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
q= trivia["question"]

a=trivia["correct_answer"]
b=trivia["incorrect_answers"][0]
c=trivia["incorrect_answers"][1]
d=trivia["incorrect_answers"][2]

#print(f"{q}")

print(html.unescape(q))
print(html.unescape(a))
print(html.unescape(b))
print(html.unescape(c))
print(html.unescape(d))
