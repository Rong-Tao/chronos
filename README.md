# E.S.D.A Chronos Room Allocation Software

This room allocation software is created by Rong Tao, sixth board of ESDA, Chronos
# Preparation of the txt file

### Add one name per line
### If this name is already in the database, the documented parameters will be used. If it is new to the database, this member will be considered an inexperienced member:
`Rong`
### Add a J flag after the name if he is a judge: 
`Rong J`
### Add a I flag after the name if he is an iron man:
 `Rong I`

### Add a E flag after the name if he is an undocumented member but with experience:
 `Rong E`

# Procedure
## Step 0
Run `Runthis.py` to open the REPL

## Step 1
Type command `read` in order to read from txt file

## Step 2
Type command `-m` to match the number of rooms, this command does not do anything in the background, but shows how many rooms will be generated

## Step 3
Type command `-a` to see the room allocation, this step can be done infinitely

# More
Type -h for all possible commands

# Possible Improvements
### 1. Automate the judge selection and iron man generation process
### 2. rewrite the read txt file so it would take into a file name instead of "20220815.txt"
### 3. Better room generation insteaf of Mod by 4
### 4. Allow customizable options like leave early and prefered teammates (Implemented in Debater class already)
