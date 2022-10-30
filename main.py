# Define items in the vending machine stating the id, name and price of each item
items = [{
    'item_id': 1,
    'item_name': 'Slim Bar',
    'item_price': '5p'
},{
    'item_id': 2,
    'item_name': 'Far Bar',
    'item_price': '10p'
},{
    'item_id': 3,
    'item_name': 'Mar Bar',
    'item_price': '20p'
},{
    'item_id': 4,
    'item_name': 'Twin Bar',
    'item_price': '50p'
}]
#Define accepted coins
coins = ['5p','10p','20p','50p']
coin = 0
balance = 0
selected_items = []
current_transaction = 0
# Define function for initializing the machine
def initMachine():
    print('welcome to machine...\n')
    return initPay()

def initPay():
    inserted_coin = input('Please insert a coin..\n')
    global coin
    coin = int(inserted_coin.replace('p',''))
    global balance
    balance = coin
    return validatePay(inserted_coin)

def validatePay(inserted_coin):
    for i in coins:
        if (i == inserted_coin):
            return itemList()
    print('Invalid coin...\nEjecting...')
    return initPay()

def itemList():
    print('Items in the machine:')
    for i in items:
        print(f"Item id: {i['item_id']}, Name: {i['item_name']}, Price: {i['item_price']}")
    return chooseItem()

def chooseItem():
    choice = input('Please input id of item you want to buy:')
    for i in items:
        if(i['item_id'] == int(choice)):
            return validatePrice(i)
    print('Item not found...\nListing available items again...')
    return itemList()

def validatePrice(item):
    price = int(item['item_price'].replace('p',''))
    global balance
    if(balance < price):
        print("Coin inserted is lower than the price of this item.")
        cta = input("Would you like to \n 1. Insert a different coin \n 2. Choose a different item \n OR \n 3. Finish transaction\n")
        if(cta == '1'):
            print("Ejecting coin...")
            return initPay()
        elif(cta == '2'):
            return chooseItem()
        else:
            if not selected_items:
                return print("Ejecting coin...")
            else:
                return endTransaction()
    selected_items.append(item)
    balance -= price
    global current_transaction
    current_transaction += price
    return last()

def last():
    print("Item has been selected...")
    progress = input("Would you like to purchase another item. (yes/no)")
    if(progress == "yes"):
        return itemList()
    else:
        return endTransaction()

def endTransaction():
    print("You have purchased")
    for i in selected_items:
        print(f"Name: {i['item_name']}, Price: {i['item_price']}")
    print(f'Your total: {current_transaction}p\n Your change: {balance}p')
    if(balance > 0):
        print("Please collect your change...")
    print("Thank you for using this machine")
    exit()

initMachine()
        