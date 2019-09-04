HEX_COLOUR_CODES = {"blue1": "#0000ff", "blue2": "#0000ee",
                    "blue4": "#00008b", "BlueViolet": "#8a2be2",
                    "CadetBlue": "#5f9ea0", "CadetBlue1": "#98f5ff",
                    "CadetBlue2": "#8ee5ee", "CadetBlue3": "#7ac5cd",
                    "cyan1": "#00ffff", "cyan2": "#00eeee"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             HEX_COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
