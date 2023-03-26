from quiz import Quiz
import  random

vocabulary_list=[]
svocabulaey_list=[]


print(f"Number enter:")

for _ in range(int(input())):
                evocabulary = input(str("English vocabulary:"))
                svocabulaey = input(str("Spanish vocabulary:"))
                set_list = (evocabulary, svocabulaey)
                vocabulary_list.append(set_list)
                sort_list = sorted(list(x for x in vocabulary_list))
                print(f"English Word:{sort_list}")

def go():
        quiz_question = random.choice(vocabulary_list)
        quiz_qs = quiz_question[0]
        print(quiz_qs)
        quiz_answer = input("Spanish:")
        P1 = Quiz()
        P1.generate(quiz_answer, quiz_question[1])
        P1.end()

go()
while True:
        keep_playing=input("Continue or not:(y/n)")
        if keep_playing.lower()!="y":
                break

        else:
                go()

if __name__=="main":
        print("Good")



































