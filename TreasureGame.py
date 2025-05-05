
def mission_treasure():
    print("Welcome to the Treasure Island. Your mission is to find your Treasure")

    DecisionOne = input("Choose left(L) or Right(R) ??-:")
    if DecisionOne != 'l':
        print("You fallen into the hole. Game Over!!")
        return

    DecisionTwo = input("Choose to Swim(S) or Wait(W) ??-:")
    if DecisionTwo != 'w':
        print("You are attached by trout. Game Over!!")
        return
    
    DecisionThree = input("Choose which door you want to enter: 1.Red(r) 2.Yellow(y) 3.Blue(b) ")
    if DecisionThree == 'r':
        print("You are burned by fire. Game Over!!")
    elif DecisionThree == 'b':
        print("You are eaten by beasts. Game Over!!")
    elif DecisionThree == 'y':
        print("You Won!!")
    else:
        print("Invalid Choice!!. Game Over!")

mission_treasure()
  
        

