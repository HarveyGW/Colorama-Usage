#Made By HarveyGW

import colorama
from colorama import Fore as f
colour = input("What colour do you want: (YELLOW, GREEN, BLUE, RED) ")
message = input("What do you want to say? ")
if colour == "YELLOW":
  print(f.YELLOW)
  print(message)
elif colour == "RED":
  print(f.RED)
  print(message)
elif colour == "BLUE":
  print(f.BLUE)
  print(message)
elif colour == "GREEN":
  print(f.GREEN)
  print(message)
else:
  print("Not a colour!")
