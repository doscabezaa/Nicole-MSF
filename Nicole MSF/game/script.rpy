init:
    # Declare the money variable
    default money = 0
    default corruption = 0
    default innocence = 100
    
    # Declare the characters
    define nicole = Character('Nicole', color="#c8ffc8")
    define brandon = Character('Brandon', color="#c8c8ff")
    define ada = Character('Ada', color="#ffc8c8")
    define brent = Character('Brent', color="#c8c8c8")
    define taxidriver = Character('Taxidriver', color="#c8ffc8")
    define kelly = Character('Kelly', color="#c8c8ff")
    define jaime = Character('Jaime', color="#ffc8c8")

label start:
    # Start of the dialogue
    scene bg citytaxi
    nicole "Now that I think about it, accepting your proposal wasn’t a bad idea. God! The buildings are huge, they seem to touch the sky."
    brandon "Wait till you see dad’s house. You’ll love it, it’s awesome."
    "Phone vibration, someone has sent you 100 bills"
    # Create a button
    $ quick_menu = False
    menu:
        "Recive":
            $ money += 100
            jump cobro_scene
        "Denied":
            $ money += 0
    jump cobro_scene
    label cobro_scene:
    nicole "It’s a pity you’re away. I would have liked to spend more time with you. We hardly see each other because of your work. Is something wrong, honey? Your voice sounds agitated."
    # Brandon was standing in front of an unknown woman, Ana.
    brandon "No, it’s okay, love. I’m just busy serving customers. We’ll talk later, honey. Dad will be home to help you with the suitcase."
    taxidriver "We have arrived."
    nicole "How much is it."
    taxidriver "35 bills."
    # Create a button
    $ quick_menu = False
menu:
    "Pay":
        if money >= 35:
            $ money -= 35
            taxidriver "Good girl."
            jump entrance_scene
    "Don't Pay":
        taxidriver "No have money, give me a blobjob."
        $ corruption += 1
        $ innocence -= 1
        jump entrance_scene
label entrance_scene:
    scene bg entrance
    brent "Damn! My son has good taste. He just thinks, Brent."
    call screen show_stats
    brent "Welcome to your humble home. I hope you feel comfortable here."
    nicole "Thank you Mr. Brent!"
    brent "Brent, just Brent. You must be exhausted from the trip."
    nicole "These have been difficult days for me. My mom passed away and my dad is an alcoholic."
    brent "I’m so sorry about your mom, Nicole. And I’m so sorry about what you’re going through with your father. But here you will be safe and protected. You can count on me for whatever you need."
    nicole "Thanks, Brent. It’s comforting to know that I have someone to trust. I don’t know how to thank you for opening the doors of your home to me."
    brent "You don’t have to thank me, Nicole. You are special to me and I want you to feel comfortable here. Come, I’ll show you your room."
    scene bg nicoleroom
    nicole "Wow this room is amazing. I can’t believe I’m going to live here. I’m very grateful, Brent."
    brent "I’m glad you like it, Nicole. I want you to feel at home. If you need anything, don’t hesitate to tell me. I am here to help you."
    # End of the dialogue
return
