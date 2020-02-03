def palindrome(string):
    if string % len(string) == 1:
        if string[0,len(string)] == string[-1:-len(string)]:
            return True
    else:
        return False
paliCheck = str(input("Podaj wyraz który chcesz sprawdzic: "))

print(palindrome(paliCheck))
