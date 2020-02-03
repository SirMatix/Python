def reverses():
    string = str(input('please write a sentence you would like to be reversed! '))
    temp = string.split()
    print(temp)
    reverse = []
    for i in temp[::-1]:
        reverse.append(i)
    reverse = " ".join(reverse)
    return reverse

print(reverses())


