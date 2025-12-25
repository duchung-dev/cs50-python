score = int(input("Score: "))

if score >= 85:
    print ("Grade: HD")
elif score >= 75:
    print ("Grade: D")
elif score >= 65:
    print ("Grade: C")
elif score >= 50:
    print ("Grade: P")
elif score >= 30:
    print ("Grade: F")
else:
    print ("Grade: FF")