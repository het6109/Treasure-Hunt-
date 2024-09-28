print("Welcome to treasure island !")
name=input("what is your name ?")  
print("Hello" + f"{name}")
print("Your mission is to find the treasure")
choice1=input(" Your are at a turn , where do you want to go? left or right?")
if choice1=="right":
  print("Fell into a hole. Game over")
else:
  choice2=input("You have come to a lake. Ther is an island in middle of lake. Would you like to wait or swim?")
  if choice2=="swim":
    print("Attacked by a swamp monster. Game over")
  else:
    choice3=input("You have arrived at the island and found out a house with three old doors. Which coloured door would you like to open? Red, Blue or Yellow?")
    if choice3=="Red":
      print("Fire caught you up. Game over")
    if choice3=="Yellow":
      print("You found out a old dead body. On going near to it you found out that it was a witch and she came alive and killed you. Game over")
    else:
      print("Behind the door you found a basement and went ahead. At the end of the basement you found out treasure. You win !!!")