import random

def run_program():
    
    get_set_of_words()
    
    pass

def welcome_the_user():
    
    print("Ready to have some fun? Follow the instructions to get a story :)")
    
    pass

def generate_florida_men_story():
    
    date = input("Please provide a random date:\n")
    verb = input("Please provide a verb\n")
    noun = input("Please provide a noun\n")
    
    list_of_human_repr = ['woman', 'man', 'human', 'guy', 'kid', 'parent', 'child', 'girl', 'boy']
    
    human_repr = random.choice(list_of_human_repr)
    
    florida_men_string = f'On {date} florida men {verb} a {human_repr} with {noun}\n'
    
    print(florida_men_string)

def one_more():
    
    response_yes = ['yes', 'y', 'ye', 'yeah', 'si']
    
    ask_for_one_more = input("Do you want to receive one more?")
    
    if(ask_for_one_more in response_yes):
        run_program()
    else:
        exit