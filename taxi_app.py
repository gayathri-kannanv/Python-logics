def mini(dist,mini_rate_perkm):
  rate=dist*mini_rate_perkm
  return rate
def micro(dist,micro_rate_perkm):
  rate=dist*micro_rate_perkm
  return rate
def prime(dist,prime_rate_perkm):
  rate=dist*prime_rate_perkm
  return rate

def taxi():
  ch="y"
  while ch=="y":
    name=str(input("ENTER YOUR NAME: "))
    email=str(input("ENTER YOUR EMAIL: "))
    phoneno=int(input("ENTER YOUR PHONE NO.: "))
    source=int(input("ENTER YOUR SOURCE: "))
    dest=int(input("ENTER YOUR DESTINATION: "))
    dist=dest-source
    rate=0
    mini_rate_perkm=20
    micro_rate_perkm=30
    prime_rate_perkm=50
    car={1:"mini",2:"micro",3:"prime"}
    car_type=int(input("CAR TYPE- ENTER YOUR OPTION:\n1:  MINI\n2: MICRO\n3: PRIME\n=> "))
    if car_type not in car:
      print("invalid car type")
    else:
      if car_type==1:
        rate=mini(dist,mini_rate_perkm)
      elif car_type==2:
        rate=micro(dist,micro_rate_perkm)
      elif car_type==3:
        rate=prime(dist,prime_rate_perkm)
    print("AMOUNT: ",rate)
    print("do you want your receipt:")
    c=input()
    if c=="y":
      print("--------------")
      print(name)
      print(email)
      print(phoneno)
      print("SOURCE: ",source)
      print("DESTINATION: ",dest)
      print("DISTANCE: ",dist,"km")
      print("AMOUNT: Rs.",rate)
      print("---------------")
    print("do you want to continue: ")
    ch=input()
taxi()

