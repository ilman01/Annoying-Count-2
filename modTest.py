import random

targetVal = 23 # y

randomNumerator = round(random.uniform(1,999),0) # 9
print(randomNumerator)

resNumerator = ((randomNumerator * targetVal) + randomNumerator)
resDenominator = ((targetVal * 2) + 1)
print(f"{resNumerator}/{resDenominator}")

