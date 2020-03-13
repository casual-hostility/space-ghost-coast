#making lists

horde_races = ['Tauren', 'Blood Elf', 'Orc', 'Nightborne', 'Undead', 'Highmountain Tauren', 'Goblin', 'Vulpera', 'Maghar Orc', 'Troll', 'Zandalari Troll']
alliance_races = ['Night Elf', 'Draenei', 'Void Elf', 'Human', 'Dwarf', 'Gnome', 'Mechagnome', 'Dark Iron Dwarf', 'Worgen', 'Lightforged Draenei']

print(horde_races, alliance_races) #prints out everything in the list, including brackets. Boo.

print(alliance_races[0]) #prints out element 0 (Night Elf) in the Alliance list

#you can use string formatting onn list elements
print(horde_races[1].upper())

#to return the last item on a list, python uses a special method, calling -1
print(alliance_races[-1])
#-2 returns the second from the end and so on. Counting backwards doesn't start from -0 

message = "My main character is a " + alliance_races[0].lower() + "."
print(message)
