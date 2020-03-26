from vending_machine.data import Drink
balance = 0
drinks = [
    Drink("可樂", 20),
    Drink("雪碧", 20),
    Drink("茶裏王", 25),
    Drink("原翠", 25),
    Drink("純粹喝", 30),
    Drink("水", 20),
]

def deposit():     # (要傳入的參數)，如果不要回傳也可以不用()
    """
    儲值功能
    :return: nothing
    """
    global balance
    value = eval(input("儲值金額:"))
    while value < 1:
        print('====儲值金額需大於零====')
        value = eval(input("儲值金額:"))
    balance += value
    print(f"儲值後餘額為 {balance}元")

def buy():
    global balance
    # 印出品項
    print("\n請選擇商品")
    for i in range(0, len(drinks)):
        print(f'({i + 1})\t{drinks[i]["name"]} \t {drinks[i]["price"]}元')
        # i+1就是把索引的0加一，因為實際的編號沒有0
    choose = eval(input('請選擇:'))

    while    choose < 1 or choose > 6:
        print("====請輸入1-6之間====")
    choose = eval(input("請選擇:"))

    buy_drink = drinks[choose - 1]  # -1就是把剛剛加的一減回來
    while balance < buy_drink["price"]:
        print("====餘額不足，需要儲值嗎?====")
        want_deposit = input('y/n?')   # y/n是字串不是數字，不用eval()
        if want_deposit == "y":
            deposit()
        elif want_deposit == "n":
            break
        else:
            print("====請重新輸入====")
    if balance >= buy_drink["price"]:
        print(f'已購買{buy_drink["name"]} {buy_drink["price"]} 元')
        balance -= buy_drink["price"]
        print(f'購買後餘額為 {balance} 元')
