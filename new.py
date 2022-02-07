player_name=input("What is your name?".upper())

#Knight comes from Swampy:

text_one=("Thanking him you ride yet again for three days and three nights and reach the base of the mountain.\n A Troll stands there guarding an entrance to a cave.\n'Who dare comes near' shouts the troll.\n'I am a Knight'you reply and tell him you came all this way to save the princess.\nI will give you my golden nuggets if you can answer my riddle he says.")

#for char in text_one:
    #sys.stdout.write(char)
    #sys.stdout.flush()

score = 0
golden_nuggets= 0

# Question:
print(" 'I speak without sound, but you see what I say.\n Im borrowed for free, but some chose to pay.\n My truth is for learning, my lies are for play. \nWhat am I?" '')

#Answer:


def game():
    def troll_path(): 
        global score,golden_nuggets
        answer_1 = input("a)Wind\nb)Stone\nc)Book\nd)Ghost\n:")
        
        if answer_1.lower() == "a":
            print(f"Sir {player_name} that is a wrong answer ")
            golden_nuggets += 25   
            print(f"Current score:{golden_nuggets}")
            next_stage()    
        elif answer_1.lower()=="b":
            print(f"Sir {player_name} that is a wrong answer ")
            golden_nuggets += 25   
            print(f"Current score:{golden_nuggets}")
            next_stage()     
        elif answer_1.lower()=="d":
            print(f"Sir {player_name} that is a wrong answer ")
            golden_nuggets += 25   
            print(f"Current score:{golden_nuggets}")
            next_stage()
        elif answer_1.lower() == "c":
            print(f"You are correct Brave Kinght Sir {player_name} ")
            golden_nuggets += 100
            print(f"Current score:{golden_nuggets}")
            next_stage()      
        else:
            print("Please make a selection")
            troll_path()

    def next_stage ():

        print(" 'Take this gold and go inside the cave and climb to the top of the tower, where the Evil Elf is with your princess.'  Says the Troll.\n He lets you pass him inside and you climb up the mountain to reach the top.\nThere on the top lies a tower........You see the Evil Elf....!!!! ")

    troll_path()
game()
