# EX: Demonstrates rounding to nearest int
# VD: Minh họa làm tròn đến số nguyên gần nhất

# Demonstrates defining a function with a return value
# Minh họa định nghĩa hàm với giá trị trả về

def main ():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()