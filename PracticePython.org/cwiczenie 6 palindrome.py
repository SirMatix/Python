text=input("Please enter a sentence: ")
text=str(text)
txet=text[::-1]
print(txet)
if text == txet:
    print("This sentence is a palindrome")
else:
    print("This sentnece is not a palindrome")
