import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    
    for json_game in json_data:
        game = test_data.Game()
        platform = test_data.Platform()
        platform.name = json_game["platform"]["name"]
        platform.launch_year = json_game["platform"]["launch year"]
        game.platform = platform
        game.title = json_game["title"]
        game.year = json_game["year"]
        game_library.add_game(game)
    
    ### End Add Code Here ###

    return game_library

#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()

with open(input_json_file, "r") as reader:
    game_library_data = json.load(reader)
library = make_game_library_from_json(game_library_data)
print(library)
### End Add Code Here ###
