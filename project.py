import sys
import cs50
import re
import time
from time import sleep


class Player:
    def __init__(self, name=None):
        self.name = name
        self.dislike = 0
        # teacher dislike of you -> tardies, rudeness, violence
        self.friends = 0
        self.smarts = 0
        self.strength = 0
        self.detention = 0
        self.happiness = 0

    def print_stats(self):
        print("Your stats: ")
        print(f"Name:       {self.name}")
        print(f"Detentions: {self.detention}")
        print(f"Friends:    {self.friends}")
        print(f"Energy:     {self.strength}")


if __name__ == "__main__":
    while True:
        current_player = Player()
        # print(current_player.detention)

        # class Me():
        # class thing? TODO

        # TODO player = Me
        # stats = print("stats: \nknowledge: ", smarts "dislike's: ", dislike "friendclass: ", friendclass)
        continue1 = input("Are you ready to continue? ")
        if continue1 == "no":
            continue
        else:
            pass
        # beginning story
        time.sleep(3)

        print("\nWelcome, to Birch High")
        time.sleep(1)
        name = input("What is your name? ")
        print(f"\nHello, {name}! You are a 10th grade student on the first day of school.\n")
        time.sleep(1)
        # delay time 1 seconds
        print("\nYou make it to school 3 minutes before the bell.\nYou told your friend you would give them a hug before school starts, but they're currently at the floor above your first class.")
        time.sleep(2)
        # delay time 2 seconds
        friendhug = input("Do you find your friend (a) or go straight to class? (b)\nAnswer: ")
        # boolean ???
        if friendhug.lower() == "a":
            current_player.dislike += 1
            current_player.friends += 1
            print("\nYour friend smiles at you - you made their day!\nYou rush downstairs to Math class and arrive 2 minutes late.\nThe teacher glares are you.")
        if friendhug.lower() == "b":
            print("\nYou made it to math class on time.\nYou sit down in the front row.")
        time.sleep(2)
        # delay time 2 second
        print("\nYour math teacher surprises the class with a pop quiz!")
        # math test begins
        answer1 = input("\n- Question 1: which number is equivalent to 3^(4)÷3^(2)\nAnswer: ")
        if int(answer1) == 9:
            # adding 1 to players' smarts
            # TODO why is it not writting correct
            current_player.smarts += 1
            print("Correct!")
        else:
            print("Incorrect")
        time.sleep(1)
        print("\nuh oh, the next question is multiple choice!")
        time.sleep(1)
        answer2 = input("\n- Question 2: If x*x-2x-35=0 then x=?\na = -35\nb = 2x^3\nc = -5\nd = 7\nAnswer: ")
        options = ['a','b','c','d']
        if answer2 == options[2]:
            # Correct answer
            print("Correct!")
            current_player.smarts += 1
        elif answer2 == options[3]:
            # Correct answer
            print("Correct!")
            current_player.smarts += 1
        else:
            print("Incorrect")
        time.sleep(2)
        print("The next question is a problem solving?! Yikes!")
        time.sleep(1)
        answer3 = input("\n- Question 3:  If the cost of a bat and a baseball combined is $1.10 and the bat costs $1.00 more than the ball, how much is the ball?\nAnswer: ")
        if answer3 == "0.10" or "$0.10" or "0.10$" or ".10":
            print("Correct!")
            current_player.smarts += 1
        else:
            print("Incorrect")
            pass
        time.sleep(1)
        print("Last one!")
        time.sleep(2)
        answer4 = input("\n- Question 4: If (0.2)x = 2 and log 2 = 0.3010, then the value of x to the nearest tenth is:\na = -10.0\nb = -0.5\nc = -0.4\nd = -0.2\ne = 10.0\nAnswer: ")
        if answer4 == "c":
            print("Correct!")
            current_player.smarts += 2
        else:
            print("Incorrect")
            pass
        time.sleep(2)
        foodorhist = input("\nFirst class is done! You have twenty minutes before your next class: English.\nYou forgot to study for your history test today, but you're also getting really hungry!\nDo you study in the break (1), or eat breakfast? (2)\nChoice: ")
        if foodorhist == "1":
            # studying in break adds smarts
            current_player.smarts += 1
        elif foodorhist == "2":
            # eating food adds strength
            current_player.strength += 1
        else:
            pass
        time.sleep(2)
        print("\n\nYou fall asleep halfway through English class from lack of sleep. The teacher gets annoyed and sends you to the principle's")
        # TODO change to function?
        principle1talk = input("\nDo you:\na) apologize profusely\nb) explain your lack of sleep in a logical way\nc) insult them\nd) fall asleep mid conversation\n\nChoice: ")
        if principle1talk.lower() == "a":
            print("The principle threatens to call your parents, but gives you one last chance")
        if principle1talk.lower() == "b":
            # explaining
            current_player.smarts += 1
            print("The principle understands you, and even lets you buy a coffee at the school cafe")
        if principle1talk.lower() == "c":
            print("The principle insults you back, then assigns you to detention at the end of the day\n")
            # add to detention
            current_player.detention += 1
        if principle1talk.lower() == "d":
            print("...")
        time.sleep(2)
        # MAIN CHOICE 1
        print("English class passes slowly, and now it's lunch!\n")
        lunchbreak = input("Do you want to eat on the sports field, where you will do sports and do homework, OR leave campus with the cool kids and raise your social status (it's low). \nDo you:\na) go to the field\nb) go out of school\nAnswer: ")
        # how spend lunchbreak
        if lunchbreak == "a":
            # cafeteria
            current_player.strength += 1
            # playing sports/getting excersize adds to strength
            print("Lunch went well, and the activity raised your spirits! Although you do end lunch sweaty...\nNext class up is history, whose teacher you hate\n")
            print("You feel really sweaty, and enter the class hesitantly.\nAs you begin the work, you notice a kid at the back of the classroom trying to look over at your work.")
            cheater = input("Do you:\na) call them out and report to teacher\nb) ignore them and continue your work\nc) scrap your original writting and copy off of the person in front of you\nd) stand up and adress them (potential fight)\nAnswer: ")
            # student is cheating on hw
            time.sleep(2)
            if cheater.lower() == "a":
                print("\nYou report the student to the teacher, but they get annoyed at you for interrupting the book they were reading, and make fun of you of being a try-hard and snitching. To your dismay, they make you restart your writing with a new prompt and only 20 minutes.")
                print("You manage to finish just in time, and feel extremely relieved as you leave the classroom. Outside the class door the student you reported starts to pick a fight with you.\nThey have 2 other friends with them, and the fight is clearly unfair.")
                # fight starts
                fightchoice = input("Do you\na) run away \nb) fight back\nAnswer: ")
                if fightchoice.lower() == "a":
                    # run away
                    print("You make it to the safety of your next class just in time - music class!")
                    current_player.smarts += 1
                    # smart decision = + 1 in smarts
                elif fightchoice.lower() == "b":
                    # fight back
                    print("You get beaten up... luckily, the principle saw the end of the fight, and gives the three students detention.\nUnfortunetely you have severe injuries and need to go to the nurse.")
                    current_player.strength -= 1
                    # severe injuries decrease strength
                    print("You make it to music class 5 minutes late, and get a tardy")
                    # increase in tardies/dislikes
                    current_player.dislike += 1
                # main music class
                instrumentchoice = input("\nThe teacher is letting everyone chose the instruments they will be learning for the year. The options are:\n a) bassoon - which you were forced to learn for 4 years\n b) drums - all of your friends are taking that instrument\nAnswer: ")
                if instrumentchoice.lower() == "a":
                    # bad instrument
                    print("the class is impressed by your guitar skills! You remember why you hated the instrument.")
                    # decrease in happiness by playing least favorite instrument
                    current_player.happiness -= 1
                    # prioritizing smarts/school results
                    current_player.smarts += 1
                if instrumentchoice.lower() == "b":
                    # bad studying
                    print("you and your friends have a fun class! You don't get any work done.")
                    # happy to play favorite instrument
                    current_player.happiness += 1
                    # having fun with friends
                    current_player.friends += 1
                time.sleep(2)
            if cheater.lower() == "b":
                print("You submit your work on time, and feel proud of your work. You worry if you will get called out for copying the other students work...")
                print("You head to music class. You decide to take the bassoon because you have prior experience with it. Your teacher asks you to play a song for possible extra points.")
                prinsong = input("\nDo you (a) attempt to impress them with an extremely difficult song that you may have forgotten or (b) play a simple song that the whole class emjoys and knows?\nAnswer: ")
                if prinsong == "a":
                    # smart decision to challenge yourself
                    current_player.smarts += 1
                    # happy to be challenged
                    current_player.happiness += 1
                    print("You're happy with your descision! You manage to finish the song with only a few minor mistakes, and you see the teacher make a note about you skills.")
                if prinsong == "b":
                    print("Your friends enjoy the song and sing along! You're happy with your descision!")
                    # have fun and are happy
                    current_player.happiness += 1
                    # choice includes friends
                    current_player.friends += 1
                time.sleep(2)
            if cheater.lower() == "c":
                print("You manage to copy the main ideas of the person in front of you. You also manage to submit it a few seconds before them.")
                print("At the end of the class, the teacher asks you, the student sitting in front of you and the student sitting behind you to stay behind.")
                print("The teacher shows the 3 similar essays and asks for an explanation.")
                time.sleep(1)
                cheatingcaughtchoice = input("\nDo you a- admit and apologize, b- blame both other students for cheating off of you, c- stay silent\nAnswer: ")
                if cheatingcaughtchoice.lower() == "a":
                    print("The teacher appreciates you being honest, but sends you and the student behind you to the principle. The principle gets annoyed.")
                    current_player.smarts += 1
                    # smart to be honest
                    current_player.dislike += 1
                    # returning to principle adds dislike
                if cheatingcaughtchoice.lower() == "b":
                    print("The teacher doesn't believe you and gets very mad.")
                    # teacher is very mad
                    current_player.dislike += 2
                if cheatingcaughtchoice.lower() == "c":
                    print("The other student blame each other, and you all end up in a heated debate, leaving you 10 minutes late for your next class.")
                    # teacher gets annoyed
                    current_player.dislike += 1
            if cheater.lower() == "d":
                print("You take a swing at the students' head. You assumed they wouldn't be strong, but they spin and punch you across the mouth, causing you to go flying.\nThe teacher pushes in between you, right as you qttempt an uppercut.\nThe teacher is furious.\nYou are given 5 days worth of detention!")

        if lunchbreak.lower() == "b":
            current_player.friends += 1
            print("You all leave campus and go to a nice cafe.\nYou spend time talking, until everyone says they need to go outside because a friend is coming, and ask you to keep the table.\n After 10 minutes of waiting, you check outside to see everyone left!\nYou realize you're running 5 minutes late for the next class, and have no idea where you are.")
            time.sleep(2)
            print("Your phone tells you that the school is 10 minutes away by walking, and 2 minutes by car. You have $10, but because everyone left, you hav to pay the bill.")
            time.sleep(2)
            print("The bill is exactly $9.99, and the uber would cost $2... Do you:")
            splitbillschool = input("\na) Pay for the bill and jog back to school\nb) Take the Uber and leave one of your 'friends' numbers on the bill\nc) Grab the Uber and run (leaving the cafe with no explanation)\nChoice: ")
            if splitbillschool.lower() == "a":
                print("\nYou run out of the restaurant, but halfway to school you get an extreme stitch! You sit on the curb for a minute trying to catch your breathe as a car pulls up beside you.")
                print("\nA 50 year old steps out of the car, and offers you candy and a ride with them...")
                time.sleep(1)
                takecarstranger = input("Do you\na) agree and get in\nb) STRANGER DANGER\nAnswer: ")
                if takecarstranger.lower() == "a":
                    print("You've been kindapped. The end.")
                    backtobegining = input("If you would like to restart the game, type Y\nAnswer: ")
                    if backtobegining.lower() == "y":
                        continue
                    else:
                        sys.exit
                if takecarstranger.lower() == "b":
                    print("You run away from them with even more energy and make it to school in under 5 minutes.")
                    print("You get a tardy to school, but feel happy that you maintained a moral code")
                    current_player.smarts += 1
                    # return to school because of safe decision
                    current_player.happiness += 1
                    # happy with result
            if splitbillschool.lower() == "b":
                print("You leave the cafe, and make it to school in a minute. The teacher excuses your slight tardy!")
                time.sleep(1)
                print("Your friend is called up to present a project you know that neither of you did.\nDo you:")
                musicclassfriendforgot = input("\na) go onstage and embaress yourselves together\nb)stay silent and hope for the best\nAnswer: ")
                if musicclassfriendforgot.lower() == "a":
                    # prioritizing being with friend
                    current_player.friends += 1
                    # bad impression from teacher
                    current_player.smarts -= 1
                    print("You and your friend fail together, and your teacher writes a bad mark on her paper..")
                if musicclassfriendforgot.lower() == "b":
                    print("Your friend does horribly, but your reputation with the teacher and classmates has been maintained")
                    # no result
            if splitbillschool == "c":
                print("The cafe owners run after you! The Uber drives you away, and you can hear their foul language fading into the distance.")
                time.sleep(1)
                print("You feel guilty. Your music teacher excuses your tardy, but 5 minutes before class ends, the police show up outside your class.")
                time.sleep(1)
                print("They confront you about not paying the bill.\nYou have no choice but to assume responsibility...")
                # bad decision -> police
                current_player.smarts -= 1
                # dislike from teacher
                current_player.dislike += 1
        time.sleep(2)
        print("\nThe school day is FINALLY over.\n")
        if current_player.dislike == 2:
            current_player.detention += 1
            # for each set of 2 dislikes, 1 will be added to detentions
        else:
            pass

        current_player.print_stats()

        if current_player.detention > 2:
            print("There are only 2 days left in the week, and you have over 2 detentions.\nYou are EXPELLED")
            backtobeginings = input("If you would like to restart the game, type Y\nAnswer: ")
            # choice to return to beginning of game
            if backtobeginings.lower() == "y":
                continue
            else:
                sys.exit

        else:
            if current_player.friends > 2:
                print("Congratulations! You have over 3 friends.")
                continue
            if current_player.smarts > 3:
                print("Congratulations! You are smart.")
                continue
            if current_player.strength > 1:
                print("Congratulations! You're ended the day off feeling strong.")
                continue
            if current_player.happiness > 4:
                print("Congratulations! You've got a big brain!")
                continue

    # END DAY FOR ALL CHOICES, SHOW STATS IF HAVE DETENTION, IF HAVE NO FRIENDS, IF ___

        # if dislike == 6:
        # print("You are expelled!")
