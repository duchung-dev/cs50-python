def main():
  difficulty = input("Difficult or Casual? ")
  players = input("Multiplayer or Single-player? ")

  if difficulty == "Difficult":
    if players == "Multiplayer":
      recommend("Lien quan")
    elif players == "Single-player":
      recommend("tut quan bung c**")
    else:
      print("Enter a valid number of players")
  elif difficulty == "Casual":
    if players == "Multiplayer":
      recommend("Hearts")
    elif players == "Single-player":
      recommend("tu tay bop d**")
    else:
      print("Enter a valid number of players")
  else:
    print("Enter a valid difficulty")

def recommend(game):
  print("You might like", game)

main()