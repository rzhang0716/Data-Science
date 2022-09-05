############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo
import random
if_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n")
while if_play == 'y':
  print(logo)
  def get_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_index = random.randint(0,len(cards)-1)
    card = cards[random_index]
    return card


  def compare_results(player_score, computer_score):
    print(f"Your final hand: {player_card}, final score: {player_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    if player_score < computer_score:
      print('You lose')
    elif  player_score > computer_score:
      print('You Win')
    else:
      print('Draw')


  def if_ace(ace_card):
    for i in range(len(ace_card)):
      if ace_card[i] == 11:
        ace_card[i] -= 10
    return ace_card

  def over_21():
    print('Burst')

  def one_more(player_score,player_card):
    s = get_a_card()
    player_score+= s
    player_card.append(s)
    # if player_score > 21:
    #   print(f"Your final hand: {player_card}, final score: {player_score}")
    #   print('You Busrt')
    #   print('Computer win!')
    # else:
    #   print(f"your cards: {player_card}, current score: {player_score}")
    #   print(f"Computer's first card: {computer_card[0]}")
    return player_score, player_card

  # def one_more(player_score,player_card):
  #   s = get_a_card()
  #   player_score+= s
  #   player_card.append(s)
  #   if player_score > 21:
  #     print(f"Your final hand: {player_card}, final score: {player_score}")
  #     print('You Busrt')
  #     print('Computer win!')
  #   elif player_score <= 21:
  #     print(f"your cards: {player_card}, current score: {player_score}")
  #     print(f"Computer's first card: {computer_card[0]}")
  #     another_card = input("Type 'y' to get another card, type 'n' to pass: ")
  #     if another_card == 'y':
  #       one_more()
  #   return player_score, player_card


  # if_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
  # while if_play == 'y':
  #   print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_card = []
  computer_card = []
  player_score = 0
  computer_score = 0
  s1 = get_a_card()
  player_card.append(s1)
  player_score+=s1

  s2 = get_a_card()
  player_card.append(s2)
  player_score+=s2

  s3 = get_a_card()
  computer_card.append(s3)
  computer_score+=s3

  print(f"your cards: {player_card}, current score: {player_score}")
  print(f"Computer's first card: {computer_card[0]}")


  def f(player_score=player_score,player_card=player_card,computer_score=computer_score,computer_card=computer_card):
    # if computer_score < player_score:
    #   s4 = get_a_card()
    #   computer_score += s4
    #   computer
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'n': 
      s4 = get_a_card()
      computer_score += s4
      computer_card.append(s4)
      if player_score > computer_score and computer_score < 21:
        s5 = get_a_card()
        computer_score += s5
        computer_card.append(s5)
      if computer_score > 21:
        print('Computer Busrt')
        print('You win!')
      elif player_score < computer_score:
        print(f"Your final hand: {player_card}, final score: {player_score}")
        print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
        print('You lose')
      elif player_score == computer_score:
        print(f"Your final hand: {player_card}, final score: {player_score}")
        print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
        print('Draw')
    elif another_card == 'y':
      s6 = get_a_card()
      player_score+= s6
      player_card.append(s6)
      if player_score > 21:
        print(f"Your final hand: {player_card}, final score: {player_score}")
        print('You Busrt')
        print('Computer win!')
      elif player_score <= 21:
        # s7 = get_a_card()
        # player_score+= s7
        # player_card.append(s7)
        print(f"your cards: {player_card}, current score: {player_score}")
        print(f"Computer's first card: {computer_card[0]}")
        # another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        f(player_score=player_score,player_card=player_card,computer_score=computer_score,computer_card=computer_card)

  f(player_score=player_score,player_card=player_card,computer_score=computer_score,computer_card=computer_card)





