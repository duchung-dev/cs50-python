def main():
    # Output using our own function
    # In ra sử dụng hàm của riêng chúng ta
    name = input("Enter your name: ")
    henrry(name)

    #output without passing the expected arguments
    # In ra mà không truyền các đối số mong đợi
    henrry()


# Create our own function
# Tạo hàm của riêng chúng ta
def henrry(to="world"):
    print("hello", to)

main()
