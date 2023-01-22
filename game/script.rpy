# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define user = Character("You", color="#A8B925")

# setting the resolution of the background assets
image cafeBac = im.Scale("images/bg cafe.jpg", 1920, 1080)
image classroomBac = im.Scale("images/bg classroom.png", 1920, 1080)
image depanneurBac = im.Scale("images/bg depanneur.png", 1920, 1080)
image downtownBac = im.Scale("images/bg downtown.jpg", 1920, 1080)
image hallwayBac = im.Scale("images/bg hallway.jpg", 1920, 1080)
image jobretailBac = im.Scale("images/bg jobretail.jpg", 1920, 1080)
image mallBac = im.Scale("images/bg mall.jpg", 1920, 1080)
image parkBac = im.Scale("images/bg park.jpg", 1920, 1080)
image partyBac = im.Scale("images/bg party.jpg", 1920, 1080)
image restaurentBac = im.Scale("images/bg restaurent2.jpg", 1920, 1080)
image roomBac = im.Scale("images/bg room.png", 1920, 1080)
image schoolBac = im.Scale("images/bg school.jpg", 1920, 1080)
image streetBac = im.Scale("images/bg street.jpg", 1920, 1080)
image transitBac = im.Scale("images/bg transportation.jpg", 1920, 1080)

# python variable storing the user's current available money
default bankAcc = 100
# python variable storing boolean variable of whether the user has done groceries
$ shopping = False
$ buyBreakfast = False


# The game starts here.
label start: 
    show roomBac
    with fade
    $ user = renpy.input("Hey there, what's your name?")
    $ user = user.strip()
    if user == "":
        $ user = "Doe"
    "Welcome %(user)s to GAM - a financial visual novel."
    "This game will let you experience a simulated version of your university life."
    "Based on the choices you make, you will be able to determine how well you currently manage your personal finances."
    "Make sure to answer as honestly as possible!"

    jump monday_start

    return
    
# initial label for monday - this is where the storyline for monday starts
label monday_start:
    show roomBac
    with fade
    #displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    #announces the day
    "Monday"
    show user sleep at right
    #narration - expedition before first choice
    "Beep beep beep bee-"
    user "*groans* \"Urgh, just 5 more minutes...\""
    "You reach for your phone and snooze your alarm."
    # first choice
    menu:
        "[user], the alarm went off again. What will you do now?"
        #option 1
        "Snooze again":
            $ buyBreakfast = True
            jump snooze_monday
        # option 2
        "Get out of bed":
            hide user sleep
            jump outBed_monday

    return


label snooze_monday:
    "You snoozed you alarm another 3 times before checking the time."
    show user surprides at center
    user "\"Sh**, I'm gonna be late!\""
    #"Better get your morning coffee on your way to work!"
    jump monday_commute

    return

label outBed_monday:
    show roomBac
    with fade
    show user normal at right
    "You get ready for the day and have half an hour to spare."
    user "*stomach growls*"
    #choice to make
    menu:
        "Maybe you should eat breakfast, [user]."
        #option 1
        "Make myself breakfast":
            jump breakfast_monday
        #option 2
        "Pick up breakfast on the way to school":
            jump monday_commute

    return

label breakfast_monday:
    "You enjoy a croissant and coffee before leaving to catch the bus."
    jump monday_commute
    return

label monday_commute:
    show transitBac

    if buyBreakfast:
        user "\"I guess I should grab something before my lecture.\""
        jump monday_commute
    
    return














label monday_choice1a:
    show cafeBac
    show text "Savings: $[bankAcc] " at topright
    "damn, i feel bad"
    return
label monday_choice1b:
    show cafeBac
    show text "Savings: $[bankAcc] " at topright
    "honesty is the best policy"
    return 



label wednesday:
    play music "audio/Crazy Frog - Axel F (Official Video).mp3"
    user "we did it!"
    return