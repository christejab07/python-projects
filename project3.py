import random, time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_probs = 10
def generate_prob():
     left = random.randint(min_operand, max_operand)
     right = random.randint(min_operand, max_operand)
     operator = random.choice(operators)
     expr = str(left) + " "+ operator + " " + str(right)
     answer = eval(expr)
     return expr, answer

wrong = 0
input("Press enter to start! ")
print("---------------------------")

start_time = time.time()

for i in range(total_probs):
     expr, answer = generate_prob()
     while True:
          guess = input("Problem #" + str(i+1) + " : " + expr + " = ")
          if guess == str(answer):
               break
          wrong +=1

end_time = time.time()
used_time = round(end_time-start_time, 2)
if wrong>2:
     feedback = "Improve next time!"
else:
     feedback = "Well done!"
print("-----------------------")
print("You used", used_time, "seconds to finish with", wrong, "wrong answers!", feedback)