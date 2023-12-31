"""
IDENTIFY EACH SPEAKER IN THE SPLITS!

Below are the speaker-to-name mappings for our project, which consists in the diarization of some podcasts. It can serve as an example. 
To illustrate them, here is a simpler example to show how it works:

replacer_dict = {}

video_one = {                                       # first video
    "1": "00,SPEAKER_X",                            # First split, and which are the speakers we want to use in that split
    "2": "00,SPEAKER_Y;01,SPEAKER_X",               # Second split
    "3": "00,SPEAKER_X;01,SPEAKER_Y;02,SPEAKER_U"   # Third and last split
}

replacer_dict["video_name"] = video_one             # Now add the dictionary that correctly maps the first video speakers in each split to the diarized splits.

video_two = {                           # Second video
    "1": "00,SPEAKER_Z;01,SPEAKER_W",   # First split
    "2": "",                            # Second split, empty because we may want to ignore it (not useful info, maybe there's an ad, etc...)
    "3": "00,SPEAKER_W;01,SPEAKER_K"    # Third and last split
}

replacer_dict["other_video_name"] = video_two       # Add the second video to the replacer

# Once we finish, this replacer will be imported in the consistency-checker.ipynb notebook to map each speaker of each video.
# (the keys are video names, the value is the dict linking split with speakers)

"""


replacer_dict = {}

to_replace_dict = {
    "1": "00,ANDREWHUBERMAN;01,LEXFRIDMAN",
    "2": "00,ANDREWHUBERMAN;01,LEXFRIDMAN",
    "3": "00,LEXFRIDMAN;01,ANDREWHUBERMAN",
    "4": "00,LEXFRIDMAN;01,ANDREWHUBERMAN",
    "5": "00,LEXFRIDMAN;01,ANDREWHUBERMAN",
    "6": "00,LEXFRIDMAN;01,ANDREWHUBERMAN",
    "7": "00,LEXFRIDMAN;01,ANDREWHUBERMAN",
    "8": "00,LEXFRIDMAN;01,ANDREWHUBERMAN",
    "9": "00,ANDREWHUBERMAN;01,LEXFRIDMAN",
    "10": "00,LEXFRIDMAN;01,ANDREWHUBERMAN",
    "11": "00,LEXFRIDMAN;01,ANDREWHUBERMAN",
    "12": "00,LEXFRIDMAN;01,ANDREWHUBERMAN",
    "13": "00,LEXFRIDMAN;01,ANDREWHUBERMAN"
}

replacer_dict["lexFridman-andrewHuberman-17082023"] = to_replace_dict

to_replace_dict = {
    "1": "00,BENSHAPIRO;01,LEXFRIDMAN",
    "2": "00,BENSHAPIRO;01,LEXFRIDMAN",
    "3": "00,LEXFRIDMAN;01,BENSHAPIRO",
    "4": "00,BENSHAPIRO;01,LEXFRIDMAN",
    "5": "00,LEXFRIDMAN;01,BENSHAPIRO",
    "6": "00,BENSHAPIRO;01,LEXFRIDMAN",
    "7": "00,BENSHAPIRO;01,LEXFRIDMAN",
    "8": "00,BENSHAPIRO;01,LEXFRIDMAN",
    "9": "00,BENSHAPIRO;01,LEXFRIDMAN",
    "10": "00,BENSHAPIRO;01,LEXFRIDMAN",
    "11": "00,BENSHAPIRO;01,LEXFRIDMAN",
    "12": "00,BENSHAPIRO;01,LEXFRIDMAN",
    "13": "00,LEXFRIDMAN;01,BENSHAPIRO",
    "14": "00,LEXFRIDMAN;01,BENSHAPIRO",
    "15": "00,LEXFRIDMAN;01,BENSHAPIRO"
}

replacer_dict["lexFridman-benShapiro-07112022"] = to_replace_dict

to_replace_dict = {
    "1": "00,GUIDOVANROSSUM;01,LEXFRIDMAN",
    "2": "00,LEXFRIDMAN;01,GUIDOVANROSSUM",
    "3": "00,LEXFRIDMAN;01,GUIDOVANROSSUM;02,LEXFRIDMAN",
    "4": "00,LEXFRIDMAN;01,GUIDOVANROSSUM",
    "5": "00,LEXFRIDMAN;01,GUIDOVANROSSUM",
    "6": "00,LEXFRIDMAN;01,GUIDOVANROSSUM",
    "7": "00,LEXFRIDMAN;01,GUIDOVANROSSUM",
    "8": "00,GUIDOVANROSSUM;01,LEXFRIDMAN",
    "9": "00,GUIDOVANROSSUM;01,LEXFRIDMAN",
    "10": "00,LEXFRIDMAN;01,GUIDOVANROSSUM",
    "11": "00,GUIDOVANROSSUM;01,LEXFRIDMAN",
    "12": "00,LEXFRIDMAN;01,GUIDOVANROSSUM",
    "13": "00,GUIDOVANROSSUM;01,LEXFRIDMAN",
    "14": "00,GUIDOVANROSSUM;01,LEXFRIDMAN",
    "15": "00,LEXFRIDMAN;01,GUIDOVANROSSUM",
    "16": "00,LEXFRIDMAN;01,GUIDOVANROSSUM",
    "17": "00,GUIDOVANROSSUM;01,LEXFRIDMAN",
    "18": "00,LEXFRIDMAN;01,GUIDOVANROSSUM",
    "19": "00,LEXFRIDMAN;01,GUIDOVANROSSUM"
}

replacer_dict["lexFridman-guidoVanRossum-26112022"] = to_replace_dict

to_replace_dict = {
    "1": "00,LEXFRIDMAN;01,GEORGEHOTZ",
    "2": "00,GEORGEHOTZ;01,LEXFRIDMAN",
    "3": "00,LEXFRIDMAN;01,LEXFRIDMAN;02,GEORGEHOTZ;03,GEORGEHOTZ;04,GEORGEHOTZ",
    "4": "00,LEXFRIDMAN;01,GEORGEHOTZ",
    "5": "00,LEXFRIDMAN;01,GEORGEHOTZ",
    "6": "00,GEORGEHOTZ;01,LEXFRIDMAN",
    "7": "00,GEORGEHOTZ;01,LEXFRIDMAN",
    "8": "00,LEXFRIDMAN;01,GEORGEHOTZ",
    "9": "00,GEORGEHOTZ;01,LEXFRIDMAN",
    "10": "00,LEXFRIDMAN;01,GEORGEHOTZ",
    "11": "00,LEXFRIDMAN;01,GEORGEHOTZ",
    "12": "00,GEORGEHOTZ;01,LEXFRIDMAN",
    "13": "00,LEXFRIDMAN;01,GEORGEHOTZ",
    "14": "00,LEXFRIDMAN;01,GEORGEHOTZ",
    "15": "00,GEORGEHOTZ;01,GEORGEHOTZ;02,LEXFRIDMAN",
    "16": "00,GEORGEHOTZ;01,LEXFRIDMAN",
    "17": "00,LEXFRIDMAN;01,GEORGEHOTZ;02,GEORGEHOTZ",
    "18": "00,GEORGEHOTZ;01,LEXFRIDMAN",
    "19": "00,LEXFRIDMAN;01,GEORGEHOTZ"
}

replacer_dict["lexFridman-georgeHotz-30062023"] = to_replace_dict

to_replace_dict = {
    "1": "00,LEXFRIDMAN;01,KANYEWEST",
    "2": "00,KANYEWEST;01,LEXFRIDMAN",
    "3": "00,LEXFRIDMAN;01,KANYEWEST",
    "4": "00,LEXFRIDMAN;01,KANYEWEST",
    "5": "00,KANYEWEST;01,LEXFRIDMAN",
    "6": "00,LEXFRIDMAN;01,KANYEWEST",
    "7": "00,KANYEWEST;01,LEXFRIDMAN",
    "8": "00,KANYEWEST;01,LEXFRIDMAN",
    "9": "00,KANYEWEST;01,LEXFRIDMAN",
    "10": "00,LEXFRIDMAN;01,KANYEWEST",
    "11": "00,LEXFRIDMAN;01,KANYEWEST",
    "12": "00,LEXFRIDMAN;01,KANYEWEST",
    "13": "00,KANYEWEST;01,LEXFRIDMAN",
    "14": "00,LEXFRIDMAN;01,KANYEWEST",
    "15": "00,KANYEWEST;01,LEXFRIDMAN"
}

replacer_dict["lexFridman-kanyeWest-24102022"] = to_replace_dict

to_replace_dict = {
    "1": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "2": "00,MARKZUCKERBERG;01,LEXFRIDMAN",
    "3": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "4": "00,MARKZUCKERBERG;01,LEXFRIDMAN",
    "5": "00,MARKZUCKERBERG;01,LEXFRIDMAN",
    "6": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "7": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "8": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "9": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "10": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "11": "00,MARKZUCKERBERG;01,LEXFRIDMAN",
    "12": "00,MARKZUCKERBERG;01,LEXFRIDMAN",
    "13": "00,MARKZUCKERBERG;01,LEXFRIDMAN",
    "14": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "15": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "16": "00,LEXFRIDMAN;01,MARKZUCKERBERG"
}

replacer_dict["lexFridman-markZuckerberg-09062023"] = to_replace_dict

to_replace_dict = {
    "1": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "2": "00,MARKZUCKERBERG;01,LEXFRIDMAN",
    "3": "00,LEXFRIDMAN;01,MARKZUCKERBERG",
    "4": "00,MARKZUCKERBERG;01,LEXFRIDMAN",
    "5": "00,MARKZUCKERBERG;01,LEXFRIDMAN",
    "6": "00,MARKZUCKERBERG;01,LEXFRIDMAN"
}

replacer_dict["lexFridman-markZuckerberg-28092023"] = to_replace_dict

to_replace_dict = {
    "1": "00,MATTHEWMCCOUNAGHEY;01,LEXFRIDMAN",
    "2": "00,MATTHEWMCCOUNAGHEY;01,LEXFRIDMAN",
    "3": "00,MATTHEWMCCOUNAGHEY;01,LEXFRIDMAN",
    "4": "00,LEXFRIDMAN;01,MATTHEWMCCOUNAGHEY",
    "5": "00,MATTHEWMCCOUNAGHEY;01,LEXFRIDMAN",
    "6": "00,LEXFRIDMAN;01,MATTHEWMCCOUNAGHEY",
    "7": "00,LEXFRIDMAN;01,MATTHEWMCCOUNAGHEY",
    "8": "00,LEXFRIDMAN;01,MATTHEWMCCOUNAGHEY",
    "9": "00,LEXFRIDMAN;01,MATTHEWMCCOUNAGHEY",
    "10": "00,LEXFRIDMAN;01,MATTHEWMCCOUNAGHEY",
    "11": "00,LEXFRIDMAN;01,MATTHEWMCCOUNAGHEY",
    "12": "00,LEXFRIDMAN;01,MATTHEWMCCOUNAGHEY",
    "13": "00,LEXFRIDMAN;01,MATTHEWMCCOUNAGHEY",
    "14": "00,LEXFRIDMAN;01,MATTHEWMCCOUNAGHEY"
}

replacer_dict["lexFridman-matthewMcConaughey-13062023"] = to_replace_dict

to_replace_dict = {
    "1": "01,ANDREWHUBERMAN",
    "2": "00,ANDREWHUBERMAN",
    "3": "01,ANDREWHUBERMAN",
    "4": "00,ANDREWHUBERMAN",
    "5": "02,ANDREWHUBERMAN;01,ANDREW",
    "6": "01,ANDREWHUBERMAN;00,ANDREW",
    "7": "01,ANDREWHUBERMAN",
    "8": "01,ANDREWHUBERMAN;02,ANDREW",
    "9": "01,ANDREWHUBERMAN;00,ANDREW",
    "10": "02,ANDREWHUBERMAN;03,ANDREW",
    "11": "02,ANDREWHUBERMAN;01,ANDREW",
    "12": "00,ANDREWHUBERMAN",
    "13": "00,ANDREWHUBERMAN;01,ANDREW"
}

replacer_dict["flagrant-andrewHubermam-17102022"] = to_replace_dict

to_replace_dict = {
    "1": "01,HANCOCK;00,ANDREW",
    "2": "01,HANCOCK;00,ANDREW",
    "3": "03,HANCOCK;02,ANDREW",
    "4": "01,HANCOCK;02,ANDREW",
    "5": "01,HANCOCK;02,ANDREW",
    "6": "00,HANCOCK",
    "7": "01,HANCOCK",
    "8": "02,HANCOCK;01,ANDREW",
    "9": "01,HANCOCK;02,ANDREW",
    "10": "00,HANCOCK;01,ANDREW",
    "11": "00,HANCOCK;01,ANDREW",
    "12": "00,HANCOCK;01,ANDREW",
    "13": "02,HANCOCK",
    "14": "02,HANCOCK;01,ANDREW",
    "15": "03,HANCOCK;00,ANDREW",
    "16": "",
    "17": "00,HANCOCK;02,ANDREW",
    "18": "00,HANCOCK"
}

replacer_dict["flagrant-grahamHancock-27062023"] = to_replace_dict

to_replace_dict = {
    "1": "01,MARQUES;03,ANDREW",
    "2": "00,MARQUES",
    "3": "01,MARQUES",
    "4": "01,MARQUES",
    "5": "04,MARQUES;02,ANDREW",
    "6": "00,MARQUES",
    "7": "00,MARQUES;01,ANDREW",
    "8": "02,MARQUES;03,ANDREW",
    "9": "01,MARQUES;03,ANDREW",
    "10": "00,MARQUES;02,ANDREW",
    "11": "02,MARQUES;03,ANDREW"
}

replacer_dict["flagrant-MKBHD-01102022"] = to_replace_dict

to_replace_dict = {
    "1": "00,MRBEAST",
    "2": "00,MRBEAST;03,ANDREW",
    "3": "01,MRBEAST",
    "4": "00,MRBEAST",
    "5": "01,MRBEAST;00,ANDREW",
    "6": "01,MRBEAST;00,ANDREW",
    "7": "00,MRBEAST;01,ANDREW",
    "8": "03,MRBEAST;02,ANDREW",
    "9": "00,MRBEAST;01,ANDREW",
    "10": "02,MRBEAST",
    "11": "02,MRBEAST;01,ANDREW",
    "12": "00,MRBEAST;02,ANDREW",
    "13": "02,MRBEAST;01,ANDREW",
    "14": "02,MRBEAST;03,ANDREW",
    "15": "02,MRBEAST;01,ANDREW",
    "16": "01,MRBEAST;00,ANDREW",
    "17": "02,MRBEAST;00,ANDREW",
    "18": "03,MRBEAST",
    "19": "02,MRBEAST;01,ANDREW",
    "20": "01,MRBEAST;02,ANDREW",
    "21": "00,MRBEAST;01,ANDREW",
    "22": "02,MRBEAST;03,ANDREW"
}

replacer_dict["flagrant-mrBeast-27092022"] = to_replace_dict

to_replace_dict = {
    "1": "00,EDWARDSNOWDEN;01,JOEROGAN",
    "2": "00,EDWARDSNOWDEN",
    "3": "00,EDWARDSNOWDEN;01,JOEROGAN",
    "4": "00,EDWARDSNOWDEN;01,JOEROGAN",
    "5": "01,EDWARDSNOWDEN;00,JOEROGAN",
    "6": "00,EDWARDSNOWDEN;01,JOEROGAN",
    "7": "00,EDWARDSNOWDEN",
    "8": "00,EDWARDSNOWDEN",
    "9": "01,EDWARDSNOWDEN;00,JOEROGAN",
    "10": "01,EDWARDSNOWDEN;00,JOEROGAN",
    "11": "00,EDWARDSNOWDEN",
    "12": "01,EDWARDSNOWDEN;00,JOEROGAN",
    "13": "00,EDWARDSNOWDEN;01,JOEROGAN",
    "14": "00,EDWARDSNOWDEN;01,JOEROGAN",
    "15": "00,EDWARDSNOWDEN",
    "16": "01,EDWARDSNOWDEN;00,JOEROGAN",
    "17": "00,EDWARDSNOWDEN;01,JOEROGAN"
}

replacer_dict["JRE-edwardSnowden-23102019"] = to_replace_dict

to_replace_dict = {
    "1": "01,JOEYDIAZ;02,JOEROGAN",
    "2": "00,JOEYDIAZ;01,JOEROGAN",
    "3": "00,JOEYDIAZ;01,JOEROGAN",
    "4": "01,JOEYDIAZ;00,JOEROGAN",
    "5": "02,JOEYDIAZ;01,JOEROGAN",
    "6": "02,JOEYDIAZ;03,JOEROGAN",
    "7": "00,JOEYDIAZ;01,JOEROGAN",
    "8": "00,JOEYDIAZ;01,JOEROGAN",
    "9": "01,JOEYDIAZ;00,JOEROGAN",
    "10": "00,JOEYDIAZ;01,JOEROGAN",
    "11": "00,JOEYDIAZ;02,JOEROGAN",
    "12": "01,JOEYDIAZ;00,JOEROGAN",
    "13": "01,JOEYDIAZ;02,JOEROGAN",
    "14": "02,JOEYDIAZ;00,JOEROGAN",
    "15": "01,JOEYDIAZ;00,JOEROGAN",
    "16": "00,JOEYDIAZ;01,JOEROGAN",
    "17": "00,JOEYDIAZ",
    "18": "00,JOEYDIAZ;01,JOEROGAN"
}

replacer_dict["JRE-joeyDiaz-26032020"] = to_replace_dict

to_replace_dict = {
    "1": "",
    "2": "00,KANYEWEST;01,JOEROGAN",
    "3": "01,KANYEWEST",
    "4": "00,KANYEWEST;01,JOEROGAN",
    "5": "01,KANYEWEST;00,JOEROGAN",
    "6": "01,KANYEWEST;00,JOEROGAN",
    "7": "01,KANYEWEST;00,JOEROGAN",
    "8": "01,KANYEWEST;00,JOEROGAN",
    "9": "00,KANYEWEST;01,JOEROGAN",
    "10": "01,KANYEWEST;00,JOEROGAN",
    "11": "02,KANYEWEST;00,JOEROGAN",
    "12": "00,KANYEWEST",
    "13": "01,KANYEWEST;00,JOEROGAN",
    "14": "01,KANYEWEST;00,JOEROGAN",
    "15": "00,KANYEWEST;01,JOEROGAN",
    "16": "02,KANYEWEST;00,JOEROGAN",
    "17": "01,KANYEWEST;00,JOEROGAN",
    "18": "02,KANYEWEST;00,JOEROGAN"
}

replacer_dict["JRE-kanyeWest-24102020"] = to_replace_dict

to_replace_dict = {
    "1": "00,JOEROGAN;01,MIKETYSON",
    "2": "00,MIKETYSON;01,JOEROGAN",
    "3": "00,MIKETYSON;01,JOEROGAN",
    "4": "00,JOEROGAN;01,MIKETYSON",
    "5": "00,MIKETYSON;01,JOEROGAN",
    "6": "00,MIKETYSON;01,JOEROGAN",
    "7": "00,MIKETYSON;01,JOEROGAN",
    "8": "00,JOEROGAN;01,MIKETYSON",
    "9": "00,JOEROGAN;01,MIKETYSON",
    "10": "00,JOEROGAN;01,MIKETYSON",
    "11": "00,JOEROGAN;01,MIKETYSON",
    "12": "00,MIKETYSON;01,JOEROGAN"
}

replacer_dict["JRE-mikeTyson-04092020"] = to_replace_dict

to_replace_dict = {
    "1": "00,JOEROGAN;01,MILEYCYRUS",
    "2": "00,JOEROGAN;01,MILEYCYRUS",
    "3": "00,MILEYCYRUS;01,JOEROGAN",
    "4": "00,MILEYCYRUS;01,JOEROGAN",
    "5": "00,MILEYCYRUS;01,JOEROGAN",
    "6": "00,MILEYCYRUS;01,MILEYCYRUS;02,MILEYCYRUS;03,JOEROGAN",
    "7": "00,MILEYCYRUS;01,JOEROGAN",
    "8": "00,JOEROGAN;01,MILEYCYRUS",
    "9": "00,MILEYCYRUS;01,JOEROGAN",
    "10": "00,JOEROGAN;01,MILEYCYRUS",
    "11": "00,JOEROGAN;01,MILEYCYRUS",
    "12": "00,MILEYCYRUS;01,JOEROGAN",
    "13": "00,JOEROGAN;01,MILEYCYRUS"
}

replacer_dict["JRE-mileyCirus-02092020"] = to_replace_dict

to_replace_dict = {
    "1": "00,NEILDEGRASSE;01,JOEROGAN",
    "2": "00,NEILDEGRASSE;01,JOEROGAN",
    "3": "00,NEILDEGRASSE;01,NEILDEGRASSE;02,NEILDEGRASSE",
    "4": "00,NEILDEGRASSE;01,JOEROGAN",
    "5": "00,JOEROGAN;01,NEILDEGRASSE",
    "6": "00,JOEROGAN;01,NEILDEGRASSE",
    "7": "00,NEILDEGRASSE;01,JOEROGAN",
    "8": "00,NEILDEGRASSE;01,JOEROGAN",
    "9": "00,JOEROGAN;01,NEILDEGRASSE",
    "10": "00,JOEROGAN;01,NEILDEGRASSE",
    "11": "00,NEILDEGRASSE;01,JOEROGAN",
    "12": "00,NEILDEGRASSE;01,JOEROGAN",
    "13": "00,NEILDEGRASSE;01,JOEROGAN",
    "14": "00,NEILDEGRASSE;01,NEILDEGRASSE;02,JOEROGAN"
}

replacer_dict["JRE-neildeGrasseTyson-06092019"] = to_replace_dict

to_replace_dict = {
    "1": "00,KEVINHART;01,JOEROGAN",
    "2": "00,KEVINHART;01,JOEROGAN",
    "3": "00,KEVINHART;01,JOEROGAN",
    "4": "00,JOEROGAN;01,KEVINHART",
    "5": "00,JOEROGAN;01,KEVINHART",
    "6": "00,KEVINHART;01,JOEROGAN",
    "7": "00,KEVINHART;01,JOEROGAN",
    "8": "00,KEVINHART;01,JOEROGAN",
    "9": "01,KEVINHART;02,JOEROGAN",
    "10": "00,KEVINHART;01,JOEROGAN",
    "11": "00,KEVINHART;01,JOEROGAN",
    "12": "00,KEVINHART;01,JOEROGAN"
}

replacer_dict["JRE-kevinHart-25052020"] = to_replace_dict

to_replace_dict = {
    "1": "00,POSTMALONE;01,JOEROGAN",
    "2": "00,POSTMALONE;01,JOEROGAN",
    "3": "00,POSTMALONE;01,JOEROGAN",
    "4": "00,JOEROGAN;01,POSTMALONE",
    "5": "00,POSTMALONE;01,JOEROGAN",
    "6": "00,JOEROGAN;01,POSTMALONE",
    "7": "00,JOEROGAN;01,POSTMALONE",
    "8": "",
    "9": "00,JOEROGAN;01,POSTMALONE",
    "10": "00,JOEROGAN;01,POSTMALONE",
    "11": "",
    "12": "00,JOEROGAN;01,POSTMALONE",
    "13": "01,POSTMALONE;02,JOEROGAN",
    "14": "00,POSTMALONE;01,JOEROGAN;02,POSTMALONE",
    "15": "00,POSTMALONE;01,POSTMALONE;02,JOEROGAN",
    "16": "00,JOEROGAN;01,POSTMALONE",
    "17": "00,POSTMALONE;01,JOEROGAN;02,POSTMALONE",
    "18": "00,JOEROGAN;01,POSTMALONE",
    "19": "00,POSTMALONE;01,JOEROGAN",
    "20": "01,POSTMALONE;02,JOEROGAN",
    "21": "",
    "22": "00,POSTMALONE;01,POSTMALONE;02,JOEROGAN",
    "23": "00,POSTMALONE;01,JOEROGAN"
}

replacer_dict["JRE-postMalone-29072020"] = to_replace_dict