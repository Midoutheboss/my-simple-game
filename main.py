import random

print("hey!")
print("what do you want to play")
print("1. dice")
print("2. rock paper scissors")
print("3. math game")
print("q. quit")

choices = ["rock", "paper", "scissors"]

while True:
    game_choice = input("enter your choice 1/2/3/q: ")
    if game_choice == "1":
     dice = random.randint(1, 6)
     print("you rolled", dice)
    if game_choice == "2":
     choice = input("enter your hand: ")
     computer_choice = random.choice(choices)
     if choice == computer_choice:
        print("the computer chose:", computer_choice)
        print("it's a draw")
     elif (choice == "rock" and computer_choice == "scissors") or \
             (choice == "paper" and computer_choice == "rock") or \
             (choice == "scissors" and computer_choice == "paper"):
        print("the computer chose:",computer_choice)
        print("you win!")
     else:
        print("the computer chose:", computer_choice)
        print("you lose")
    if game_choice == "3":
        score = 0
        round = 5
        for i in range(round):
            num_1 = random.randint(1, 15)
            num_2 = random.randint(1, 15)
            operator = random.choice(["+", "-", "*", "/"])

            if operator == "+'":
                correct_answer = num_1 + num_2
            if operator == "-":
                correct_answer = num_1 - num_2
            if operator == "*":
                correct_answer = num_1 * num_2
            if operator == "/":
                correct_answer = (num_1 // num_2)

            print(f"question{i+1}: what is {num_1}{operator}{num_2}?")
            user_answer = float(input("enter your answer: "))

            if user_answer == correct_answer:
                print("correct")
                score += 1
                print("your score is: ", score)
            else:
                print("incorrect")
    if game_choice == "q":
     print("thanks for playing")
     break
