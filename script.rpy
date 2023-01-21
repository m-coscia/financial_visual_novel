# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define user = Character("You", color="red")
define guide = Character("P")


# The game starts here.

label start:
    $ user = renpy.input("User, enter your name:")
    $ user = user.strip()
    if user == "":
        $ user = "Doe"

    user "Welcome %(user)s!"

    "what do you want to do?"
    menu:
        "steal the money":
            jump choice1
        "give the 5$ back to the old lady":
            jump start

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label choice1:
    play music "audio/Crazy Frog - Axel F (Official Video).mp3"
    user "we did it!"
    return