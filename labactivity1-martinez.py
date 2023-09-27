#Programmed by: MARTINEZ, Gerryle R.
#BSCS 1B - CC2 - Lab Activity 1
#Sept. 9, 2023

lbs = 160
kg = lbs/2.205
kg = round(kg,2)
lbs = str(lbs)
kg = str(kg)
print("Weight in Pounds (lbs): " + lbs)
print("Weight in Kilograms (kg): " + kg)
print("=========================================")

mi = 32.8
km = mi*1.609
km = round(km,2)
mi = str(mi)
km = str(km)
print("Length in Miles (mi): " + mi)
print("Length converted to Kilometers: " + km)
print("=========================================")

fahrenheit = 34
celsius = (5/9)*(fahrenheit-32)
celsius = round(celsius,2)
fahrenheit = str(fahrenheit)
celsius = str(celsius)
print("Temperature in Fahrenheit (°f): "+ fahrenheit)
print("Temperature converted to Celsius (°C): "+ celsius)
print("=========================================")

studentage = [22, 27, 23, 23, 20, 24, 25, 19, 24, 29]
studentage = sum(studentage)
average = (studentage)/10
studentage = ["22", "27", "23", "23", "20", "24", "25", "19", "24", "29"]
average = str(average)
print("Age of Student 1: " + studentage[0])
print("Age of Student 2: " + studentage[1])
print("Age of Student 3: " + studentage[2])
print("Age of Student 4: " + studentage[3])
print("Age of Student 5: " + studentage[4])
print("Age of Student 6: " + studentage[5])
print("Age of Student 7: " + studentage[6])
print("Age of Student 8: " + studentage[7])
print("Age of Student 9: " + studentage[8])
print("Age of Student 10: " + studentage[9])
print("The average age of the students is: " + average)
print("=========================================")

chNames = ["Lumaine", "Scara", "Raiden", "Barbatos", "Kaedehara"]
worldNames = ["Teyvat", "Earth-918"]
weaponNames = ["Skyward", "Widsith", "The Catch"]
abilities = ["elemental resonance", "vision holder", "elemental reaction"]

print("There was once a lost star who was searching for her brother who she separated with. Her name was " + chNames [0] + " traveling the world of " + worldNames[0] + "."
    "A world which holds elemental powers where " + abilities [1] + "s from all nations help with its peace and safety." + chNames [0] + " somehow has the ability of " + abilities [0] + 
    " where she can connect with any elements on the world of " + worldNames [0] + ". There she met a loving mother named " + chNames [2] + ". She was helping her child " + chNames [1] + 
    " farm for Rukkhashava Mushroom for them to feast on for dinner. " + chNames [0] + " did not realize that she encountered the nation's archon and casually spoke with her. " + chNames [0] + 
    " soon violated the rules of " + chNames [2] + "'s nation and fought with her using her " + weaponNames [0] + " sword. To " + chNames [0] + "'s little knowledge, she did not know that " + chNames [1] + 
    " also has the ability to fight with his " + weaponNames [1] + " wapon. " + chNames [2] + " weilded " + weaponNames [2] + " and tried to strke on " + chNames [0] +
    " but the wind was her guardian. The archon " + chNames [3] + " has come to her rescue together with his assistant, " + chNames [-1] + ". While " + chNames [-1] + ", as a double " + abilities [1] + ", help buy time for " + chNames [0] + 
    " to escape, " + chNames [3] + " told her that her brother was in another world called " + worldNames [1] + " where Avengers exists. And with that, " + chNames [0] + 
    " has gathered her strength to leap to another world and find her brother. That's how she ended up on our world with no weapons, abilities and just a laptop to study computer science while looking for her brother. The end.")  