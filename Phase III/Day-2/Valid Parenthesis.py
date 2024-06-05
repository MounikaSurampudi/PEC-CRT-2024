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

#or

def printValidOnes(opened_ones, closed_ones, ans, result):
    if opened_ones == 0 and closed_ones == 0:
        result.append(ans)
        return
    if opened_ones != 0:
        printValidOnes(opened_ones - 1, closed_ones, ans + '(', result)

    if closed_ones != 0 and closed_ones > opened_ones:
        printValidOnes(opened_ones, closed_ones - 1, ans + ')', result)


n = int(input())
result = []
opened_ones = n
closed_ones = n
ans = ""
printValidOnes(opened_ones, closed_ones, ans, result)
for i in result:
    print(i)
print()
