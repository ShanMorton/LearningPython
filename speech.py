text = """ Now the trumpet summons us again—not as a call to bear arms, though arms we need—not as a call to battle, though embattled we are—but a call to bear the burden of a long twilight struggle, year in and year out, "rejoicing in hope, patient in tribulation"—a struggle against the common enemies of man: tyranny, poverty, disease and war itself. . . .

In the long history of the world, only a few generations have been granted the role of defending freedom in its hour of maximum danger. I do not shrink from this responsibility—I welcome it. I do not believe that any of us would exchange places with any other people or any other generation. The energy, the faith, the devotion which we bring to this endeavor will light our country and all who serve it—and the glow from that fire can truly light the world.

And so, my fellow Americans: ask not what your country can do for you—ask what you can do for your country.

My fellow citizens of the world: ask not what America will do for you, but what together we can do for the freedom of man."""

# this will break the whole text down into strings
# Use """ """ for mulitline text

#print(len(text.split()))

text2 = """ z z y x w a b b c d d e z y z z z z A A Z B Q"""

#create an empty dictionary
word_count = {}

# for each item in the list of words
# if the word shows up more than once, keep a total
# count all the words, if they are upper case, make them
# lower case and count them.
for x in text.lower().split():
    if x in word_count:
        word_count[x] += 1
    else:        
        word_count[x] = 1

print(word_count)
