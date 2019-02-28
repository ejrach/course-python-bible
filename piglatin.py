
# get sentence from, user
original = input("Please enter a sentence: ").strip().lower()

# split sentence into words
words = original.split()

# loop through the words and convert to pig latin
new_words = []
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]         #consonate position is from the beginning of word until the vowel position
        the_rest = word[vowel_pos:]     #the rest of the word is from the vowel position to end of the word
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# stick words back together, adding a space between each word
output = " ".join(new_words)

# output the final string
print(output)


