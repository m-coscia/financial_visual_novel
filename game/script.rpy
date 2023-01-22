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

transform collapse:
    zoom 0.75 ypos 0.20 xpos 0.30 rotate 90 rotate_pad True
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
transform blurr:
    blur 10.0
define user = Character("You", color="#A8B925")

# setting the resolution of the background assets
image blackBac = im.Scale("images/bg black.png", 1920, 1080)
image supperBac = im.Scale("images/bg supper.jpg", 1920, 1080)
image libraryBac = im.Scale("images/bg library.png", 1920, 1080)

image introBac = im.Scale("images/bg intro.jpg", 1920, 1080)
image breakfastBac = im.Scale("images/bg breakfast.png", 1920, 1080)
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
image kitchenBac = im.Scale("images/bg kitchen.jpg", 1920, 1080)

# python variable storing the user's current available money
default bankAcc = 100
# python variable storing boolean variable of whether the user has done groceries
$ shopping = False
default buyBreakfast = False


# The game starts here.
label start:
    scene introBac
    play music "audio/Umineko Episode 1 OST - Novelette.mp3" fadein 2.0 loop
    with fade
    $ user = renpy.input("Hey there, what's your name?")
    $ user = user.strip()
    if user == "":
        $ user = "Doe"
    "Welcome %(user)s to GAM - a Financial Visual Novel."
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
    user "\"Oh no, I'm gonna be late!\""
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
    show user surprised at center
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

        "An iced coffee and a donut from Cafe Van Houtte - $15":
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
    user "What a hard day's work! It was so busy that I skipped my break. On the bright side, I made 50$ today!"

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

    jump eatSupper

    return

label eatSupper:
    scene supperBac with fade
    show text "Savings: $[bankAcc] " at topright

    "You happily eat your meal."

    jump dayEnd_mon

    return

label dayEnd_mon:
    scene roomBac with fade
    show text "Savings: $[bankAcc] " at topright
    show  user normal at center
    "You've eaten your supper and you're beginning to wind down."
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
    "You snooze your alarm until you realize you overslept."
    hide user sleep
    show user surprides at center
    user "\"Oh np, I'm gonna be late!\""
    $ buyBreakfast = True
    #"Better get your morning coffee on your way to work!"
    jump wed_commute

    return

label outBed_wed:
    hide user
    show user normal at left
    "You get ready for the day, leaving you with the entire morning ahead."
    user "*stomach growls*"
    #choice to make
    menu:
        "Maybe you should eat breakfast, [user]."
        #option 1
        "Make myself pancakes and coffee":
            jump breakfast_wed
        #option 2
        "Pick up a quick breakfast on the way to school":
            $ buyBreakfast = True
            jump wed_commute

    return

label breakfast_wed:
    scene breakfastBac with fade
    # displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    "You enjoy your homemade pancakes with syrup and coffee before walking out the front door to catch the bus."
    jump wed_commute
    return

label wed_commute:
    scene transitBac with fade
    # displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    show user surprides at center
    menu:
        "\"I'm really hungry...\"" if buyBreakfast:
            jump buying_breakfast_wed
        "\"Almost there...\"" if buyBreakfast == False:
            jump school

    return

label buying_breakfast_wed:
    show user smile
    user "\"I guess I should grab something before my lecture starts.\""
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
    "You attend your lectures for the day and begin packing up."
    user "*relaxes* What a long day!"
    jump study

    return

label study:
    scene libraryBac with fade
    show text "Savings: $[bankAcc] " at topright
    show user glasses at center
    "You head to the library to power through a last minute essay."
    user "\"Let's hit the books!\""
    "After progressing, you decide to take a break. You decide to check your phone."
    hide user glasses at center
    show user surprides at left
    "Wait a minute, [user]!"

    menu:
        "The concert tickets of your favourite artisit have gone on sale!"
        "Buy the concert tickets right now! - $150":
            $ bankAcc -= 150
            jump delay_study
        "Decide against it and go back to studying":
            jump leave_lib
    
    return
    
label delay_study:
    scene libraryBac with fade
    show text "Savings: $[bankAcc] " at topright
    show user confident at center
    "Happy having snagged some tickets, you are grinning ear to ear."
    hide user confident
    show user surprides at center
    user "Shoot! I need to finish essay!"
    "And with that, you put your head back to the grindstone."
    jump leave_lib
    return

label leave_lib:
    scene streetBac with fade
    show text "Savings: $[bankAcc] " at topright
    show user smile at center
    "Now that you have finished your essay, you think to yourself"
    #user "What should I do with the time I can kill before going home?"
    menu:
        "How should you spend your time before going home?"
        "Buy groceries for the week on the way back - $40" if shopping == False:
            $ bankAcc -= 40
            jump get_home
        "Walk to the park on the way home" if shopping == True or shopping == False:
            jump park
    return

label get_home:
    scene kitchenBac with fade
    show text "Savings: $[bankAcc] " at topright
    show user smile at center

    "After eating, you wind down with some video games"
    jump gaming
    return

label park:
    scene parkBac with fade
    show text "Savings: $[bankAcc] " at topright
    show user smile at center

    "You pass by the scenery and admire in awe as you walk home"
    jump get_home

    return

label gaming:
    scene roomBac with fade
    show text "Savings: $[bankAcc] " at topright
    show user gamer at center

    user "\"Haha, game go brrrrrr so easy\""

    "Then a pop-up appears..."

    menu:
        "To celebrate the ten year aniversaty of the game, the fighting pass is on sale for half the usual price this week-end ! do you buy it ?"

        "Buy the pass and obtain 19 free skins (12.5$)":
            $ bankAcc -= 12.5
            #displays current bank balance the user has
            show text "Savings: $[bankAcc] " at topright
            user "Damn, these skins really do look amazing, I can now play as One Naruto Z"
        "Keep playing for free with the same enjoyment":
            show user smile
            user "That was fun ! I'm glad that i didn't get tempted by those in-game purchases !"
    jump end_wed
    return

label end_wed:
    scene roomBac with fade
    show text "Savings: $[bankAcc] " at topright
    show  user normal at center
    "You've eaten your supper and are beginning to wind down."
    hide user normal
    show user sleep at slep
    "Time to sleep..."
    jump SatMorn
    return

########## SATURDAY ############

label SatMorn:

    scene roomBac
    #displays current bank balance the user has
    show text "Savings: [bankAcc]$ " at topright
    play music "audio/Umineko Episode 1 OST - Towering Cloud in Summer.mp3" fadeout 2.0 fadein 5.0 loop

    show user sleep at slep

    "you wake up now, it is now Saturday."

    show user normal at left,wakeup with fade

    user "..."
    user "finally got some sleep..."

    show shadow at right with fade
    play music "audio/Umineko Episode 1 OST - Suspicion.mp3" fadeout 2.0 fadein 1.0 loop
    "you recieve a message form your friend"
    
    "they invite you to attend hang out in a bar in the evening"

    menu:
        "respond with \"HELL YEAH BROTHA\"":
            stop music fadeout 2.0
            hide shadow
            jump SatGoParty
            
            
        "tell him you don't want to go right now":
            stop music fadeout 2.0
            hide shadow
            jump SatActivity

    return


label SatGoParty:
    "You spend some time preparing yourself to go out"
    play music "audio/1.Pursuing My True Self(P4).mp3" fadein 2.0
    play sound "audio/Cartoon Running.mp3"
    pause 0.5

    hide user

    show user confident at right with moveinleft

    play sound "audio/B1.WAV"
    scene streetBac with fade
    play sound "audio/B1.WAV"
    scene transitBac with fade
    play sound "audio/B1.WAV"
    scene downtownBac with fade
    play sound "audio/B1.WAV"
    scene partyBac with fade
    play sound "audio/B5.WAV"
    #displays current bank balance the user has
    show text "Savings: $[bankAcc] " at topright
    
    show user confident at left with moveinleft
    pause 0.4
    play sound "audio/B1.WAV"
    show user confident at flip
    pause 0.4
    play sound "audio/B1.WAV"
    show user confident at unflip

    play sound "audio/B5.WAV"
    show user confident at right with moveinleft

    pause 0.4
    play sound "audio/B1.WAV"
    show user confident at flip
    pause 0.4
    play sound "audio/B1.WAV"
    show user confident at unflip

    play sound "audio/B5.WAV"
    show user confident at left with moveinleft

    play sound "audio/1.wav"
    pause 2.0

    show shadow at right with moveinleft

    "friend" "amazing moves dude, let's keep this night great, come drink with me !"

    menu: 
        "go for a drink ! (20$)":
            $ bankAcc -= 20.0
            #displays current bank balance the user has
            show text "Savings: $[bankAcc] " at topright
            play sound "audio/Minecraft Potion Drinking).mp3" volume 10.0
            pause 2.0
            menu:
                "amazing dude ! let's go for another round !"

                "go for it (25$)":
                    $ bankAcc -= 25.0
                    #displays current bank balance the user has
                    show text "Savings: $[bankAcc] " at topright
                    play sound "audio/Minecraft Potion Drinking).mp3" volume 10.0
                    pause 2.0
                    play sound "audio/B5.WAV" volume 5.0
                    show user confident at right with moveinleft
                    pause 0.4
                    play sound "audio/B1.WAV" volume 5.0
                    show user confident at flip
                    pause 0.4
                    play sound "audio/B1.WAV" volume 5.0
                    show user confident at unflip

                    play sound "audio/B5.WAV" volume 5.0
                    show user confident at left with moveinleft
                    menu: 
                        "SUUUPEEERR ! One last one ! MAN OF THE NNIGHT !"
            
                        "drink it all (50$)":
                            $ bankAcc -= 50.0
                            #displays current bank balance the user has
                            show text "Savings: $[bankAcc] " at topright
                            play sound "audio/Minecraft Potion Drinking).mp3" volume 10.0
                            pause 2.0
                            pause 1.0
                            show user confident at flip
                            pause 0.4
                            show user confident at unflip

                            show user confident at collapse with fade 
                            play sound "audio/body hitting.mp3" volume 30.0
                            pause 2.0
                            jump finalDayDrunk
                        
                        "I... Really think I can't keep going...":
                            show user confident at collapse with fade 
                            play sound "audio/body hitting.mp3" volume 30.0
                            pause 2.0
                            jump finalDayDrunk
                            return


                "stop here, you've had your fun":
                    user "one drink is enough for me, now watch this ! "
                    pause 0.4
                    play sound "audio/B1.WAV"
                    show user confident at flip
                    pause 0.4
                    play sound "audio/B1.WAV"
                    show user confident at unflip

                    pause 0.4
                    play sound "audio/03.wav"
                    show user with vpunch
                    
                    pause 0.4
                    play sound "audio/B5.WAV"
                    show user confident at flip
                    pause 0.4
                    play sound "audio/B5.WAV"
                    show user confident at unflip
                    
                    play sound "audio/1.wav"
                    pause 2.0   
                    jump SatSleep
                    return

        "nah man, i'm only here to move to the beat !":
            #DO THIS
            pause 0.4
            play sound "audio/B1.WAV"
            show user confident at flip
            pause 0.4
            play sound "audio/B1.WAV"
            show user confident at unflip

            pause 0.4
            play sound "audio/03.wav"
            show user with vpunch
            
            pause 0.4
            play sound "audio/B5.WAV"
            show user confident at flip
            pause 0.4
            play sound "audio/B5.WAV"
            show user confident at unflip
            play sound "audio/1.wav"
            pause 2.0



            jump SatSleep


    
    return


label SatActivity:
    "you decide to stay at home and spend the time relaxing"

    menu:
        "What should you do ?"

        "Read a book.":
            jump SatReading
        "Play video games":
            jump SatGamer
    return

label SatReading:
    show user reading
    user "The mystery in this book is amazing, so many aspecs to keep track of, and they all connect and solve each other, truly a splendid work!"
    jump SatSleep
    return

label SatGamer:
    show user gamer
    user "\"Haha, game go brrrrrr so easy\""

    "Then a pop-up appears..."

    menu:
        "To celebrate the ten year aniversaty of the game, the fighting pass is on sale for half the usual price this week-end ! do you buy it ?"

        "Buy the pass and obtain 19 free skins (12.5$)":
            $ bankAcc -= 12.5
            #displays current bank balance the user has
            show text "Savings: $[bankAcc] " at topright
            user "damn, these skins really do look amazing, I can now play as One Naruto Z"
        "Keep playing for free with the same enjoyment":
            show user smile
            user "that was fun ! I'm glad that i didn't get tempted by those in-game purchases !"
    jump SatSleep
    return


label SatSleep:

    scene roomBac
    hide user
    show user sleep at slep
    "time to go sleep Zz...."
    scene blackBac 
    pause 3.0
    jump finalday
    return

label finalday:
    scene roomBac
    show user sleep at slep
    "as sunlight slowly started reaching my demeure, I started to come awake"
    "yesterday was quite a fun day "
    
    jump finaltally
    return

label finalDayDrunk:
    scene blackBac
    pause 3.0
    scene roomBac
    show user sleep at slep 

    user "what is this note ?"

    "note" "hey man, it's me, yesterday was amazing man you were the star of the night man ! hope getting that much to drink didn't mess you up too bad"

    "as I slowly start recalling what happened last night, a sudden realisation started to hit me."
    "I had been horrendously reckless last night."
    jump finaltally
    return

    label finaltally:
        if bankAcc >= 100:
            "I did amazing this week with my finances. I am responsible and conscious of what spendings!" 
        if (bankAcc >=50 and bankAcc < 100):
            "I did pretty well this week. I can always improve and manage my money better."
        if (bankAcc >=15 and bankAcc < 50):
            "I did pretty poorly this week" 
        if bankAcc < 15:
            "I did not do well. "  
        
        
        return

