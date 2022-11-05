print("歡迎使用拉麵點餐機 ~ ")
print("(1)鹽味拉麵 $220")
print("(2)醬油拉麵 $240")
print("(3)豚骨拉麵 $280\n")
num = input("請選擇拉麵口味 (輸入: 1 or 2 or 3): ")
big = input("是否加大，豚骨口味+$50，其他口味*$30(輸入: Y or N)").upper()
egg = input("是否加糖心蛋+$30(輸入: Y or N)").upper()
meat = str(input("是否加叉燒+$30(輸入: Y or N)")).upper()

bill = 0

if num == "1":
    bill += 220
elif num == "2":
    bill += 240
else:
    bill+= 280

if big == "Y":
    if num == "3":
        bill += 50
    else:
        bill += 30

if egg == "Y":
    bill += 30

if meat == "Y":
    bill += 60

if big == "Y" and egg =="Y" and meat == "Y":
    bill -= 20
    print(f"\n加好加滿折扣20元，總金額${bill}，感謝您的光臨!!")
else:
    print(f"總金額是${bill}，感謝您的光臨!!")