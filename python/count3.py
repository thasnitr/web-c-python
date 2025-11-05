s=input("Enter a sentence:")
print(s)
wordlist=s.split()
print(wordlist)
uniquewords=set(wordlist)
for word in uniquewords:
    print(f"{word} occurs {wordlist.count(word)} times")
