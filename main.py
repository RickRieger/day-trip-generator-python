import random
from tkinter import N

destination_list = ['New York', 'Paris', 'Oslo', 'Dublin', 'Tokyo']
restaurant_list = ['Italian Restaurant', 'Sushi Restaurant', 'Burger Restaurant', 'Pizza Restaurant', 'Greek Restaurant']
transportation_list = ['train', 'car', 'motorcycle', 'helicopter', 'limo', 'monster truck']
entertainment_list = ['Broadway show', 'movie', 'miniature golf', 'opera', 'live jazz', 'videogame and beer place']


def greeting():
   return print("Welcome to the Day Trip Generator! If you aren't sure what to do for your trip, you have come to the right place!")


def random_from_list_generator(list, element_from_list = ''):
   index = random.randrange(0, len(list))
   new_element = list[index]
   if new_element != element_from_list:
      return new_element
   else: 
      return random_from_list_generator(list, new_element)
    


def get_user_input_destination(random_element_from_list):
      user_input = input(f'We have selected {random_element_from_list} for your destination! Does this sound good? y/n: ')
      if user_input == 'n':
         random_destination = random_from_list_generator(destination_list, random_element_from_list)
         get_user_input_destination(random_destination)
      else:
         return random_element_from_list



def get_user_input_transportation(random_element_from_list = ''):
      user_input = input(f'We have selected {random_element_from_list} for your transportation! Does this sound good? y/n: ')
      if user_input == 'n' or user_input == '':
         random_transportation = random_from_list_generator(transportation_list, random_element_from_list)
         get_user_input_transportation(random_transportation)
      else: 
         return random_element_from_list
   

def get_user_input_restaurant(random_element_from_list = ''):
      user_input = input(f'We have selected a {random_element_from_list} for your dining pleasure! Does this sound good? y/n: ')
      if user_input == 'n' or user_input == '':
         random_restaurant = random_from_list_generator(restaurant_list, random_element_from_list)
         get_user_input_transportation(random_restaurant)
      else: 
         return random_element_from_list


def get_user_input_entertainment(random_element_from_list = ''):
      user_input = input(f'We have selected a {random_element_from_list} for your entertainment during your stay! Does this sound good? y/n: ')
      if user_input == 'n' or user_input == '':
         random_entertainment = random_from_list_generator(entertainment_list, random_element_from_list)
         get_user_input_entertainment(random_entertainment)
      else: 
         return random_element_from_list
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   # if type_of_list == 'transportation':
   #    user_input = input(f'We have selected {random_element_from_list} for your transportation option! Does this sound good? y/n: ')
   #    if user_input == 'n':
   #       random_transportation = random_from_list_generator(transportation_list, random_element_from_list)
   #       get_user_input(random_transportation, 'transportation')
   #    else: return random_element_from_list   
   # if type_of_list == 'restaurants':
   #    user_input = input(f'We have selected {random_element_from_list} for your dining pleasure! Does this sound good? y/n: ')
   #    if user_input == 'n':
   #       random_restaurant = random_from_list_generator(restaurant_list, random_element_from_list)
   #       get_user_input(random_restaurant, 'restaurants')
   #    else: return random_element_from_list
   # if type_of_list == 'entertainment':
   #    user_input = input(f'We have selected {random_element_from_list} for your entertainment! Does this sound good? y/n: ')
   #    if user_input == 'n':
   #       random_entertainment = random_from_list_generator(entertainment_list, random_element_from_list)
   #       get_user_input(random_entertainment, 'entertainment')
   #    else: return random_element_from_list












greeting()

random_destination = random_from_list_generator(destination_list)

destination_chosen = get_user_input_destination(random_destination)

random_transportation = random_from_list_generator(transportation_list)

transportation_chosen = get_user_input_transportation(random_transportation)

random_restaurant = random_from_list_generator(restaurant_list)

restuarant_chosen = get_user_input_restaurant(random_restaurant)

random_entertainment = random_from_list_generator(entertainment_list)

entertainment_chosen = get_user_input_restaurant(random_entertainment)











# while destination_chosen:
#    random_transportation = random_from_list_generator(transportation_list)

#    transportation_chosen = get_user_input(random_transportation, 'transportation')

# while transportation_chosen:
#    random_restaurant = random_from_list_generator(restaurant_list)

#    restaurant_chosen = get_user_input(random_restaurant, 'restaurants')

# while restaurant_chosen:
#    random_entertainment = random_from_list_generator(entertainment_list)

#    entertainment_chosen = get_user_input(random_entertainment, 'entertainment')

# while entertainment_chosen:
#    print('doing good rick')

