import csv

with open("customers.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    customers = list(reader)

print("【顧客情報一覧】")
for customer in customers:
    print(f"■名前: {customer['name']}、遅延日数: {customer['overdue_days']}日、スコア: {customer['score']}")
