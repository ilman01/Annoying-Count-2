import random

targetVal = 1.635

denominator = targetVal + 1

randomMultiplication = random.randint(5,8)
nominator = round(targetVal + denominator * randomMultiplication,4)

randomConfuseDenominator = round(random.uniform(1, denominator-1),2)
stringRandomConfuseDenominator = str(round(denominator - randomConfuseDenominator,2)) + "+" + str(randomConfuseDenominator)

#print(f"{nominator}%{denominator}")
print(f"({nominator}%({stringRandomConfuseDenominator}))")
#print(nominator % denominator)
