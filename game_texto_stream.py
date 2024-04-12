import time
import random

def display_intro():
    print("Welcome to the Challenging Text Adventure Game!")
    print("You find yourself in a dark and treacherous forest. Your survival depends on your choices.")
    print("Make the wrong decisions, and you may never escape this forest. Good luck!\n")

def make_choice(options):
    while True:
        choice = input("Choose an option ({0}): ".format('/'.join(options))).strip().lower()
        if choice in options:
            return choice
        else:
            print("Invalid input. Please choose a valid option.")

def encounter_wild_animal():
    print("As you walk through the forest, you encounter a wild animal!")
    time.sleep(1)
    print("It's a fierce wolf!")
    time.sleep(1)
    print("What do you want to do?")
    print("a: Fight the wolf")
    print("b: Try to run away")
    choice = make_choice(['a', 'b'])
    if choice == 'a':
        print("You decide to fight the wolf!")
        time.sleep(1)
        print("You grab a stick nearby and bravely face the wolf.")
        time.sleep(2)
        if random.random() < 0.5:
            print("Incredibly somehow, you manage to defeat the wolf! You can continue your journey.")
            print("You can continue your previous path.")
        else:
            print("The wolf proves to be too strong for you. You barely escape with your life.")
            print("You died horribly, jackass.")
    else:
        print("You try to run away from the wolf.")
        time.sleep(2)
        if random.random() < 0.3:
            print("You manage to escape from the wolf and continue your journey.")
            print("You can continue your previous path.")
        else:
            print("The wolf catches up to you and attacks. You are injured, but you manage to scare it away.")
            print("You died horribly, jackass.")

def find_useful_item():
    print("While exploring the forest, you find a hidden stash!")
    time.sleep(1)
    print("Inside the stash, you find a potion of healing.")
    time.sleep(1)
    print("This potion can help you in your journey.")
    time.sleep(1)
    print("You add the potion to your inventory.")
    print("You can continue your previous path.")

def solve_environmental_riddle():
    print("You come across an ancient stone monument with mysterious inscriptions.")
    time.sleep(1)
    print("The inscriptions seem to be a riddle.")
    time.sleep(1)
    print("Solve the riddle to proceed.")
    time.sleep(1)
    print("Riddle: Say friend to unlock?")
    answer = input("Your answer: ").strip().lower()
    if answer == "friend":
        print("Correct! The stone monument trembles, and a hidden passage is revealed.")
        print("You found Pamela Anderson and she made your dream come through.")
        time.sleep(1)
        print("You can continue your journey.")
    else:
        print("Incorrect answer. You must ponder the riddle further to proceed.")

def discover_secret_location():
    print("While exploring the forest, you notice a strange pattern in the trees.")
    time.sleep(1)
    print("Following your instincts, you investigate further and find a hidden cave.")
    time.sleep(1)
    print("Inside the cave, you discover a secret chamber.")
    time.sleep(1)
    print("The chamber contains a valuable treasure!")
    time.sleep(1)
    print("You collect the treasure and continue your journey.")

def random_events():
    events = [encounter_wild_animal, discover_secret_location, solve_environmental_riddle, find_useful_item]
    random.choice(events)()


def path_a():
  time.sleep(2)
  print("You can cross the river (a) or follow it downstream (b).")
  choice_a = make_choice(['a', 'b'])
  if choice_a == 'a':
    print("You try to cross the river but get swept away by the current. Game Over!")
  else:
    print("You follow the river downstream and find a hidden waterfall. You can climb it (a) or go around it (b).")
    choice_waterfall = make_choice(['a', 'b'])

    if choice_waterfall == 'a':
      print("You successfully climb the waterfall, but you encounter a dangerous creature on the other side.")
      time.sleep(2)
      print("You have two allies from Clash of Clans, P.E.K.K.A and Wizard, to help you defeat the creature.")
      print("a: Choose P.E.K.K.A to wage war")
      print("b: Choose Wizard to wage war ")
      ally_choice = make_choice(['a', 'b'])
      if ally_choice == 'a':
          print("You choose P.E.K.K.A, and together you defeat the creature and successfully escape")
          time.sleep(2)
          print("Now both of you applies to the next Monster Inc. movie as Sully and boo")
          time.sleep(2)
          print("You win!")
      else:
          print("You choose Wizard, but the creature proves too powerful and transforms you in a dwarf.")
          time.sleep(2)
          print("As a dwarf you don't have the height to play the game.")
          time.sleep(2)
          print("Game over!")
    else:
      print("As you go around, you found Bilu, the E.T.")
      time.sleep(2)
      print("You can't handle all the knowledge and dies")
      time.sleep(2)
      print("Game over!")

def path_b():
  time.sleep(2)
  print("You enter the cave and discover a treasure chest guarded by a albine dragon.")
  time.sleep(2)
  print("You have two options to defeat the dragon:")
  print("a: Use an electro dragon lord of dragons.")
  print("b: Use a little sword.")
  
  dragon_choice = make_choice(['a', 'b'])
  if random.random() < 0.3:
    random_events()
    continue_path(dragon_choice = dragon_choice)
  else:
    if dragon_choice == 'a':
        print("You summon the electro dragon lord of dragons, which defeats the albine dragon.")
        time.sleep(2)
        print("As reward the dragon transforms you in an electrified albino.")
        time.sleep(2)
        print("You win!.")
    else:
        print("You attempt to fight the dragon with the little sword, but it's not enough. The dragon breathes fire on you.")
        time.sleep(2)
        print("You died horribly, jackass.")
        time.sleep(2)
        print("Game over!")

def path_c():
  time.sleep(2)
  print("You enter the mysterious house. It's dark inside.")
  time.sleep(2)
  print("Do you explore the house (A) or leave immediately (B)?")
  choices = {
      'a': "Explore the house.",
      'b': "Leave immediately."
  }

  choice_house = make_choice(choices)

  if random.random() < 0.3:
    random_events()
    continue_path(choice_house = choice_house)
  else:   
    if choice_house == 'a':
        print("You explore the house and discover two different paths:")
        time.sleep(2)
        print("a: Talk to Martina Oliveira from only fans")
        print("b: Get a drug that could help")
        
        house_choice = make_choice(['a', 'b'])
        
        if house_choice == 'a':
            print("She says: 2 dollars or a mystery box?.")
            time.sleep(2)
            print("You do not have time to answer, a big witch sudenly appears.")
            time.sleep(2)
            print("You just turn around with a hard dick and...")
            time.sleep(2)
            print("You Win, fatality! (read as in mortal combat).")
        else:
          print("You took an insane amout of molly")
          time.sleep(2)
          print("You enter in a  giant island and get lost in its vastness.")
          time.sleep(2)
          print("Game over.")

    else:
        print("When you are leaving the house, you fall in a Saw movie like trap and dies!")
        time.sleep(2)
        print("Game over!")

def continue_path(choice = None, dragon_choice = None, choice_house = None):
  if choice:
    path_a()
  elif dragon_choice:
    path_b()
  else:
    path_C()
  
def forest_path():
    print("You start walking through the forest...")
    time.sleep(2)
    
    paths = {
        'a': "You take the left path and find a river.",
        'b': "You take the right path and come across a cave.",
        'c': "You venture deeper into the forest and find a mysterious house."
    }
    choice = make_choice(paths.keys())

    if random.random() < 0.3:
        random_events()
        continue_path(choice = choice)
    else:
      print(paths[choice])
      
      if choice == 'a':
          path_a()

      elif choice == 'b':
        path_b()
      
      else:
        path_c()
        
def main():
    display_intro()
    forest_path()

if __name__ == "__main__":
    main()