#count of the vowels
def countVowelsWay1(word, index, n, result):
    if index == n:
        print("Vowels count is:", result)
        return
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        result += 1
    countVowelsWay1(word, index + 1, n, result)


word = "abcdeefuigh"
countVowelsWay1(word, 0, len(word), 0)

#using backtracing
def countVowelsWay2(word, index, n):
    if index == n:
        return 0
    nextVowelsCount = countVowelsWay2(word, index + 1, n)
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        nextVowelsCount += 1
    return nextVowelsCount


word = "abcdeefuigh"
result = countVowelsWay2(word, 0, len(word))
print("Vowels count is:", result)
