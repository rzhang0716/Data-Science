from art import logo, vs
from game_data import data
import random

# Print the logo
print(logo)

# Shuffle the order of list
random_scope = random.sample(range(50),50)

# Define display information function
def compare_num(des1, des2):
  print(f"Compare A: {des1['name']}, {des1['description']}, from {des1['country']}")
  print(vs)
  print(f"Against B: {des2['name']}, {des2['description']}, from {des2['country']}")
# Initial the first comparison
dic_loction = 1
des1 = data[random_scope[dic_loction-1]]
des2 = data[random_scope[dic_loction]]
compare_num(des1=des1, des2=des2)


# Define compare and against function
score = 0
while score < 49:
  if des1['follower_count'] > des2['follower_count']:
    guess_result = 'A'
  elif des1['follower_count'] < des2['follower_count']:
    guess_result = 'B'
    des1 = des2

    
  guess = input("Who has more followers? Type 'A' or 'B':\n")

  if guess == guess_result:
    score += 1
    dic_loction += 1
    des2 = data[random_scope[dic_loction]]
    print(f"You're right! Current score: {score}")
    compare_num(des1=des1, des2=des2)
    # print(f"Compare A: {des1['name']}, {des1['description']}, from {des1['country']}")
    # print(vs)
    # print(f"Against B: {des2['name']}, {des2['description']}, from {des2['country']}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    break














