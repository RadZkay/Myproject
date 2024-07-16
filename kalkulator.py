def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Kesalahan"
    else:
        return x / y



print("Pilih operasi:")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

choice = (input("Masukan pilihan operasi yang anda inginkan (1/2/3/4): "))
while choice not in ['1', '2', '3', '4']:
    choice = (input("Mohon masukkan angkan diantara 1 hingga 4: "))


num1 = float(input("Masukan angka pertama: "))
num2 = float(input("Masukan angka kedua: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))