import streamlit as st
import time
import random

def display_intro():
    st.write("Welcome to the Challenging Text Adventure Game!")
    st.write("You find yourself in a dark and treacherous forest. Your survival depends on your choices.")
    st.write("Make the wrong decisions, and you may never escape this forest. Good luck!\n")

def make_choice(options):
    choice = st.selectbox("Choose an option", options)
    return choice

def encounter_wild_animal():
    st.write("As you walk through the forest, you encounter a wild animal!")
    time.sleep(1)
    st.write("It's a fierce wolf!")
    time.sleep(1)
    st.write("What do you want to do?")
    choice = make_choice(['Fight the wolf', 'Try to run away'])
    if choice == 'Fight the wolf':
        st.write("You decide to fight the wolf!")
        time.sleep(1)
        st.write("You grab a stick nearby and bravely face the wolf.")
        time.sleep(2)
        if random.random() < 0.5:
            st.write("Incredibly somehow, you manage to defeat the wolf! You can continue your journey.")
        else:
            st.write("The wolf proves to be too strong for you. You barely escape with your life.")
    else:
        st.write("You try to run away from the wolf.")
        time.sleep(2)
        if random.random() < 0.3:
            st.write("You manage to escape from the wolf and continue your journey.")
        else:
            st.write("The wolf catches up to you and attacks. You are injured, but you manage to scare it away.")

def find_useful_item():
    st.write("While exploring the forest, you find a hidden stash!")
    time.sleep(1)
    st.write("Inside the stash, you find a potion of healing.")
    time.sleep(1)
    st.write("This potion can help you in your journey.")
    time.sleep(1)
    st.write("You add the potion to your inventory.")

def solve_environmental_riddle():
    st.write("You come across an ancient stone monument with mysterious inscriptions.")
    time.sleep(1)
    st.write("The inscriptions seem to be a riddle.")
    time.sleep(1)
    st.write("Solve the riddle to proceed.")
    time.sleep(1)
    answer = st.text_input("Your answer")
    if answer.lower() == "friend":
        st.write("Correct! The stone monument trembles, and a hidden passage is revealed.")
    else:
        st.write("Incorrect answer. You must ponder the riddle further to proceed.")

def discover_secret_location():
    st.write("While exploring the forest, you notice a strange pattern in the trees.")
    time.sleep(1)
    st.write("Following your instincts, you investigate further and find a hidden cave.")
    time.sleep(1)
    st.write("Inside the cave, you discover a secret chamber.")
    time.sleep(1)
    st.write("The chamber contains a valuable treasure!")

def random_events():
    events = [encounter_wild_animal, discover_secret_location, solve_environmental_riddle, find_useful_item]
    random.choice(events)()

def path_a():
    st.write("You can cross the river (a) or follow it downstream (b).")
    choice_a = make_choice(['Cross the river', 'Follow downstream'])
    if choice_a == 'Cross the river':
        st.write("You try to cross the river but get swept away by the current. Game Over!")
    else:
        st.write("You follow the river downstream and find a hidden waterfall. You can climb it (a) or go around it (b).")
        choice_waterfall = make_choice(['Climb the waterfall', 'Go around'])
        if choice_waterfall == 'Climb the waterfall':
            st.write("You successfully climb the waterfall, but you encounter a dangerous creature on the other side.")
            time.sleep(2)
            st.write("You have two allies from Clash of Clans, P.E.K.K.A and Wizard, to help you defeat the creature.")
            choice_ally = make_choice(['Choose P.E.K.K.A to wage war', 'Choose Wizard to wage war'])
            if choice_ally == 'Choose P.E.K.K.A to wage war':
                st.write("You choose P.E.K.K.A, and together you defeat the creature and successfully escape.")
                st.write("Now both of you apply to the next Monster Inc. movie as Sully and boo.")
                st.write("You win!")
            else:
                st.write("You choose Wizard, but the creature proves too powerful and transforms you into a dwarf.")
                st.write("As a dwarf you don't have the height to play the game.")
                st.write("Game over!")
        else:
            st.write("As you go around, you found Bilu, the E.T.")
            st.write("You can't handle all the knowledge and die.")
            st.write("Game over!")

def path_b():
    st.write("You enter the cave and discover a treasure chest guarded by an albino dragon.")
    st.write("You have two options to defeat the dragon:")
    choice_dragon = make_choice(['Use an electro dragon lord of dragons', 'Use a little sword'])
    if random.random() < 0.3:
        random_events()
    else:
        if choice_dragon == 'Use an electro dragon lord of dragons':
            st.write("You summon the electro dragon lord of dragons, which defeats the albino dragon.")
            st.write("As a reward, the dragon transforms you into an electrified albino.")
            st.write("You win!")
        else:
            st.write("You attempt to fight the dragon with the little sword, but it's not enough. The dragon breathes fire on you.")
            st.write("You died horribly, jackass.")
            st.write("Game over!")

def path_c():
    st.write("You enter the mysterious house. It's dark inside.")
    choice_house = make_choice(['Explore the house', 'Leave immediately'])
    if random.random() < 0.3:
        random_events()
    else:
        if choice_house == 'Explore the house':
            st.write("You explore the house and discover two different paths:")
            house_choice = make_choice(['Talk to Martina Oliveira from only fans', 'Get a drug that could help'])
            if house_choice == 'Talk to Martina Oliveira from only fans':
                st.write("She says: 2 dollars or a mystery box?.")
                st.write("You do not have time to answer, a big witch suddenly appears.")
                st.write("You just turn around with a hard dick and...")
                st.write("You Win, fatality!")
            else:
                st.write("You took an insane amount of molly.")
                st.write("You enter in a giant island and get lost in its vastness.")
                st.write("Game over.")
        else:
            st.write("When you are leaving the house, you fall into a Saw movie like trap and die!")
            st.write("Game over!")

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
      st.write(paths[choice])
      
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