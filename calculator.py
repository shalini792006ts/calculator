def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "❌ Cannot divide by zero!"
    return x / y

print("📟 Simple CLI Calculator")
print("Choose operation: +  -  *  /")

op = input("Operation: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", sub(a, b))
elif op == "*":
    print("Result:", mul(a, b))
elif op == "/":
    print("Result:", div(a, b))
else:
    print("❌ Invalid operation")
