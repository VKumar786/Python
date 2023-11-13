mydict = {
    'medicine' : 'the science or practice of the diagnosis, treatment, and prevention of disease (in technical use often taken to exclude surgery).',
    'hacker' : 'a person who uses computers to gain unauthorized access to data.',
    'mountain' : 'a large natural elevation of the earths surface rising abruptly from the surrounding level; a large steep hill.',
    'dictionary' : 'a book or electronic resource that lists the words of a language (typically in alphabetical order) and gives their meaning, or gives the equivalent words in a different language, often also providing information about pronunciation, origin, and usage.',
}
print("What Words meaning inside my Dictionary")
for i,key in enumerate(mydict.keys()):
    print(f"{i+1}. {key}")

while True:
    print(f"Meaning is :",mydict[input("Enter the value : ")])
    if input("Press 'q' to quit & 'c' to continue : ") == 'q':
        break
    else:
        continue