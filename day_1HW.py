#question 1 Filter out all empty strings 

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

while("" in places):
    places.remove("")
    places.remove("")
    places.remove(" ")
    places.remove(" ")
    places.remove("  ")
print(str(places))

#I know there is more efficient way to solve this. I tried below with a lambda, filter, and maybe a map? and got stuck.

places_2 = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def new_places (locations):
    if locations == " ":
        places_2.remove("")
        return False
    else:
        return True
new_locations = list(filter(new_places, places_2))
print(new_locations)

#I left a white space idk how to get rid of, ran out of time



#Question 2 Write a function that sorts list by last name

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
#tried to use a function for this and got stuck, but the internet has a solution I will complete as well
#def last_name(names):
    #new_list = sorted(author, key=lambda name: name.split(" ")[-1])
    #print(author)

new_list = sorted(author, key=lambda name: name.split(" ")[-1])
print(author)
print(list.lower(new_list))

#Lost on question 2

#Took so long on question 1 and 2 I could not finish question 3 and 4


        

    



