from sys import exit

"""
The gold_room has a weird way of getting you to type a number. What are all 
the bugs in this way of doing it? Can you make it better than just 
checking if “1” or “0” are in the number? Look at how int() works for clues.
"""
def gold_room():
  print "This room is full of gold. How much will you take?"
  next = raw_input("> ")

  if "0" in next or "1" in next:
    how_much = int(next)
  else: 
    dead("Man, learn to type a number.")

  if how_much < 50:
    print "Nice, you are not greedy! You win!"
    exit(0)
  else:
    dead("You greedy bastard!")

def bear_room():
  print """There is a bear here.
           The bear has a bunch of honey.
           The fat bear is in front of another door.
           How are you going to move the bear?
           otions: take honey, taunt bear, open door
           """
  bear_moved = False

  while True:
    next = raw_input("> ")

    if next == "take honey":
      dead("The bear slaps you like the hoe you are.")
    elif next == "taunt bear" and not bear_moved:
      print "The bear has moved from the door, you can go through now."
      bear_moved = True
    elif next == "taunt bear" and bear_moved:
      dead("The bear chews your leg off")
    elif next == "open door" and bear_moved:
      gold_room()
    else:
      print "I got no idea what that means"

def cthulu_room():
  print """ You see the great evil cthulu
            You go insane and shart yourself
            Do you stay and eat your head, or run
        """
  next = raw_input("> ")

  if "flee" in next:
    start()
  elif "head" in next:
    dead("Well that was tasty!")
  else:
    cthulu_room()

def dead(why):
  print why, "Good job!"
  exit(0)

def start():
  print "You are in a dark room, do you take the right, straight, or left door?"
  next = raw_input("> ")

  if next == "left":
    bear_room()
  elif next == "right":
    cthulu_room()
  elif next == "straight":
    gold_room()
  else:
    dead("You stumble around the room and die of diarrhea.")

start()