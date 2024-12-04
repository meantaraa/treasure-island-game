print(r''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# Stage 1: Crossroad
choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right": ').lower()
if choice1 == "left":
    # Stage 2: Lake
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat or "swim" to swim across: ').lower()
    if choice2 == "wait":
        # Stage 3: Island
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors: '
                        'one red, one yellow, and one blue. Which color do you choose? ').lower()
        if choice3 == "yellow":
            # Stage 4: Treasure room
            print("You found the treasure room! But wait... it’s locked. You need a key.")
            choice4 = input('You see three objects nearby: a chest, a tree, and a rock. '
                            'Where do you want to search? Type "chest", "tree", or "rock": ').lower()
            if choice4 == "chest":
                print("The chest is full of gold, but no key. You hear a growl behind you. Game over. 🐉")
            elif choice4 == "tree":
                print("You find a magical key inside a hollow in the tree!")
                # Stage 5: Escape
                choice5 = input('You unlock the treasure room and take the gold. '
                                'Now, you must escape! Do you "run" or "hide"? ').lower()
                if choice5 == "run":
                    print("You sprint to safety with the treasure! You win! 🏆")
                else:
                    print("You try to hide, but the guardians of the treasure find you. Game over. 😨")
            else:
                print("There’s nothing under the rock. Suddenly, the ground shakes, and you fall into a pit. Game over. 🕳️")
        elif choice3 == "red":
            print("It’s a trap! Burned by fire. Game over. 🔥")
        elif choice3 == "blue":
            print("Oops! Eaten by beasts. Game over. 🐾")
        else:
            print("You chose a door that doesn’t exist. Game over. 🚪")
    else:
        print("Attacked by trout. Game over. 🐟")
else:
    # Bonus Stage: Shortcut
    print("You fell into a hole but landed in an underground tunnel. You can still continue!")
    choice_bonus = input('You see two tunnels: one leads to the "forest" and the other to a "cave". Which do you choose? ').lower()
    if choice_bonus == "forest":
        print("You wander into a forest and get lost. Game over. 🌲")
    else:
        print("You find a hidden entrance to the treasure room through the cave. You win! 🏆")
