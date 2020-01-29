import random
def random1():
  min=int(input("enter the min value: "))
  max=int(input("enter the max value: "))
  rand=random.randint(min,max)
  ch="y"
  while (ch=="y"):
    num=int(input("ENTER GUESS NUMBER:\n"))
    if num==rand:
      print("YOU WIN!!!!!")
    else:
      print("try again!!!!!!")
    print("do u want to continue: ")
    ch=input()

random1()
