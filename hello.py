# Create our own function
# Tạo hàm của riêng chúng ta
def henrry(to="world"):
    print("helloo", to)

# Output using our own function
# Xuất dữ liệu sử dụng hàm của chúng ta
name = input("What's your name? ")
henrry(name)

# Output without passing the expected arguments
# Xuất dữ liệu mà không truyền các đối số mong đợi
henrry()