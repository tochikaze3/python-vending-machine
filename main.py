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

# Define default values for current coin amount inserted,coin balance, selected items and total amount purchased
coin = 0
balance = 0
selected_items = []
current_transaction = 0

# Define function for initializing the machine
def initMachine():
    print('welcome to machine...\n')
    return initPay()

# The initPay function asks the user to insert a coin and initiates the validatePay function that validates the coin inserted
def initPay():
    inserted_coin = input('Please insert a coin..\n')
    return validatePay(inserted_coin)

# The validatePay function checks if the coin inserted is an accepted coin by looping through the list of accepted coins to check 
# if the coin matches any. If it matches any it removes the p from the coin and converts it to an integer(eg. 20p becomes 20).
# It then assigns the converted value to the original coin amount inserted and coin balance and initiates the itemsList function that lists all the available items in the list
# If the coin does not match any of the accepted coins, it is ejected and then the program falls back to the initPay function
def validatePay(inserted_coin):
    for i in coins:
        if (i == inserted_coin):
            global coin
            coin = int(inserted_coin.replace('p',''))
            global balance
            balance = coin
            return itemList()
    print('Invalid coin...\nEjecting...')
    return initPay()

# The itemList function lists all items available items and initiates the chooseItem function
def itemList():
    print('Items in the machine:')
    for i in items:
        print(f"Item id: {i['item_id']}, Name: {i['item_name']}, Price: {i['item_price']}")
    return chooseItem()

# The chooseItem function asks the user to input the id of the item they want. When an input is made, the program loops through the item list
# to find the item with the inputed id(converted to an integer). If the item is found, it parses the item dictionary as a parameter to the validatePrice function.
# if the item is not found the program prompts the user that the item was not found and falls back to the itemList function to list the available items.
def chooseItem():
    choice = input('Please input id of item you want to buy:')
    for i in items:
        if(i['item_id'] == int(choice)):
            return validatePrice(i)
    print('Item not found...\nListing available items again...')
    return itemList()

# The validate function removes the p from the item_price and converts it to an integer(eg. 20p becomes 20) and checks if the balance is lower than the price of the item.
# If it is, it prompts the user that the balance is lower than the price of the item. It then gives the user three options 
    # 1. to insert a different coin 2. To choose a different item or 3. Finish the transaction
    # If option 1 is selected it ejects the coin and falls back to the initPay function
    # If option 2 is selected it initiates the chooseItem function again
    # If option 3 is selected it checks the selected_items list for already selected_items.If it contains any items, it initiates the endTransaction function. If it doesn't,
    # it ejects the coin
# If the balance is not lower than the price of the item it adds the item to the list of selected_items, deducts the price from the balance, adds the price to the current_transaction and theen
# It then initiates the last function
def validatePrice(item):
    price = int(item['item_price'].replace('p',''))
    global balance
    if(balance < price):
        print("Coin balance is lower than the price of this item.")
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

# The last function asks the user if they would like to purchase another item. If yes, it initiates the itemList function again. 
# If not it initiates the endTransaction function
def last():
    print("Item has been selected...")
    progress = input("Would you like to purchase another item. (yes/no)")
    if(progress == "yes"):
        return itemList()
    else:
        return endTransaction()

# The endTransaction function prints out a reciept for the transaction and ends the transaction.
def endTransaction():
    print("You have purchased")
    for i in selected_items:
        print(f"Name: {i['item_name']}, Price: {i['item_price']}")
    print(f'Your total: {current_transaction}p\n Your change: {balance}p')
    if(balance > 0):
        print("Please collect your change...")
    print("Thank you for using this machine")
    exit()

# Initiate the machine
initMachine()
        