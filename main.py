"""
    Just a module holding the FloridaMan class generating the random story of a Florida man on a given date.
    This idea just came from a popular googling of your birth date + florida men will generate a story.
"""

import random

class FloridaMan():
    
    counter = 0
    
    def __init__(self):
        pass

    def run_program(self):
        """Main method handling the program"""
        
        if not self.counter > 0:
            self.welcome_the_user()
        self.counter += 1
        answers = self.get_set_of_answers()
        date = answers[0]
        verb = answers[1]
        noun = answers[2]
        print(self.generate_florida_men_story(date, verb, noun))
        self.one_more()

    def welcome_the_user(self):
        """Welcoming message that should appear only once"""
        
        print("Ready to have some fun? Follow the instructions to get a story :)")
        
        pass
    
    def get_set_of_answers(self):
        """Simple method returning the set of questions to be answered by the user"""
        
        date = input("Please provide a random date:\n")
        verb = input("Please provide a verb: \n")
        noun = input("Please provide a noun: \n")
        
        return date, verb, noun

    def generate_florida_men_story(self, date, verb, noun):
        """Taking the list of answers and generating a florida man story sentence in return"""
        
        list_of_human_repr = ['woman', 'man', 'human', 'guy', 'kid', 'parent', 'child', 'girl', 'boy']
        
        human_repr = random.choice(list_of_human_repr)
        
        florida_men_string = f'On {date} florida man {verb} a {human_repr} with {noun}\n'
        
        return florida_men_string

    def one_more(self):
        """Simple question to user if he wants to do one more story"""
        
        response_yes = ['yes', 'y', 'ye', 'yeah', 'si']
        
        ask_for_one_more = input("Do you want to receive one more?\n")
        
        if(ask_for_one_more in response_yes):
            self.run_program()
        else:
            exit