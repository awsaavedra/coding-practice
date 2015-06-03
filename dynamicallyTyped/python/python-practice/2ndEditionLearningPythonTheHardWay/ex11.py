print "How tall are you?"
height = raw_input()
print "What is your age?"
age = raw_input()
print "How much do you weigh?"
weight = raw_input()

output = "So you are %r tall, weigh %r much, and are %r old? Cool."
print output %( height, age, weight)


# 1. Go online and find out what Python’s raw_input does.
# 2. Can you find other ways to use it? Try some of the samples you find.
# 3. Write another “form” like this to ask some other questions.
# 4. Related to escape sequences, try to find out why the last line has ’6\’2"’ with that \’ sequence.
# See how the single-quote needs to be escaped because otherwise it would end the string?
