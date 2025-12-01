a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("3 cạnh tạo thành tam giác")
else:
    print("Không phải tam giác")