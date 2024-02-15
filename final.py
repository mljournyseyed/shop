products={100:{'brand':'bmw','model':'m3','hp':395,'coler':'pershain bleu','price':1000,'stock':65},
          101:{'brand':'bmw','model':'m5cs','hp':600,'coler':'red','price':2500,'stock':4},
          102:{'brand':'bmw','model':'m8','hp':850,'coler':'blck','price':4000,'stock':6},
          103:{'brand':'bmw','model':'xm','hp':1000,'coler':'pinck','price':1000,'stock':12},
          104:{'brand':'benz','model':'g wagon','hp':900,'coler':'black','price':7000,'stock':32},
          105:{'brand':'benz','model':'c280','hp':280,'coler':'orange','price':190,'stock':10},
          106:{'brand':'benz','model':'s500','hp':900,'coler':'white','price':91000,'stock':11},
          107:{'brand':'ford','model':'f150','hp':700,'coler':' bleu','price':4000,'stock':24},
          108:{'brand':'ford','model':'f350','hp':650,'coler':'plum','price':1000,'stock':31},
          109:{'brand':'ford','model':'f450','hp':770,'coler':'cyan','price':1000,'stock':32},
          110:{'brand':'doghe','model':'ram','hp':1100,'coler':'oliver','price':1000,'stock':24},
          111:{'brand':'doghe','model':'diman','hp':1200,'coler':'golden','price':1000,'stock':13},
          112:{'brand':'doghe','model':'charcher','hp':1170,'coler':'gray','price':1000,'stock':19},
          113:{'brand':'porsh','model':'911','hp':700,'coler':'brown','price':1000,'stock':32},
          114:{'brand':'porsh','model':'918','hp':1100,'coler':'green','price':1000,'stock':7},
          115:{'brand':'doghe','model':'chalnger','hp':981,'coler':'yellow','price':1000,'stock':65},
          116:{'brand':'audi','model':'r8','hp':781,'coler':'white','price':1000,'stock':46},
          117:{'brand':'audi','model':'tt','hp':300,'coler':'black','price':1000,'stock':23},
          118:{'brand':'audi','model':'rs7','hp':800,'coler':'red','price':1000,'stock':18},
          119:{'brand':'honda','model':'civick','hp':395,'coler':'black','price':1000,'stock':25}}
shopping_cart = {}

def show_products():
    print('-' * 53)
    print(f'|{"code":^8}|{"brand":^10}|{"model":^10}|{"price":^10}|')
    print('-' * 53)
    for code in products:
        print(f'|{code:^8}|{products[code]["brand"]:^10}|{products[code]["model"]:^10}|{products[code]["price"]:^10}|')
    print('-' * 53)

def add_to_cart(code, number):
    if code in shopping_cart:
        shopping_cart[code][0] += int(number)
        print(f'The number of products increased to {shopping_cart[code][0]}')
    else:
        if code in products:
            shopping_cart[code] = [int(number), products[code]['price']]
            print(f'{code} added to the shopping cart')
        else:
            print(f'Error: Product with code {code} not found.')

def remove_from_cart(code, number):
    if code not in shopping_cart:
        print('This product is not in your shopping cart')
    else:
        if shopping_cart[code][0] <= int(number):
            answer = input(f'The product {code} is in your shopping cart. Do you want to remove it completely? (yes/no): ')
            if answer.lower() == 'yes':
                shopping_cart.pop(code)
                print(f'The product {code} has been removed from your shopping cart')
        else:
            shopping_cart[code][0] -= int(number)
            print(f'The number of products decreased to {shopping_cart[code][0]}')

def show_shopping_cart():
    if not shopping_cart:
        print('Your shopping cart is empty.')
    else:
        print('Your shopping cart:')
        print('-' * 53)
        print(f'|{"code":^8}|{"brand":^10}|{"model":^10}|{"price":^10}|')
        print('-' * 53)
        for code in shopping_cart:
            print(f'|{code:^8}|{products[code]["brand"]:^10}|{products[code]["model"]:^10}|{products[code]["price"]:^10}|')
        print('-' * 53)

while True:
    text = input('Dear user, how can I help you?\nEnter 1 to show products\nEnter 2 to add or remove items in the shopping cart\nEnter 3 to display the shopping cart\nEnter "q" to exit\n')
    
    if text == 'q':
        break
    elif text == '1':
        show_products()
    elif text == '2':
        print('# help\nEnter the car code')
        while True:
            text = input('What do you want to do?\nFor buying the car, enter "add" or "1"\nFor removing the car from the shopping cart, enter "remove" or "2"\nAfter completing the purchase, enter "done"\n')
            
            if text.lower() in ['add', '1']:
                car_info = input('Please enter the car code and the number you need : ')
                if car_info.isdigit():
                    code, number = car_info.split()
                    add_to_cart(code, number)
                else:
                    print('Please input correctly.')
            
            elif text.lower() in ['remove', '2']:
                car_info = input('Please enter the car code and the number you want to remove: ')
                if car_info.isdigit():
                    code, number = car_info.split()
                    remove_from_cart(code, number)
                else:
                    print('Please input correctly.')
            
            elif text.lower() == 'done':
                break
            else:
                print('Please input correctly.')
    
    elif text == '3':
        show_shopping_cart()

print('We hope to give you a satisfactory experience.')
