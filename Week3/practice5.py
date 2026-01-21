# Demonstrates inequaalitiese and logical operators
# Minh họa các phép so sánh không bằng nhau và toán tử logic

score = int(input(" What's your score? "))

if score >= 85 and score <= 100:
    print(" Grade: HD")
elif score >= 75 and score < 85:
    print(" Grade: D")
elif score >= 65 and score < 75:
    print(" Grade: C")
elif score >= 50 and score < 65:
    print(" Grade: P")
else:
    print(" Grade: F")