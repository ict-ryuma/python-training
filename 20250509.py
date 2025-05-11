# 四則演算の関数定義
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "エラー：0では割れません"
    return a / b

# 入力を受け取る
print("数字を2つ入力してください：")
num1 = int(input("1つ目の数字："))
num2 = int(input("2つ目の数字："))

# 演算子を選ぶ
print("演算を選んでください (+ - * /)：")
operator = input("演算子：")

# 条件によって関数を呼び出す
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "無効な演算子です"

print(f"計算結果：{result}")
