def printThis(position):
    print("Leaving here",position)
    if position==0:
        print("Base condition got hit")
        return
    if position%2==1:
        print("Even position:",position)
    else:
        print("Odd position",position)
    printThis(position-1)
    for index in range(position,-1,-1):
        print("Index is:",index)
    print("Entering here",position)
printThis(11)
