def FancyDivide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError, e:
            FancyDivide(numbers, len(numbers) - 1)
        else:
            print "1"
        finally:
            print "0"
    except ZeroDivisionError, e:
        print "-2"


#print FancyDivide([0, 2, 4], 1)
#print FancyDivide([0, 2, 4], 4)
print FancyDivide([0, 2, 4], 0)
