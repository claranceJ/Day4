#understanding variables, data types and calling a function

def get_choices():
  #getting input from user
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  computer_choice = "paper"
  # using a Dictionary
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

choices = get_choices()
print(choices)
