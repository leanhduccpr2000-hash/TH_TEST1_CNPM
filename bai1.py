def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return a * b // ucln(a, b)

# Nhập hai số
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))

print(f"Bội chung nhỏ nhất của {x} và {y} là: {bcnn(x, y)}")
