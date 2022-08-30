from random import random
import random


MAXNAME = 10

class pref:
  def ONLY_OG():
    return [1,0,0,0]

  def ONLY_OO():
    return [0,1,0,0]

  def ONLY_OPENING():
    return [1,1,0,0]

  def NO_PREF():
    return [1,1,1,1]

class Debater:
     def __init__(self, id, name, can_judge = False,  exp_lv = True, can_iron = False, prefer = pref.NO_PREF()):
         self.id = id                                 # Unique debater id 
         self.name = name                             # Name of debater for printing
         self.j = can_judge                 # Can judge or not, default: False
         self.e = exp_lv
         self.i = can_iron
         self.prefer = prefer

member_dict = {}
member_dict["Danniel"] = Debater(57501,"Danniel")
member_dict["Guy"]     = Debater(57502,"Guy")
member_dict["Rong"]    = Debater(57503,"Rong")
member_dict["Simon"]   = Debater(57504,"Simon")
member_dict["Martin"]  = Debater(57505,"Martin")
member_dict["Anne"]    = Debater(57506,"Anne")
member_dict["Rijkman"] = Debater(57507,"Rijkman")
member_dict["Willem"]  = Debater(57508,"Willem")
member_dict["Luka"]    = Debater(57509,"Luka")
member_dict["Leon"]    = Debater(57510,"Leon")
member_dict["Effe"]    = Debater(57511,"Effe")



def print_member(dict : Debater, mode = None):
    if mode is None:
        print("  ID ",' | ',"  NAME     |", )
        for dbter in dict:
            id = dict[dbter].id
            name = dict[dbter].name 
            name += " " * (10-len(name))
            print(id,' | ',name,"|" )
    else:
        print("  ID "," |   NAME      |","JUDGE |","IRON  |" )
        for dbter in dict:
            id = dict[dbter].id
            
            name = dict[dbter].name 
            name += " " * (10-len(name))
            judge = None
            if dict[dbter].j is True:
                judge = "  J   |" 
            else:
                judge = "      |"
            
            if dict[dbter].i is True:
                iron = "  I   |" 
            else:
                iron = "      |"

            print(id,' | ',name,"|" , judge, iron)
        print("*New* means that this debater is inexperienced, plz add E flag if this is not intended")
        print("--- Press F to pay respect ---")

def read(participants,filename = '20220815.txt'):
    
    with open(filename) as f:
      lines = f.read().splitlines()

    for line in lines[5:]:
        x = line.split(" ", -1)
        if x[0] in member_dict.keys():
            participants[x[0]] = member_dict[x[0]]
        else:
            participants[x[0]] = Debater("*NEW*",x[0], exp_lv = 0)
        if len(x) > 1:
            exprinece = False
            judge = False
            iron = False
            for flag in x[1:]:
                if flag == 'J':
                    judge = True
                if flag == 'E':
                    exprinece = True
                    if participants[x[0]].id == "*NEW*":
                        participants[x[0]].id = "*OLD*"
                if flag == 'I':
                    iron = True
            participants[x[0]].j = judge
            participants[x[0]].e = exprinece
            participants[x[0]].i = iron
    print("read from ",filename)

class Room:
    def __init__(self,rm_id, FULL_BP):
        self.rm_id = rm_id
    
        self.BP = (4 if FULL_BP == True else 2)

        self.iron = 0
        self.new = 0
        self.exp = 0

        self.new_member = []
        self.exp_member = []
        self.iron_member = []

        self.seat = [  ""  for y in range(self.BP*2) ] 
    
    def add_member(self, member):
        if member.i:
            self.iron += 1
            self.iron_member.append(member)
            return

        if not member.e:
            self.new += 1 # the count of new member + 1
            self.new_member.append(member)
            return
        else:
            self.exp += 1
            self.exp_member.append(member)
            return
        
    
    def assigned_member(self):
        # Assuming we are getting correct number of ppl
        # Arrange seat randomly

        random.shuffle(self.iron_member)
        random.shuffle(self.new_member)
        random.shuffle(self.exp_member)

        start = random.randint(0, self.BP - 1)

        for i in range(self.BP):
            self.pop_pool( (start+i) % self.BP )
    
    def pop_pool(self,i):
        # pop one member for one of the three pools and return the
        # name of the string
        if self.iron > 0:
            self.seat[i*2] = self.iron_member.pop().name
            self.iron -= 1
            return
        
        if (self.exp > 0) and (self.new > 0)  :
            
            self.seat[i*2]   = self.exp_member.pop().name
            self.seat[i*2+1] = self.new_member.pop().name

            self.new -= 1
            self.exp -= 1
            return
        
        if (self.exp > 0) and (self.new == 0)  :
            self.seat[i*2]   = self.exp_member.pop().name
            self.seat[i*2+1] = self.exp_member.pop().name

            self.exp -= 2
            return
        
        if (self.exp == 0) and (self.new > 0)  :
            self.seat[i*2]   = self.new_member.pop().name
            self.seat[i*2+1] = self.new_member.pop().name

            self.new -= 2
            return
    
    def display(self):
        for i in range( self.BP * 2 ):
            self.seat[i] += " " * (10-len(self.seat[i]))
        print("================== Room",self.rm_id,"=================")
        print("======= OG =======        ======= OO ======")
        print("    ",self.seat[0],"               ",self.seat[2])
        print("    ",self.seat[1],"               ",self.seat[3])
        if self.BP == 4:
            print("======= CG =======        ======= CO ======")
            print("    ",self.seat[4],"               ",self.seat[6])
            print("    ",self.seat[5],"               ",self.seat[7])           
