import random
from tkinter import N

# Lists with data
destination_list = ['New York', 'Paris', 'Oslo', 'Dublin', 'Tokyo', 'St Thomas']
restaurant_list = ['Italian Restaurant', 'Sushi Restaurant',
                   'Burger Restaurant', 'Pizza Restaurant', 'Greek Restaurant', 'Caribbean Restaurant']
transportation_list = ['Train', 'Car', 'Motorcycle',
                       'Helicopter', 'Limo', 'Monster truck', 'Air balloon']
entertainment_list = ['Broadway show', 'Movie', 'Miniature golf',
                      'Opera music', 'live jazz', 'Videogame and beer place', 'Petting zoo']


# Initial function
def greet_and_get_user_input():
    print("Welcome to the Day Trip Generator! If you aren't sure what to do for your trip, you have come to the right place!")

    destination = provide_random_item_from_list(destination_list)

    destination_chosen = get_user_input(destination_list,
                                        destination, 'destination')

    transportation = provide_random_item_from_list(transportation_list)

    transportation_chosen = get_user_input(transportation_list,
                                           transportation, 'transportation')

    restaurant = provide_random_item_from_list(restaurant_list)

    restaurant_chosen = get_user_input(restaurant_list,
                                       restaurant, 'restaurant')

    entertainment = provide_random_item_from_list(entertainment_list)

    entertainment_chosen = get_user_input(entertainment_list,
                                          entertainment, 'entertainment')

    choices_object = {
        'destination': destination_chosen,
        'transportation': transportation_chosen,
        'restaurant': restaurant_chosen,
        'entertainment': entertainment_chosen
    }

    finalize_transaction(choices_object)

# Provides random element from a list


def provide_random_item_from_list(list, previous_element=''):
    index = random.randrange(0, len(list))
    new_element = list[index]
    if previous_element != new_element:
        return new_element
    else:
        return provide_random_item_from_list(list, previous_element)


# Interaction with user
def get_user_input(list_to_choose_from, selection_from_list, type_of_selection, alt_message_bool=False):

    if alt_message_bool == False:
        user_input = input(
            f'We have selected {selection_from_list} for your {type_of_selection}! Does this sound good? y/n: ')
    if alt_message_bool == False:
        if user_input == 'y':
            return selection_from_list
        else:
            new_selection_from_list = provide_random_item_from_list(
                list_to_choose_from, selection_from_list)
            return get_user_input(list_to_choose_from, new_selection_from_list, type_of_selection, True)
    if alt_message_bool == True:
        new_selection_from_list = provide_random_item_from_list(
            list_to_choose_from, selection_from_list)
        user_input = input(
            f'Oh sorry, you do not like this {type_of_selection}. No worries, we can try something else! How about {new_selection_from_list}? Does this sound good? y/n: ')
    if alt_message_bool == True:
        if user_input == 'y':
            return new_selection_from_list
        else:
            new_selection_from_list = provide_random_item_from_list(
                list_to_choose_from, new_selection_from_list)
            return get_user_input(list_to_choose_from, new_selection_from_list, type_of_selection, True)


# Confirm selections
def finalize_transaction(choices_obj):
    new_line = '\n'

    destination_chosen = choices_obj['destination']
    transportation_chosen = choices_obj['transportation']
    restaurant_chosen = choices_obj['restaurant']
    entertainment_chosen = choices_obj['entertainment']

    print(
        f'Awesome! Glad that was decided! Lets move on!{new_line}Congrats! We have completed you trip. Now lets confirm everything.')

    print(
        f'The trip we generated for you is:{new_line}Destination: {destination_chosen}')

    print(f'Transportation: {transportation_chosen}')

    print(f'Restaurant: {restaurant_chosen}')

    print(f'Entertainment: {entertainment_chosen}')

    finalize = input(f'Are you satisfyied with these choices? y/n: ')
    if finalize == 'y':
        handle_final_message(choices_obj)
    else:
        handle_modify_booking(choices_obj)

# Modify selections


def handle_modify_booking(choices_obj):
    new_line = '\n'
    print(
        f'Oh, so which would you like to modify? {new_line} a: destination {new_line} b: transportation {new_line} c: entertainment {new_line} d: restaurant {new_line}')
    user_input = input('Please provide answer here ( a b c OR d ):  ')
    if user_input == 'a':
        destination_chosen = get_user_input(destination_list,
                                            choices_obj['destination'], 'destination', True)
        choices_obj['destination'] = destination_chosen
        return finalize_transaction(choices_obj)
    elif user_input == 'b':
        transportation_chosen = get_user_input(transportation_list,
                                               choices_obj['transportation'], 'transportation', True)
        choices_obj['transportation'] = transportation_chosen
        finalize_transaction(choices_obj)
    elif user_input == 'c':
        entertainment_chosen = get_user_input(entertainment_list,
                                              choices_obj['entertainment'], 'entertainment', True)
        choices_obj['entertainment'] = entertainment_chosen
        finalize_transaction(choices_obj)
    elif user_input == 'd':
        restuarant_chosen = get_user_input(restaurant_list,
                                           choices_obj['restaurant'], 'restaurant', True)
        choices_obj['restaurant'] = restuarant_chosen
        finalize_transaction(choices_obj)

# Final essage to user


def handle_final_message(choices_obj):
    destination_chosen = choices_obj['destination']
    transportation_chosen = choices_obj['transportation']
    restaurant_chosen = choices_obj['restaurant']
    entertainment_chosen = choices_obj['entertainment']

    print(
        f'Prepare for a wonderful trip we booked for you! You will be arriving to {destination_chosen} by {transportation_chosen} where you will spend the day checking out {entertainment_chosen}.')
    print(
        f'When you are hungry you will have directions to the {restaurant_chosen} we picked out for you.')
    print('Thank you for booking with us and enjoy your stay!')
    print('Arbitrary explanation mark !')
    print('This time two!!')


greet_and_get_user_input()
