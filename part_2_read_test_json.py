import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    for game in json_data:
        game_object = test_data.Game()
        game_object.title = game["title"]
        game_object.year = game["Year"]
        platform_object = test_data.Platform()
        platform_object.name = game["platform"]["name"]
        platform_object.launch_year = game["platform"]["launch year"]
        game_object.platform = platform_object
        game_library.add_game(game_object)
    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

with open(input_json_file, "r") as reader:
    library_data = json.load(reader)

    final = make_game_library_from_json(library_data)
    print(final)

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
