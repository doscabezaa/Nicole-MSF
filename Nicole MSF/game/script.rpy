init:
    # Declare the characters
    define nicole = Character('Nicole', color="#c8ffc8")
    define brandon = Character('Brandon', color="#c8c8ff")
    define ada = Character('Ada', color="#ffc8c8")
    define brent = Character('Brent', color="#c8c8c8")
    define taxidriver = Character('Taxidriver', color="#c8ffc8")
    define kelly = Character('Kelly', color="#c8c8ff")
    define jaime = Character('Jaime', color="#ffc8c8")
    define e = Character('Eileen', color="#c8c8c8")

label start:
    # Start of the dialogue
    scene bg room
    show eileen happy
    e "You've created a new Ren'Py game."
    e "Add a story, images, and music, and you can present it to the world!"
    # End of the dialogue

return