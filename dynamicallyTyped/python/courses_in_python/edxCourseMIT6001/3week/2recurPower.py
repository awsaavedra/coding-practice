#Write a procedure recurPowerNew which recursively computes exponentials using this idea.

def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    if exp > 0 and (exp%2 == 0):
        return base*recurPowerNew(base, exp-1)
    if exp > 0 and (exp%2 != 0):
        return base*recurPowerNew(base, exp-1)

print recurPowerNew(2,5)
print recurPowerNew(3,3)
