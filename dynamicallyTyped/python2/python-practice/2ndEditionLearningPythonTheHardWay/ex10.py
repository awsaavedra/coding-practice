tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \not a line."
backslash_cat = "I'm \\a\\ cat."

fat_cat = """
I'll do a list:
\t* I like cat nip
\t* I like fishes
\t* I catnipple \t* poop
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

formatter = "%r %r %r %r"
formatter2 = "%s %s %s %s"
print formatter % (tabby_cat, persian_cat, backslash_cat, fat_cat)
print formatter2 % (tabby_cat, persian_cat, backslash_cat, fat_cat)
#why does %s print the way you want while %r doesn't?
#Use ”’ (triple-single-quote) instead. Can you see 
#why you might use that instead of """?