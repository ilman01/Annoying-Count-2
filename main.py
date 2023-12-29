import random
import math
import sympy

target = int(input("Input Number: "))
length = int(input("Input Length (Recommended: 40): "))

listOfNumbers = []

for i in range(length):

    randomMode = random.randint(1,2)

    if randomMode == 1: # Plus
        randomNumber = round(random.uniform(1, 1000), 2)
        listOfNumbers.append(randomNumber)
    
    if randomMode == 2: # Minus
        randomNumber = round(random.uniform(-1000, -1), 2)
        listOfNumbers.append(randomNumber)



listOfNumbersWithString = listOfNumbers.copy()

for i in range(random.randint(len(listOfNumbersWithString) - 20, len(listOfNumbersWithString))):
    print("Executed" + str(i))

    randomMode = random.randint(1,6)
    randomIndex = random.randint(0, len(listOfNumbersWithString) - 1)
    Minus = False

    if type(listOfNumbersWithString[randomIndex]) == str: # If already converted, skip to the next iteration
        continue
    if listOfNumbersWithString[randomIndex] < 0: # If the number is a negative
        listOfNumbersWithString[randomIndex] = listOfNumbersWithString[randomIndex] * -1
        Minus = True

    if randomMode == 1: # square root
        listOfNumbersWithString[randomIndex] = "(sqrt(" + str(round((listOfNumbersWithString[randomIndex] ** 2),8)) + "))"
        if Minus == True:
            listOfNumbersWithString[randomIndex] = "-" + listOfNumbersWithString[randomIndex]
        else:
            listOfNumbersWithString[randomIndex] = "+" + listOfNumbersWithString[randomIndex]

    if randomMode == 2: # square
        listOfNumbersWithString[randomIndex] = "(" + str(round(math.sqrt(listOfNumbersWithString[randomIndex]),8)) + "^2)"
        if Minus == True:
            listOfNumbersWithString[randomIndex] = "-" + listOfNumbersWithString[randomIndex]
        else:
            listOfNumbersWithString[randomIndex] = "+" + listOfNumbersWithString[randomIndex]

    if randomMode == 3: # cubic root
        listOfNumbersWithString[randomIndex] = "(cbrt(" + str(round((listOfNumbersWithString[randomIndex] ** 3),8)) + "))"
        if Minus == True:
            listOfNumbersWithString[randomIndex] = "-" + listOfNumbersWithString[randomIndex]
        else:
            listOfNumbersWithString[randomIndex] = "+" + listOfNumbersWithString[randomIndex]

    if randomMode == 4: # cubic
        listOfNumbersWithString[randomIndex] = "(" + str(round(math.cbrt(listOfNumbersWithString[randomIndex]),8)) + "^3)"
        if Minus == True:
            listOfNumbersWithString[randomIndex] = "-" + listOfNumbersWithString[randomIndex]
        else:
            listOfNumbersWithString[randomIndex] = "+" + listOfNumbersWithString[randomIndex]

    #if randomMode == 5: # times
    #    randomDiv = round(random.uniform(1,100),3)
    #    listOfNumbersWithString[randomIndex] = "(" + str(randomDiv) + "*" + str(round(listOfNumbersWithString[randomIndex] / randomDiv,8)) + ")"
    #    if Minus == True:
    #        listOfNumbersWithString[randomIndex] = "-" + listOfNumbersWithString[randomIndex]
    #    else:
    #        listOfNumbersWithString[randomIndex] = "+" + listOfNumbersWithString[randomIndex]
        

    if randomMode == 5: # divide
        randomTimes = round(random.uniform(1,100),3)
        listOfNumbersWithString[randomIndex] = "(" + str(round(listOfNumbersWithString[randomIndex] * randomTimes,8)) + "/" + str(randomTimes) + ")"
        if Minus == True:
            listOfNumbersWithString[randomIndex] = "-" + listOfNumbersWithString[randomIndex]
        else:
            listOfNumbersWithString[randomIndex] = "+" + listOfNumbersWithString[randomIndex]
    
    if randomMode == 6: # modulo
        targetVal = listOfNumbersWithString[randomIndex]

        denominator = targetVal + 1

        randomMultiplication = random.randint(5,8)
        nominator = round(targetVal + denominator * randomMultiplication,4)

        randomConfuseDenominator = round(random.uniform(1, denominator-1),2)
        stringRandomConfuseDenominator = str(round(denominator - randomConfuseDenominator,2)) + "+" + str(randomConfuseDenominator)

        listOfNumbersWithString[randomIndex] = f"({nominator}%({stringRandomConfuseDenominator}))"

        if Minus == True:
            listOfNumbersWithString[randomIndex] = "-" + listOfNumbersWithString[randomIndex]
        else:
            listOfNumbersWithString[randomIndex] = "+" + listOfNumbersWithString[randomIndex]
        
    

lastNumber = round(sum(listOfNumbers) - target, 3) * -1

listOfNumbers.append(lastNumber)
listOfNumbersWithString.append(lastNumber)


def ifLastAboveOneThousand():
    if listOfNumbersWithString[-1] > 1000:
        randomVal = round(random.uniform(1, 999),2)
        listOfNumbersWithString.append(randomVal)
        listOfNumbersWithString[-2] = round(listOfNumbersWithString[-2] - randomVal,4)

        listOfNumbersWithString.append(listOfNumbersWithString[-2])
        listOfNumbersWithString.pop(-3)
        ifLastAboveOneThousand()

def ifLastBelowOneThousand():
    if listOfNumbersWithString[-1] < -1000:
        randomVal = round(random.uniform(-1, -999),2)
        listOfNumbersWithString.append(randomVal)
        listOfNumbersWithString[-2] = round(listOfNumbersWithString[-2] - randomVal,4)

        listOfNumbersWithString.append(listOfNumbersWithString[-2])
        listOfNumbersWithString.pop(-3)
        ifLastBelowOneThousand()

ifLastAboveOneThousand()
ifLastBelowOneThousand()

# Put a plus on every normal floats
for i,v in enumerate(listOfNumbersWithString):
    if type(v) == float:
        if v > 0 :
            listOfNumbersWithString[i] = "+" + str(listOfNumbersWithString[i])




outputString1 = ""

for v in listOfNumbers:
    if v > 0:
        outputString1 = outputString1 + "+" + str(v)
    else:
        outputString1 = outputString1 + str(v)




outputStringCompl = ""

for v in listOfNumbersWithString:
    outputStringCompl = outputStringCompl + str(v)



# Gets rid of first plus
if outputStringCompl[0] == "+":
    outputStringCompl = outputStringCompl[1:]



print(listOfNumbers)
print("\n")
print(outputString1)
print(sympy.sympify(outputString1))
print("\n")
print(listOfNumbersWithString)
print("\n")
print(outputStringCompl)
print(sympy.sympify(outputStringCompl))
print("\n")
print(outputStringCompl + "+" + str(target - sympy.sympify(outputStringCompl)))