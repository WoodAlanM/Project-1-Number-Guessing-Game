# Number guessing game
# 12/30/2022

import random
from statistics import median, mean, mode

def start_game():
  playing = True
  number_of_attempts = 0
  list_of_num_attempts = []

  print("*** Number Guessing Game ***\n")
  # Enter the main game loop
  while playing:
    # Random integer is assigned for checking against later
    answer = random.randint(1, 100)
    number_of_attempts = 0
    # Attempt to receive an integer input between 1 and 100
    try:
      user_answer = int(input("Please enter a number between 1 and 100: "))
    # Prompt for an acceptable integer input upon receipt of inappropriate input
    except ValueError:
      print("Please choose a valid integer between 1 and 100.")
      continue
    # Prompt for an integer betwwen 1 and 100 if input is out of bounds
    if user_answer < 1 or user_answer > 100:
      print("Please choose a number between 1 and 100.")
      continue
    else:
      # Enter answer loop after an appropriate first answer is given
      while True:
        if user_answer != answer:
          # Prompt for a new answer when input does not match random number
          # Also validate new input
          if user_answer > answer:
            while True:
              try:
                user_answer = int(input("Too high.  Try again: "))
              except ValueError:
                print("Please enter a valid integer between 1 and 100.")
                continue
              if user_answer < 1 or user_answer > 100:
                print("Please enter a number between 1 and 100.")
                continue
              else:
                number_of_attempts += 1
                break
          elif user_answer < answer:
            while True:
              try:
                user_answer = int(input("Too low.  Try again: "))
              except ValueError:
                print("Please enter a valid integer between 1 and 100.")
                continue
              if user_answer < 1 or user_answer > 100:
                print("Please enter a number between 1 and 100.")
                continue
              else:
                number_of_attempts += 1
                break
        else:
          # Assign statistical values to appropriate variables
          list_of_num_attempts.append(number_of_attempts)
          attempts_mean = mean(list_of_num_attempts)
          attempts_median = median(list_of_num_attempts)
          attempts_mode = mode(list_of_num_attempts)

          # Output game statistics and prompt to play again
          print("\nCongratulations! The answer was " + str(answer))
          print("\nNumber of attempts: " + str(number_of_attempts))
          replay = input("\nWould you like to play again (y/n): ")
          if replay == "y":
            print("\n")
            break
          else:
            # Say goodbye
            print("\nMean: " + str(attempts_mean))
            print("Median: " + str(attempts_median))
            print("Mode: " + str(attempts_mode))
            print("\nThanks for playing!")
            playing = False
            break

start_game()