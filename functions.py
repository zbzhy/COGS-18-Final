"""A collection of function for doing my project."""

# This is a collection of input and output things our chatbot can say and respond to
country_input = ['America', 'UK', 'Italy', 'Germany', 'Japan']

body_type_dict = {'America' : ['Wagon', 'SUV', 'Sedan', 'GT'],
            'UK' : ['Wagon', 'SUV', 'Sedan', 'GT'],
            'Italy' : ['Wagon', 'SUV', 'Sedan', 'GT'],
            'Germany' : ['Wagon', 'SUV', 'Sedan', 'GT'],
            'Japan' : ['Wagon', 'SUV', 'Sedan', 'GT']}

body_type_input = ['Wagon', 'SUV', 'Sedan', 'GT']

trait_dict = {'Wagon' : ['Comfort', 'Power'], 
          'SUV' : ['Comfort', 'Power'], 
          'Sedan' : ['Comfort', 'Power'], 
          'GT' : ['Comfort', 'Power']}

trait_input = ['Comfort', 'Power']

car_catalog = {"['America', 'Wagon', 'Comfort']" : ['Ford C-Max'], "['America', 'Wagon', 'Power']" : ['Dodge Magnum SRT-8'], 
          "['America', 'SUV', 'Comfort']" : ['Cadillac XT6'], "['America', 'SUV', 'Power']" : ['Grand Cherokee SRT-8'],
          "['America', 'Sedan', 'Comfort']" : ['Lincoln Continental'], "['America', 'Sedan', 'Power']" : ['Dodge Charger Hellcat'], 
          "['America', 'GT', 'Comfort']" : ['Mustang Ecoboost'], "['America', 'GT', 'Power']" : ['Dodge Challenger Hellcat'], 
          "['UK', 'Wagon', 'Comfort']" : ['Jaguar XF-S'], "['UK', 'Wagon', 'Power']" : ['Aston Martin Vanquish Zagato Shooting Brake'],
          "['UK', 'SUV', 'Comfort']" : ['Range Rover'], "['UK', 'SUV', 'Power']" : ['Aston Martin DBX'], 
          "['UK', 'Sedan', 'Comfort']" : ['Jaguar XJ'], "['UK', 'Sedan', 'Power']" : ['Rolls Royce Ghost'], 
          "['UK', 'GT', 'Comfort']" : ['Bentley Continental GT'], "['UK', 'GT', 'Power']" : ['McLaren GT'], 
          "['Italy', 'Wagon', 'Comfort']" : ['Fiat Tipo'], "['Italy', 'Wagon', 'Power']" : ['Ferrari GTC4Lusso'],
          "['Italy', 'SUV', 'Comfort']" : ['Alfa Romeo Stelvio'], "['Italy', 'SUV', 'Power']" : ['Maserati Levante Trofeo'],
          "['Italy', 'Sedan', 'Comfort']" : ['Alfa Romeo Giulia'], "['Italy', 'Sedan', 'Power']" : ['Maserati Quattroporte SQ4'],
          "['Italy', 'GT', 'Comfort']" : ['Maserati GranTurismo'], "['Italy', 'GT', 'Power']" : ['Ferrari Roma'],
          "['Germany', 'Wagon', 'Comfort']" : ['Mercedes CLS 350'], "['Germany', 'Wagon', 'Power']" : ['Audi RS6 Avant'], 
          "['Germany', 'SUV', 'Comfort']" : ['BMW X7'], "['Germany', 'SUV', 'Power']" : ['Audi RSQ8'], 
          "['Germany', 'Sedan', 'Comfort']" : ['Mercedes Maybach S450'], "['Germany', 'Sedan', 'Power']" : ['Porsche Panamera'], 
          "['Germany', 'GT', 'Comfort']" : ['Porshce 911 Carrera'], "['Germany', 'GT', 'Power']" : ['Mercedes AMG GTR'], 
          "['Japan', 'Wagon', 'Comfort']" : ['Mazda 6'], "['Japan', 'Wagon', 'Power']" : ['Subaru WRX Sportswagon'], 
          "['Japan', 'SUV', 'Comfort']" : ['Lexus LX570'], "['Japan', 'SUV', 'Power']" : ['Nissan Patrol Nismo'], 
          "['Japan', 'Sedan', 'Comfort']" : ['Toyota Century'], "['Japan', 'Sedan', 'Power']" : ['Lexus LS F'], 
          "['Japan', 'GT', 'Comfort']" : ['Lexus LC 500'], "['Japan', 'GT', 'Power']" : ['Nissan GTR Nismo']}

hp_dict = {'Ford C-Max' : 188, 'Dodge Magnum SRT8' : 425, 
        'Cadillac XT6' : 310, 'Grand Cherokee SRT-8' : 470, 
        'Lincoln Continental' : 305, 'Dodge Charger Hellcat' : 707,  
        'Mustang Ecoboost' : 310, 'Dodge Challenger Hellcat' : 717, 
        'Jaguar XF-S' : 380, 'Aston Martin Vanquish Zagato Shooting Brake' : 580, 
        'Range Rover' : 355, 'Aston Martin DBX' : 542, 
        'Jaguar XJ' : 340, 'Rolls Royce Ghost' : 563, 
        'Bentley Continental GT' : 542, 'McLaren GT' : 620, 
        'Fiat Tipo' : 120, 'Ferrari GTC4Lusso' : 680, 
        'Alfa Romeo Stelvio' : 280, 'Maserati Levante Trofeo' : 590, 
        'Alfa Romeo Giulia' : 280, 'Maserati Quattroporte SQ4' : 523, 
        'Maserati GranTurismo' : 399, 'Ferrari Roma' : 612, 
        'Mercedes CLS 350' : 309, 'Audi RS6 Avant' : 591, 
        'BMW X7' : 335, 'Audi RSQ8' : 591, 
        'Mercedes Maybach S450' : 329, 'Porsche Panamera' : 690, 
        'Porshce 911 Carrera' : 379, 'Mercedes AMG GTR' : 577, 
        'Mazda 6' : 187, 'Subaru WRX Sportswagon' : 271, 
        'Lexus LX570' : 383, 'Nissan Patrol Nismo' : 428, 
        'Toyota Century' : 280, 'Lexus LS F' : 416, 
        'Lexus LC 500' : 471, 'Nissan GTR Nismo' : 600}

mani_prompt = ['Type the country of the car you like', 
               'Type the body type of the car you like', 
               'Type the trait of the car you like', 
               'type [result] to find your dream car', 
               'type [compare] to get the cars with the similar horsepower'] 
             

import string

# This function is cited from the Assignment A3.
def remove_punctuation(input_string):
    out_string = ''
    
    for character in input_string:
        if character not in string.punctuation:
            out_string = out_string + character
            
    return out_string


# This function is cited from the Assignment A3.
def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list


# This function is cited from the Lecture Notes 20.
def end_chat(input_string):
    
    if 'quit' in input_string:
        output = 'Bye'
        chat = False
        
    else:
        output = None
        chat = True
        
    return output, chat


# This function is cited from the Assignment A3, but I modified some.
def filter_country(input_string, check_list, return_list, target):
    
    if input_string in check_list:
        # List target appends user's input
        target.append(input_string)
        output = return_list[input_string]
        
    else:
        output = 'The car you search can not be found.'
    
    return output


# This function is cited from the Assignment A3, but I modified some.
def filter_body_type(input_string, check_list, return_list, target):
    
    if input_string in check_list:
        # List target appends user's input
        target.append(input_string)
        output = return_list[input_string]
        
    else:
        output = 'Please type the body type shown in the previous list.'
      
    return output
 
    
# This function is cited from the Assignment A3, but I modified some.    
def filter_trait(input_string, check_list, target):
    
    if input_string in check_list:
        # List target appends user's input
        target.append(input_string)
        output = target
        
    else:
        output = 'Please type the trait shown in the previous list.'
    
    return output


# This function is cited from the Assignment A3, but I modified some.
def result_car(input_string, target, car_list):
    
    if 'result' in input_string:
        # I try using target as the key of the dictionary, but the type of target is list, so I use str() to make it useable.
        output = car_list[str(target)]
        
    else:
        output = 'Please type [result] to find your dream car!'
        
    return output


# My function # 1
def compare_hp(input_string, target, car_list, parameter_dict):
    """Find the cars with similar horsepower to the one users choose.
    
    Parameters
    ----------
    input_string : str
        The string used to determine if the cars with similar horsepower will be returned or not.
    target : list
        The list that records user's input in chatbot.
    car_list : dict
        The dictionary that records cars with specific features.
    parameter_dict : dict
        The dictionary that records horsepower of different cars.
    
    Returns
    -------
    answer : list or str
        The list containing cars with similar horsepower to the one users choose or the instruction to correctly use this function. 
        
    Examples
    --------
    
    When 'compare' exists in parameter, we will get a key of the last dictionary, which is the first element in the value of the first dictionary. Then we compare value of that key to other values in the last dictionary, adding keys into a list if the difference of the value between the target key and other keys is less than 50.
    
    >>> compare_hp('compare', [2, 3], {'[2, 3]' : [4, 5]}, {4 : 30, 5 : 40})
    [4, 5]
    """
   
    if 'compare' in input_string:
        # Find the specific model of car according to user's input
        car_name = car_list[str(target)]
        # Find the horsepower of that car
        parameter = parameter_dict[car_name[0]]
        # Collect a list of cars with similar horsepower to the one user chooses
        similar_hp = []
        # Loop through the list of horsepower to find cars with similar horsepower, adding the car into the previous list.
        for item in parameter_dict:
            if abs(parameter_dict[item] - parameter) < 50:
                similar_hp.append(item)
        output = similar_hp
        
    else:
        output = 'Please type [compare] to find cars with similar horsepower!'
            
    return output 


# My function # 2
def go_back(input_string, counter, target):
    """Go back to the last step in the chatbot. 
    
    Parameters
    ----------
    input_string : str
        The string used to determine how many steps the user wants to go back.
    counter : int
        The number in chatbot function determining which step the chatbot is at.
    target : list
        The list that records user's input in chatbot.
    
    Returns
    -------
    counter : int 
        The step that the chatbot is at after going back. 
        
    Examples
    --------
    
    The number in the string indicates how many steps to go back. The integer 3 , which is the number subtracted , shows it is now at which step.
    
    >>> go_back('back 2', 3, [1, 2, 3])
    1
    """
    
    # Turn input string to the form of list
    input_list = prepare_text(input_string)
    # The number of steps going back will be the second element in the list
    delete_count = int(input_list[1])
    
    # The list storing user's input will always have three elements maximum. The number user inputs decides the number of steps back and elements     deleted
    if counter >= delete_count and delete_count <= 3:
        while delete_count > 0:
            target.remove(target[-1])
            counter = counter - 1
            delete_count = delete_count - 1
    
    # User can't go back more than where they are
    elif counter < delete_count:
        print("You only move", str(counter), "steps. You can't move more than that")
    
    # The list storing user's input will always have three elements maximum. If user wants to go back more than three, the steps will go back but     only three elements get deleted
    elif counter >= delete_count and delete_count > 3:
        while delete_count > 1:
            target.remove(target[-1])
            delete_count = delete_count - 1
        counter = counter - int(input_list[1])
        
    return counter


# My function # 3
def find_source(input_list):
    """Find the website in which users can lease or buy cars. 
    
    Parameters
    ----------
    input_list: list
        The string used to determine how many steps the user want to go back.
    
    Returns
    -------
    output : str
        The website of leasing cars or the website of buying cars.
        
    Examples
    --------
    
    When the length of the list is equal or greater than 5, a specific string will be returned.
    
    >>> find_source([1, 2, 3, 4, 5])
    'There are so many alternatives! You can lease cars to have different experiences! https://www.leasetrader.com/'
    
    When the length of the list is less than 5, another string will be returned.
    
    >>> find_source([1, 2, 3])
    'There are only few alternatives. You can find second-hand cars on sale and buy one! https://www.carmax.com/' 
    """
    
    # Recommending user to buy or lease car according to the length of car list of similar horsepower
    if len(input_list) >= 5:
        output = 'There are so many alternatives! You can lease cars to have different experiences! https://www.leasetrader.com/'
        
    elif len(input_list) < 5:
        output = 'There are only few alternatives. You can find second-hand cars on sale and buy one! https://www.carmax.com/' 
              
    return output
    
    
# Main function to run my chatbot    
def find_dream_car_chat():
    print("If you want to quit, type [quit]")
    print("If you want to go to the previous choice, type [back number], where [number] indicates how many steps back")
    
    chat = True
    level = 0
    catalog = []
    
    while chat:
        print(mani_prompt[level])
        
        # Get a message from the user
        msg = input('INPUT :\t')
        
        # Check for an end msg 
        out_msg, chat = end_chat(msg)
        
        # Check if user wants to go back
        if 'back' in prepare_text(msg): 
            level = go_back(msg, level, catalog)
            continue
            
        # Returning possible bodytype after users inputing country    
        if level == 0 and chat == True:
            out_msg = filter_country(msg, country_input, body_type_dict, catalog)
            
        # Returning possible trait after users inputing bodytype   
        elif level == 1 and chat == True:
            out_msg = filter_body_type(msg, body_type_input, trait_dict, catalog)
            
        # Returning users' input after users inputing trait    
        elif level == 2 and chat == True:
            out_msg = filter_trait(msg, trait_input, catalog)
            
        # Returning the specific model of car according to users' input     
        elif level == 3 and chat == True:
            out_msg = result_car(msg, catalog, car_catalog)
            
        # Returning a list of cars with similar horsepower to the model users choose     
        elif level == 4 and chat == True:
            out_msg = compare_hp(msg, catalog, car_catalog, hp_dict)
            chat = False
            
        print('Output:', out_msg)
        
        # When users successfully input according to the instruction, the chatbot will go to the next step.
        if type(out_msg) == list:
                level = level + 1
                
    source = find_source(out_msg)
    
    # Showing users different website according to the length of car list of similar horsepower.
    print(source)
    print("You've found your dream cars! Hope one day your dream will come true!")
                
    
    
        
   

    
    
    



            
        
            
    
    
    