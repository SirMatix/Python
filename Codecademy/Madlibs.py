"""
This program generates passages that are generated in mad-lib format
Author: Matt
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s ruled the world."

print('Mad Libs has started')

name = str(input("Enter a name: "))
adj1 = str(input('please write first adjective: '))
adj2 = str(input('please write second adjective: '))

adj3 = str(input('please write third adjective: '))
verb = str(input('please enter a verb: '))
noun1 = str(input('Enter a noun: '))
noun2 = str(input('Enter a second noun: '))

animal = str(input('Enter an animal: '))
food = str(input('Enter a food: '))
fruit = str(input('Enter a fruit: '))
superhero = str(input('Enter a superhero: '))

country = str(input('Enter a country: '))
dessert = str(input('Enter a dessert: '))
year = str(input('Enter a year: '))

print(STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2))
