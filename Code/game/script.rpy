# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    import json
# define Alec = Character("Alec",color="e0dbd6",who_outlines=[ (1, "000000") ])
# define Beatrice = Character("Beatrice",color="e0dbd6",who_outlines=[ (1, "00000") ])
# define Chloe = Character("Chloe",color="e0dbd6",who_outlines=[ (1, "000000") ])

#Defining positions
transform left:
        xalign 0.1
        yalign 1.0
transform right:
        xalign 1.2
        yalign 1.0
transform midright:
        xalign 0.8
        yalign 1.0



# The game starts here.
label start:
    scene bg library
    "Librarian" "Yo, kiddos! \"The library\" is only open for 20 more minute\'s, so finish\'s whatever work you have in a speedy manner! And do it quietly! This is a library for peat\'s sake!"(color="e0dbd6",who_outlines=[ (1, "000000") ])
    "Narrator" "Alec, Beatrice and chloe file into the libaray and gather around one of the tables in the corner to brainstorm potential ideas for their presentation."(color="e0dbd6",who_outlines=[ (1, "000000") ])
    "Narrator" "Alec pulls out his laptop while Beatrice grabs a few history books and the pair get to work. Meanwhile, Chloe was slacking off as usual."(color="e0dbd6",who_outlines=[ (1, "000000") ])
    show a ms neutral at left
    "Alec" "Does anyone have any ideas about a possible topic?"(color="e0dbd6",who_outlines=[ (1, "000000") ])
    hide a ms neutral
    show c ms triumphant at left
    "Chloe" "I\'ve got one: today\'s era! We\'re living in it, so there\'s not much to research!"(color="e0dbd6",who_outlines=[ (1, "000000") ])
    hide c ms triumphant
    show a  ms amused at left
    "Alec" "Yeah, I wish. But, unfortunately, we need to choose something from class."(color="e0dbd6",who_outlines=[ (1, "000000") ])
    hide a  ms amused
    show c ms annoyed at left
    "Chloe" "Aww, you\'re no fun! Do you have anything better?"(color="e0dbd6",who_outlines=[ (1, "000000") ])
    hide c ms annoyed
    show a ms intellectual at left
    "Alec" "I was thinking something like the Industrial Revolution."(color="e0dbd6",who_outlines=[ (1, "000000") ])
    hide a ms intellectual
    show c ms bored at left
    "Chloe" "..."(color="e0dbd6",who_outlines=[ (1, "000000") ])
    hide c ms bored
    show a ms annoyed at left
    "Alec" "Just hear me out!"(color="e0dbd6",who_outlines=[ (1, "000000") ])
    show a ms intellectual at left
    "Alec" "There are so many cool inventions that we could talk about. Like the cotton gin! And the steam engine!"(color="e0dbd6",who_outlines=[ (1, "000000") ])
    hide a ms intellectual
    show c ms excited at left
    "Chloe" "Ooh! Steam engine sounds cool. I vote for that idea!"(color="e0dbd6",who_outlines=[ (1, "000000") ])
    show c ms triumphant at left
    "Chloe" "It\'s official. We\'re doing the inbustrial whatever and talking about steam engines!"(color="e0dbd6",who_outlines=[ (1, "000000") ])
    hide c ms triumphant
    show a ms unamused at left
    "Alec" "The Industrial Revolution, you mean."(color="e0dbd6",who_outlines=[ (1, "000000") ])
    with vpunch
    show a ms worried at midright with easeinleft
    show c ms worried at right with easeinright
    "Librarian" "The library is closed. Get up and get out! Now!!"(color="e0dbd6",who_outlines=[ (1, "000000") ])

    # show ms a unamused at left:
    #     zoom 1.0
    # a "You heard that, guys. We are definitely not ready, no thanks to Chloe. We'll have to work a lot this weekend if we want to finish in time."
    # show ms c mischievous at left:
    #     zoom 1.0
    # c "Don't act like you don't love my amazing personality!"
    # show ms c happy smile at left:
    #     zoom 1.0
    # c "I know... how about we meet at someone's house to finish the work?"
    # return
