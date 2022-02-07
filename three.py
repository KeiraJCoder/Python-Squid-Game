import random
import time
def main():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nafter a long, treacherous journey, headed west - you find a desert island..\n\nout of sheer desperation, you begin to scour the island for any signs of previous activity or discarded or washed up items that may be of any use..\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    def get_map():
        rand_num = random.randint(1,4)
        user_key = int(input("you find a mysterious box, you decide to test your lockpicking skills to try to reap the treasure within.. \nbeing adept in such methods, you know to always use the right tools for the job..\nwhich lockpick do you choose?\n\n1.\n2.\n3.\n4.\n\n: "))
        
        def treasure_chest (user_key,rand_num):

            if user_key == rand_num:
             (print (f"\n{user_key} is correct.. \n\nyou have aquired a mysterious map to a key to an unknown lock.."))
            else:
             for i in range (1):
                (print (f"\n{user_key} is incorrect..\n\nthe correct answer is {rand_num}..\nyou have 30 seconds to decide.. \nwould you like to try again?"))
                time.sleep(3)
                # 5 second wait - change
        treasure_chest(user_key, rand_num)
        if user_key != rand_num:
            restart = (input("\nready?"))
            if restart == " ":
                get_map()
            else:
                get_map()
        
        if user_key == rand_num:
            print (input("\n upon inspecting the map closely, you see what appears to be the location of the island on which you currently languish..\n\n  further still to the west, located close to the coast, is a clear marker in the shape and image of a gold coin\n\n   in your mind.. this can only mean one thing..\n\n[enter]"))
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print ("\nyou arrive at a port, and as you step off your ship, you see a lone fellow traveller, looking inebriated and worse for wear..\n")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        def dock():

            
            answer = str (input("you decide whether to:\n \na) interact with the stranger, \nb) return to board the ship, or \nc) remain stationary while you plot your course.. \n\n"))

            if answer == 'a':
                print ("you choose to speak with the mysterious stranger \n")
            elif answer == "b":
                print ("you choose to return to your ship\n")
            elif answer == "c":
                print ("you choose to remain stationary while you plot your course..\n")
            else:
                print ("please choose interact with stranger, board ship or remain\n") # <-- fix this <--maybe randomize the outcome rather than restart sequence

            # hopefully next stage of port..    

            # for sake of easiness doing limiting choices first then opening the stranger sequnce later, for now..

            if answer == 'b':
                answer = str (input("whilst docked, you ponder upon your best course of action\n"))
                restart = input ("go back?")
                if restart == '':
                    dock()

                else:
                    dock()    
                # this need linking to other options - dont forget this! // update // semi fixed // find more interesting loop back..

            if answer =='c':
                answer = str (input("after some rest, your vision is clearer and you are ready to decide how to proceed..\n"))
                restart = input ("ready to proceed?")
                if restart == '':
                    dock()
                else:
                    dock()

            # also needs linking - please fix this! // update // semi fixed // find more interesting loop back..


            if answer == 'a':

                answer = input("what next?.. \n\na) quietly try to get their attention, \nb) shout them as you approach, \nc) you clear your throat to announce your presence as you gingerly approach.. \n\n")

        # ok so this is hopefully going to be the stranger section..

                if answer == 'a':
                    print ("you failed to rouse them from their intoxicated haze")
                elif answer == 'b':
                    print ('they become belligerent and offensive in their drunken state')
                elif answer == 'c':
                    print ('you have their full attention, they ask how they may assist you in your travels..')
                else:
                    print("it apperars you also may be sozzled, please select again..")

                    if answer == 'a':
                        print ("apparently unsure of yourself, you retrace your steps back..")
                    restart = input ("ready to proceed?")
                    if restart == '':
                        dock()
                    else:
                        dock()
            elif answer =='b':
                    print ("somewhat on the defensive, you retreat to the safety of your ship")
                    restart = input ("ready to proceed?")
                    if restart == '':
                        dock()
                    else:
                        dock()
            elif answer =='c':
                print ("you decide to utilize this good fortune to attempt to advance your journey")
            else:
                print ("pay attention this time matey")
                restart = input ("ready to have another go?")
                if restart == '':
                    dock()
                else:
                    dock()

            if answer == 'c':
            
            # hopefully working and interesting progression of dialogue..
            
             answer = input("the stranger enquires as to your origin and reason for docking:\n \na) you decide that disclosing the nature of your journey to a drunken ne'er-do-well may result in perilous confrontation, so lie and say youre a cleric spreading tomes of faith. \nb) you inform the drunkard that you came across a map and key that have led you here. \nc) you tell the intoxicated transient that you are nomadic and at sea in search of great fortune.\n\n")
            
            if answer == 'a':
                print ("\nyour dishonesty gets you nowhere, more precisely, back to your ship to start over..")
                restart = input ("ready to proceed?")
                if restart == 'yes':
                 dock()
                else:
                 dock()
            elif answer == 'b':
                print ("\nperplexingly indifferent to your supposed treasure quest the stranger points you in the direction of a local tavern.. \nwith instructions to speak with the barkeep, who is known to be something of a character among the locals..\n")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
                print("as you squint into the dark distance, you make out the name of the tavern from its sign.. \nTHE GOLD COAST TAVERN..")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")   

            elif answer == 'c':
                print("\nalthough initially slightly curious of your intentions, his suspicions are immediately quelled and decides to inform you of a local tavern where you may wish to converse with the locals\n")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("as you squint into the dark distance, you make out the name of the tavern from its sign.. \nTHE GOLD COAST TAVERN..")   
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            else:
                print ("\nhe doesnt seem to like the cut of your jib, and quickly loses interest in you and return to their previous semi-slumbering state of imbibement..\n")
                restart = input ("ready to try again?")
                if restart == 'yes':
                 dock()
                else:
                 dock()
                
            if answer == 'b':
                        print("\nyou see the lights of a tavern that looks warm and inviting..\n")
                        # check if this breaks it
            elif answer =='c':
                        print("\nthe enticing warmth of the tavern beckons you..")
            else:
                    print ("better luck next time..\n")

            answer = str(input("\npress to continue..\n"))
            if answer == '':
                print ("\nsights now set firmly on the tavern, and citizens therein, curiousity draws you nearer..\n")
            else:
                ("\nsights now set firmly on the tavern, and citizens therein, curiousity draws you nearer..\n")

            def o_tavern():
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print ("you stand outside the tavern, equally weary and curious you decide whether to..")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")  
                answer = str (input("\na) enter the tavern.. or.. \nb) peek through the window \n\n: "))

                if answer == 'a':
                    print ("\nentering the tavern..")
                elif answer == 'b':
                    print ("\nyou peek through the window, all looks friendly and cheerful..")
                else:
                    print ("\nyou remain nervously at the entrance to the tavern..")

                if answer != 'a':
                    answer = str(input("\nyou feel assured that you are entering a safe and friendly place\n"))
                    restart = input ("\nback to tavern entrance..") 
                    if restart == " ":
                        o_tavern()
                    else:
                        o_tavern()

                if answer == 'a':
                 print ("\nyou feel the eyes of strangers follow you as you approach the bar keeper..\n")
        
                answer = str(input("press to.. \na) initiate introduction with person tending bar..\nb) turn and exit the tavern\n: "))

                if answer == 'a':
                    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print ("with a confused expression over his face, the barkeep enquires..")
                    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                elif answer == 'b':
                    restart = input("exiting the tavern..")
                    if restart == " ":
                     o_tavern()
                    else:
                     o_tavern()

                def game(): 

                    answer = str (input("\n ..be ye?\n \na) lad, \nb) wench ..or.. \nc) otherwise.. \n\n: "))
                    if answer == 'a':

                            name = input ("\nwhat be your name laddy? :\n")

                    elif answer == 'b':

                            name = input ("\nwhat be your name wench? :\n")
                    
                    elif answer == 'c':

                        name = input ("well whether ye be..\nAgender,Androgyne,Androgynous,Bigender,Cis,\nCisgender,Cis Female,Cis Male,Cis Man,Cis Woman,Cisgender Female,Cisgender Male,Cisgender Man"
                        "\nCisgender Woman,Female to Male,FTM,Gender Fluid,Gender Nonconforming,Gender Questioning,\nGender Variant,Genderqueer,Intersex,Male to Female,MTF,Neither,Neutrois,Non-binary"
                        "\nOther,Pangender,Trans,Trans*,Trans Female,Trans* Female,Trans Male,Trans* Male,Trans Man,\nTrans* Man,Trans Person,Trans* Person,Trans Woman,Trans* Woman,Transfeminine"
                        "\nTransgender,Transgender Female,Transgender Male,Transgender Man,Transgender Person,\nTransgender Woman,Transmasculine,Transsexual,Transsexual Female,Transsexual Male"
                        "\nTranssexual Man,Transsexual Person,Transsexual Woman or Two-Spirit \n..welcome to ye, now state ye name.. \n\n")

                    else:
                            name = input("\noh a smarypants ay? just stick to the script rapscallion and state your name..\n")
                    def games_start():
                        print (f"\nbe ye able to guess the word which i be thinkin', then maybe i'll point ye in the right direction, whadd'ya say {name}? have ye the minerals?\n")

                        answer = str (input("\nWell have ye? \na: no\nb: yes \n: "))

                        if answer == 'a':
                            print ("\nahh ye coward is ye? have some heart..\n")

                        # elif answer != str:
                        #     print ("\nhuh? well i'll just that as a yes then..")

                        elif answer == 'b':
                            print ("\ngreat, here we go then.\n")

                        else:
                            print ("\ngreat, here we go then..\n")

                        # WHERE THE GAME STORES WORDS

                        word_list = [
                        ("compass"),("crew"),("deckhands"),("eyepatch"),("firstmate"),("galleon"),("gangplank"),("gold"),("gunpowder"),("\nhighseas"),("jewels"),("keel"),("landho"),("landlubber"),("LongJohnSilver"),("mutiny"),("nautical"),("\nnavigate"),("overboard"),("parley"),("Xmarksthespot"),("YellowFever"),
                        ("parrot"),("pegleg"),("pillage"),("pirate"),("\nplank"),("plunder"),("ransack"),("ruthless"),("sailor"),("scallywag"),("scurvy"),("\nshipmate"),("shivermetimbers"),("shore"),("skullbones"),("spoils"),("swabthedeck"),("treasure"),("treasureisland"),("vessel"),("villain"),("walktheplank"),

                        ]

                        # WHERE THE GAME PULLS WORDS FROM

                        random_word = random.choice(word_list)

                        guesses = ''

                        turns = 12

                        while turns > 0:

                            failed = 0

                        # THE RULES FOR THE WORD GAME

                            for char in random_word:

                                if char in guesses:
                                    print (char)

                                else:
                                        print ("_")

                                        failed += 1

                        # FIRST PART OF THE ACTUAL GAME..

                            if failed == 0:
                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                print(f"\nCongratulations matey.. You've bested me, the word i was thinking of was {random_word} heres the directions to the east, but.. BEWARE THE KRAKEN!! ..Travel At Ye Own Peril\n")
                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            if failed ==0:
                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                print("\n\nbefore you depart, the barkeeper asks you for the map, looking rather suspiciously chipper considering his recent defeat, he marks an 'X' near the bottom of your map and slides it back across the bar, with a rusty key resting atop..")
                                print("..so it appears you've exhausted all reasonable options in the western territories..\n..if the recently befriended barkeep is to be believed, perilous danger awaits you in the east..")
                                print("and to the south is a bounty of unknown value.. could this be a trap? could this be the score of a lifetime?\nor maybe just a tale-worthy adventure, the likes of which very few sea faring travellers stumble across in a whole lifetime..\n\n")
                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
                                break

                            guess = input("\nguess a letter:\n\n\n")

                            guesses += guess

                            if guess not in random_word:

                                turns -= 1

                                print (f"\nUnlucky young scallywag {name}")

                                print ("\nYou have", + turns, 'more guesses\n')

                            if turns ==0: 
                                restart = (input("You lose, try again young buccaneer.."))
                                if restart == "":
                                 games_start()
                                else:
                                    games_start()  
                            
                                
                    games_start()
                              
                game()



            o_tavern()
        dock()
    get_map()
main()