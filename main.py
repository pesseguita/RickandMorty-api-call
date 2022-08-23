import requests
from Characters import *

url = requests.get('https://rickandmortyapi.com/api/character')
# print(url.status_code)

# Put character data in dictionary from API
character_data = url.json()
# print(character_data)

# Get the character data from the results section
character_data_results = character_data['results']

# Testing accessing JSON data
# print(character_data_results[0]['name'])
# print(character_data_results[0]['origin']['name'])
# print(character_data_results[0]['location']['name'])
# print(len(character_data_results[0]['episode']))

# How to access origin in the first character of the character list
# data_results_origin = character_data['results'][0]['origin']['name']
# print(data_results_origin)

#Creating character list from JSON data
def create_characters_list():
    characters_list = []
    for i in range(0, len(character_data_results)):
        character = Character(character_data_results[i]['name'], character_data_results[i]['status'],
                              character_data_results[i]['species'], character_data_results[i]['gender'],
                              character_data_results[i]['origin']['name'], character_data_results[i]['location']['name'],
                              len(character_data_results[i]['episode']))
        characters_list.append(character)
        # character.show_characters()
        # print(character.show_characters())
        # print(characters_list[i].show_characters())
    # print(characters_list[3].show_characters())
    # print(characters_list)
    return characters_list

#Saving character list to txt file
def save_to_file(list):
        with open("file.txt", "a") as output:
            output.write(str(list)+"\n")

if __name__ == '__main__':
    final_character_list = create_characters_list()
    """
    Different way of saving the list onto file
    for character in final_character_list:
        save_to_file(character.show_characters())
    """
    for i in range(0, len(final_character_list)):
        save_to_file(final_character_list[i].show_characters())



