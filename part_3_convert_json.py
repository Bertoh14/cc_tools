import cc_dat_utils
import cc_data
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

def make_ccfile_from_json( json_data ):
    cc_file = cc_data.CCDataFile()
    cc_file.levels = []
    for level in json_data:
        level_object = cc_data.CCLevel()
        level_object.level_number = level["level_number"]
        level_object.time = level["time"]
        level_object.num_chips = level["chip_number"]
        level_object.upper_layer = level["upper_layer"]
        level_object.lower_layer = level["lower_layer"] 

        for field in level["optional_fields"]:
            if field["field_num"] == 3:
                obj = cc_data.CCMapTitleField(field["title"])
                level_object.add_field(obj)
            elif field["field_num"] == 6:
                obj = cc_data.CCEncodedPasswordField(field["list"])
                level_object.add_field(obj)
            elif field["field_num"] == 7:
                obj = cc_data.CCMapHintField(field["hint"])
                level_object.add_field(obj)
            elif field["field_num"] == 10:
                a = []
                for i in range(len(field["xcoord"])):
                    mons = cc_data.CCCoordinate(field["xcoord"][i], field["ycoord"][i])
                    a.append(mons)
                obj = cc_data.CCMonsterMovementField(a)
                level_object.add_field(obj)
            elif field["field_num"] == 4:
                a = []
                for i in range(len(field["trapx"])):
                    #button = cc_data.CCCoordinate(field["buttonx"][i], field["buttony"][i])
                    #trap = cc_data.CCCoordinate(field["trapx"][i], field["trapy"][i])
                    combined = cc_data.CCTrapControl(field["buttonx"][i], field["buttony"][i], field["trapx"][i], field["trapy"][i])
                    a.append(combined)
                obj = cc_data.CCTrapControlsField(a)
                level_object.add_field(obj)
            elif field["field_num"] == 5:
                a = []
                for i in range(len(field["buttonx"])):
                    #button = cc_data.CCCoordinate(field["buttonx"][i], field["buttony"][i])
                    #machine = cc_data.CCCoordinate(field["machinex"][i], field["machiney"][i])
                    combined = cc_data.CCCloningMachineControl(field["buttonx"][i], field["buttony"][i], field["machinex"][i], field["machiney"][i])
                    a.append(combined)
                obj = cc_data.CCCloningMachineControlsField(a)
                level_object.add_field(obj)
            else: print("idk")
        cc_file.add_level(level_object)
    return cc_file 


input_json_file = "data/format.json"

with open(input_json_file, "r") as reader:
    final = json.load(reader)

    final2 = make_ccfile_from_json(final)
    print(final2)
    cc_dat_utils.write_cc_data_to_dat(final2, "data/format.dat") 
    cc_dat_utils.write_cc_data_to_dat(final2, "tworld1.3.2win32/data/format.dat") 
