import random
min_number = 1
max_number= 10
nb_questions=4

def ask_question():
     
        a=random.randint(min_number, max_number)
        b=random.randint(min_number, max_number)
        o =random.randint(0,1)
        operator_str = "+"
        if o==1:
            operator_str ="*"
        answer_str = input(f"Compute: {a} {operator_str} {b} = ")
        answer_int= int(answer_str) 
        c=a+b
        if o==1:
            c=a*b
        if answer_int == c:
            return True
            
        return False
       
nb_points= 0
for i in range(0,nb_questions):
    print(f"Question n * {i+1} out of {nb_questions}")
    print()
    if ask_question():# if is for true statements or expressions, its like if the answer is correct then do thisbecause if is for correct
        print("Right Answer")
        nb_points+=1
    else:
        print("Wrong Answer")
    print();
    
print(f"Your points: {nb_points} out of {nb_questions}")
if nb_points == nb_questions:
    print("Excellent")
elif nb_points == 0:
    print("Improve your maths!")
    
average = int(nb_questions/2)
if nb_points >= average:
    print("That's good")
else:
    print("You can do better")