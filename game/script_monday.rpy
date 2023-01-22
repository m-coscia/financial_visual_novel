# The script of the game goes in this file.

#defined actions
transform slep:
    zoom 0.65 ypos 0.40 xpos 0.30 rotate -55.0 rotate_pad True

transform flip:
    xzoom -1.0

transform unflip:
    xzoom 1.0


transform wakeup:
    zoom 1.0 rotate 0.0 ypos 1.2 xpos 0.0

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
image kitchenBac = im.Scale("images/bg kitchen.png", 1920, 1080)

# python variable storing the user's current available money
default bankAcc = 100
# python variable storing boolean variable of whether the user has done groceries
$ shopping = False
default buyBreakfast = False


# The game starts here.
label start: 
    scene cafeBac
    play music "audio/Umineko Episode 1 OST - Novelette.mp3" fadein 2.0 loop
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
    scene roomBac with fade
    #displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    #announces the day
    "Day 1"
    show user sleep at slep
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
            jump outBed_monday

    return


label snooze_monday:
    scene roomBac with fade
    #displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    show user sleep at slep
    "You snoozed your alarm another 3 times before checking the time."
    hide user sleep
    show user surprides at center
    user "\"Sh**, I'm gonna be late!\""
    $ buyBreakfast = True
    #"Better get your morning coffee on your way to work!"
    jump monday_commute

    return

label outBed_monday:   
    scene roomBac with fade
    #displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    show user normal at left
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
            $ buyBreakfast = True
            jump monday_commute

    return

label breakfast_monday:
    scene kitchenBac with fade
    # displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    "You enjoy a croissant and coffee before leaving to catch the bus."
    jump monday_commute
    return

label monday_commute:
    scene transitBac with fade
    # displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    show user surprides at center
    menu:
        "\"I'm really hungry...\"" if buyBreakfast:
            jump buying_breakfast_monday
        "\"Almost there...\"" if buyBreakfast == False:
            jump school_monday
    
    return

label buying_breakfast_monday:
    show user smile
    user "\"I guess I should grab something before my lecture.\""
    scene cafeBac with fade
    # displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    show user normal at left
    #breakfast options
    menu:
        user "\"Hmm, what should I buy?\""

        "A tall latte and a breakfast sandwich from Starbucks - $15":
            $ bankAcc -= 15
            jump school_monday
        "A large coffee and a bagel - $5":
            $ bankAcc -= 5
            jump school_monday
    
    return

label school_monday:
    scene schoolBac with fade
    show text "Savings: $[bankAcc] " at topright
    show user confident at center
    user "\"Better get to my classes...\""

    scene classroomBac with dissolve
    show text "Savings: $[bankAcc] " at topright
    show user glasses
    "You attend your lectures for the day and begin packing up"
    user "*relaxes* What a long day!"
    jump jobretail

    return

label jobretail:
    scene jobretailBac with fade
    show text "Savings: $[bankAcc] " at topright
    show user normal at center
    "After classes end, you head over to your part-time job, where you tend to the local retail store."
    hide user normal
    $ bankAcc += 50
    scene streetBac with fade
    show text "Savings: $[bankAcc] " at topright
    show  user confident at left
    user "What a hard day's work! It was so busy that I skipped my break."

    "You check the time and see that it's a little past supper time."

    menu:
        user "\"What should I do about supper?\""
        "Pickup my groceries and cook supper - $40":
            $ shopping = True
            $ bankAcc -= 40
            jump cookSupper
        "Order Uber Eats for the meal - $30":
            $ bankAcc -= 30
            jump dayEnd_mon
    return

label cookSupper:
    scene kitchenBac with fade
    show text "Savings: $[bankAcc] " at topright
    show  user smile at center

    "After finishing the weekly grocery run, you cook yourself a meal."

    jump dayEnd_mon

    return

label dayEnd_mon:
    scene roomBac with fade
    show text "Savings: $[bankAcc] " at topright
    show  user normal at center
    "You've eaten your supper and are beginning to wind down."
    hide user normal
    show user sleep at slep
    "Time to sleep..."
    jump wed_start
    return


####### WEDNESDAY #######
# initial label for wednesday - this is where the storyline for monday starts
label wed_start:
    scene roomBac with fade
    #displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    #announces the day
    "Day 2"
    show user sleep at slep
    #narration - expedition before first choice
    "Beep beep beep bee-"
    user "*groans* \"Urgh, not again...\""
    "Once again, you are a tired creature of habit - you snooze the alarm."
    # first choice
    menu:
        "[user], the alarm went off again. What will you do now?"
        #option 1
        "Snooze again":
            $ buyBreakfast = True
            jump snooze_wed
        # option 2
        "Get out of bed":
            jump outBed_wed

    return

label snooze_wed:
    scene roomBac with fade
    #displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    show user sleep at slep
    "You snoozed your alarm until you realize you overslept."
    hide user sleep
    show user surprides at center
    user "\"Sh**, I'm gonna be late!\""
    $ buyBreakfast = True
    #"Better get your morning coffee on your way to work!"
    jump wed_commute

    return

label outBed_wed:    
    hide user
    show user normal at left
    "You get ready for the day, leaving you with the hole morning ahead."
    user "*stomach growls*"
    #choice to make
    menu:
        "Maybe you should eat breakfast, [user]."
        #option 1
        "Make myself avocado toast":
            jump breakfast_wed
        #option 2
        "Pick up a meal on the way to school":
            $ buyBreakfast = True
            jump wed_commute

    return

label breakfast_wed:
    scene kitchenBac with fade
    # displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    show user smile at center
    "You enjoy your avocado toast and coffee before walking out the front door to catch the bus."
    jump wed_commute
    return

label wed_commute:
    scene transitBac with fade
    # displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    show user surprides at center
    menu:
        "\"I really hungry...\"" if buyBreakfast:
            jump buying_breakfast_wed
        "\"Almost there...\"" if buyBreakfast == False:
            jump school
    
    return

label buying_breakfast_wed:
    show user smile
    user "\"I guess I should grab something before my lecture.\""
    scene cafeBac with fade
    # displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    show user normal at left
    #breakfast options
    menu:
        user "\"Hmm, what should I buy?\""

        "A tall latte and a breakfast sandwich from Starbucks - $15":
            $ bankAcc -= 15
            jump school
        "A large coffee and a bagel - $5":
            $ bankAcc -= 5
            jump school
    
    return

label school:
    scene schoolBac with fade
    show text "Savings: $[bankAcc] " at topright
    show user confident at center
    user "\"Better get to my classes...\""

    scene classroomBac with dissolve
    show text "Savings: $[bankAcc] " at topright
    show user glasses
    "You attend your lectures for the day and begin packing up"
    user "*relaxes* What a long day!"
    jump study

    return

label study:
    return
