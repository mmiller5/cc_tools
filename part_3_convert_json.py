import cc_dat_utils
import json
import cc_data

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

def make_game_from_json( json_data ):
    #Initialize a new CCDataFile
    cc_game = cc_data.CCDataFile()

    for level in json_data:
        cc_level = cc_data.CCLevel()
        cc_level.level_number = level["level number"]
        cc_level.time = level["time"]
        cc_level.num_chips = level["chip number"]
        cc_level.upper_layer = level["upper layer"]
        optional_fields = level["optional fields"]
        
        for field in optional_fields:
            if field["id"] == "title":
                title = cc_data.CCMapTitleField(field["map title"])
                cc_level.add_field(title)
            elif field["id"] == "traps":
                traps_coords = []
                
                for coord in field["traps"]:
                    xb = coord[0][0]
                    yb = coord[0][1]
                    xt = coord[1][0]
                    yt = coord[1][1]
                    control_coords = cc_data.CCTrapControl(xb, yb, xt, yt)
                    traps_coords.append(control_coords)
                    
                
                traps = cc_data.CCTrapControlsField(traps_coords)
                cc_level.add_field(traps)
            elif field["id"] == "clone":
                clone_coords = []
                
                for coord in field["clone"]:
                    xb = coord[0][0]
                    yb = coord[0][1]
                    xt = coord[1][0]
                    yt = coord[1][1]
                    control_coords = cc_data.CCCloningMachineControl(xb, yb, xt, yt)
                    clone_coords.append(control_coords)
                    
                clone = cc_data.CCCloningMachineControlsField(clone_coords)
                cc_level.add_field(clone)
            elif field["id"] == "pass":
                passw = cc_data.CCEncodedPasswordField(field["encoded password"])
                cc_level.add_field(passw)
            elif field["id"] == "hint":
                hint = cc_data.CCMapHintField(field["hint text"])
                cc_level.add_field(hint)
            elif field["id"] == "monsters":
                monster_coords = []
                
                for coord in field["monsters"]:
                    x = coord[0]
                    y = coord[1]
                    monster_coord = cc_data.CCCoordinate(x, y)
                    monster_coords.append(monster_coord)
                    
                monsters = cc_data.CCMonsterMovementField(monster_coords)
                cc_level.add_field(monsters)
        
        cc_game.add_level(cc_level)
    
    return cc_game

input_json_file = "data/mmiller5_cc1.json"

with open(input_json_file, "r") as reader:
    game_data = json.load(reader)
game = make_game_from_json(game_data)
print(game)

cc_dat_utils.write_cc_data_to_dat(game, "data/mmiller5_cc1.dat")



