import random
min_number = 1
max_number= 10
nb_questions=4

def ask_question():
     
        a=random.randint(min_number, max_number)
        b=random.randint(min_number, max_number)
        answer_str = input(f"Compute: {a}+{b} = ")
        answer_int= int(answer_str)
        c=a+b
        if answer_int == c:
            print()
            print("Right Answer")
            
        else:
            print("Wrong Answer")
       
       
nb_points= 0
for i in range(0,nb_questions):
    print(f"Question n * {i+1} out of {nb_questions}")
    print()
    ask_question()
    if ask_question:# if is for true statements or expressions, its like if the answer is correct then do thisbecause if is for correct
        nb_points+=1
    print();
    
print(f"Your points: {nb_points} out of {nb_questions}")
 