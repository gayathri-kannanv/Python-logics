def rock():
  ch="y"
  while (ch=="y"):
    play1=str(input("PLAYER 1:enter your option:  "))
    play2=str(input("PLAYER 2:enter your option:  "))
    arr=["rock","paper","scissor"]
    if play1 not in arr and play2 not in arr:
      print("invalid option")
    else:
      if (play1==play2):
        print("DRAW GAME")
      elif (play1=="rock" and play2=="paper"):
        print("PLAYER 2 WINS")
      elif (play1=="rock" and play2=="scissor"):
        print("PLAYER 1 WINS")
      elif (play1=="paper" and play2=="rock"):
        print("PLAYER 2 WINS")
      elif (play1=="paper" and play2=="scissor"):
        print("PLAYER 1 WINS")
      elif (play1=="scissor" and play2=="paper"):
        print("PLAYER 1 WINS")
      elif (play1=="scissor" and play2=="rock"):
        print("PLAYER 2 WINS")
      print("do u want to continue: ")
      ch=input()
rock()

