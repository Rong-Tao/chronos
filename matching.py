# Taking the participant dict

# Matching a standard 8 slot BP with the lowest COST
# Cost is 0 if an experienced is assigned to a slot
# Cost is 1 both slot is filled with inexperienced debater
# Cost is 10 if a slot is unfilled
# Cost is 10 if more than 2 people is assigned to the same team
# Cost is 10 if less than 1 judge in 1 room
# Cost is 5 if 1 iron person (just for anne to use iron person) exist

# Prioity 
# assign inexp with exp >> 
# assign 2 inexp in the same slot >>
# iron person exist >>
# slots unfilled,


# First calc the possible number of people
from itertools import count
from math import ceil, floor
import random
from tkinter.messagebox import NO

from lib import Room

def match(dict):
    possible_max = 0
    possible_jug = 0
    for participant in dict:
        if dict[participant].j :
            possible_jug += 1
        elif dict[participant].i :
            possible_max += 2
        else :
            possible_max += 1

    print("","We can have",possible_max,"Debaters and",possible_jug,"judges","*ironperson counts as 2 people\n") 
    # Again using iron person to pay respect to anne
    

    modnum = possible_max // 4
    print("We can have",floor(modnum/2),"full BP and",ceil(modnum/2)-floor(modnum/2),"half BP")  
    print("TYPE -a to allocate, adjust the txt file if this is not intended")
 
def allocate(dict):
    possible_max = 0
    possible_jug = 0
    for participant in dict:
        if dict[participant].j :
            possible_jug += 1
        elif dict[participant].i :
            possible_max += 2
        else :
            possible_max += 1

    modnum = possible_max // 4    

    fullbp_num = floor(modnum/2)
    halfbp_num = ceil(modnum/2)-floor(modnum/2)

    iron = 0
    new = 0
    exp = 0

    new_member = []
    exp_member = []
    iron_member = []

    for participant in dict:
        member = dict[participant]
        if member.i:
            iron += 1
            iron_member.append(member)
            continue

        if member.j:
            continue

        if not member.e:
            new += 1 # the count of new member + 1
            new_member.append(member)
            continue
        else:
            exp += 1
            exp_member.append(member)
            continue
    
    random.shuffle(iron_member)
    random.shuffle(new_member)
    random.shuffle(exp_member)
    
    

    Rooms = [None for i in range(fullbp_num+halfbp_num)]

    for i in range(fullbp_num+halfbp_num):
        MAXCOUNT = None
        if i == fullbp_num:
            Rooms[i] = Room(i+1,False)
            MAXCOUNT = 4
        else:
            Rooms[i] = Room(i+1,True)
            MAXCOUNT = 8

        count = 0 

        while count < MAXCOUNT:

            if iron > 0:
                Rooms[i].add_member(iron_member.pop())
                iron -= 1
                count += 2
                continue
            
            if (exp > 0) and (new > 0)  :
                Rooms[i].add_member(exp_member.pop())
                Rooms[i].add_member(new_member.pop())
                new -= 1
                exp -= 1
                count += 2
                continue
            
            if (exp > 0):
                Rooms[i].add_member(exp_member.pop())
                exp -= 1
                count += 1
                continue

            if (new > 0):
                Rooms[i].add_member(exp_member.pop())
                new -= 1
                count += 1
                continue


    
    for _Room in Rooms:
        print("\n")
        _Room.assigned_member()
        _Room.display()
        print("\n")