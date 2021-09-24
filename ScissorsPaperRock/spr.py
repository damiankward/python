import random

fight = {"s":["p","r"],"p":["r","s"],"r":["s","p"]}
                            #list[0] == win condition, list[1]== lose condition


#prompt the user to choose their weapon
user = input("Choose! [s]iz or [p]aype or [r]ok!? ")
print("You have chosen: " + user)

#randomly chose comp's weapon
comp = random.randint(0,2)
#fix comp
if comp == 0:
    comp = "s"
elif comp == 1:
    comp = "p"
else:
    comp = "r"
print("Computer has chosen: " + comp)
 
for weapon in fight:
    if weapon == user:
        if comp == (fight[weapon][0]):
            print(user + " beats " + comp + "! you win!")
        elif comp == (fight[weapon][1]):
            print(comp + " beats " + user + "! you lose!")
        else:
            print("Draw! A well matched fight!")
