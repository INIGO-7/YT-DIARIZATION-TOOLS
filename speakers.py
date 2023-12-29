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
    "1": "00,MRBEAST;01,LEXFRIDMAN",
    "2": "00,MRBEAST;01,LEXFRIDMAN",
    "3": "00,LEXFRIDMAN;01,MRBEAST",
    "4": "00,MRBEAST;01,LEXFRIDMAN",
    "5": "00,MRBEAST;01,LEXFRIDMAN",
    "6": "00,MRBEAST;01,LEXFRIDMAN",
    "7": "00,LEXFRIDMAN;01,MRBEAST",
    "8": "00,MRBEAST;01,LEXFRIDMAN",
    "9": "00,MRBEAST;01,LEXFRIDMAN",
    "10": "00,MRBEAST;01,LEXFRIDMAN",
    "11": "00,LEXFRIDMAN;01,MRBEAST",
    "12": "00,LEXFRIDMAN;01,MRBEAST",
    "13": "00,LEXFRIDMAN;01,MRBEAST",
    "14": "00,LEXFRIDMAN;01,MRBEAST"
}

replacer_dict["lexFridman-mrBeast-11012023"] = to_replace_dict

to_replace_dict = {
    "1": "01,HUBERMAN",
    "2": "00,HUBERMAN",
    "3": "01,HUBERMAN",
    "4": "00,HUBERMAN",
    "5": "02,HUBERMAN;01,ANDREW",
    "6": "01,HUBERMAN;00,ANDREW",
    "7": "01,HUBERMAN",
    "8": "01,HUBERMAN;02,ANDREW",
    "9": "01,HUBERMAN;00,ANDREW",
    "10": "02,HUBERMAN;03,ANDREW",
    "11": "02,HUBERMAN;01,ANDREW",
    "12": "00,HUBERMAN",
    "13": "00,HUBERMAN;01,ANDREW"
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