def printThis(n, result, openOnes, closedOnes):
    if closedOnes > openOnes:
        return
    if openOnes > (n // 2) or closedOnes > (n // 2):
        return
    if len(result) == n:
        print(result)
        return 
 
    printThis(n, result + "(", openOnes + 1, closedOnes)
    printThis(n, result + ")", openOnes, closedOnes + 1)
 
 
n = 6
printThis(n, "", 0, 0)
