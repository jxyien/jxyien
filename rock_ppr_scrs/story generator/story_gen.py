import random 
# importing random module to take random strings to create story.

when = ['One day', "One night", "Long ago", "Long long ago", "One fine evening", "One sunny day"] # when did it happen
who =  [" Jamie ", " Superman ", " Captain america ", " Bill Gates ", " David Goggins ", " Madhu "] # protagonist
what = ["saved a cat from a tree ", "did 25 squats ", "took his pills on time ", "finished his latest AI model ", "bought an XBOX series S ", "bought a new pair of headsets "] # what did he do?
using = ["hands", "legs", "credit card", "grandpa's old walking stick", "dumbbells", "his first slipper", "landline phone", "lenovo laptop"] # how did he do it?

# using random.choice() function to pick random options from the tables and create a story.

# I have used extra elements to the story like ",", "using his", "." to create realism and grammatical improvements.

print(random.choice(when) + "," + random.choice(who) + random.choice(what) + "using his " + random.choice(using) + ".")

# end