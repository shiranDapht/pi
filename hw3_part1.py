def create_products_selling(file_name):
    with open(file_name, 'r') as products_file:
        products = {}
        selling = {}
        products_lines = products_file.read().splitlines()
        for line in products_lines:
            if(line.startswith('add product')):
                line.split()
                if(line[1] in products):
                    continue
                if(line[2] < 0):
                    continue
                price_amount = [line[2], line[3]]
                products.update(line[1], price_amount)
                selling.update(line[1], 0)

            if(line.startswith('change amount')):
                line.split()
                change_amount = products.get(line[1])
                change_amount[1] += line[2]
                products.update(line[1], change_amount)

            if(line.startswith('ship order')):
                products_list = line.split('--')
                for name_amount in products_list:
                    name_amount.split()
                    if(name_amount[0] not in products):
                        continue
                    price_amount = products.get(name_amount[0])
                    if(name_amount[1] > price_amount[1]):
                        continue
                    price_amount[1] -= name_amount[1]
                    products.update(name_amount[0], price_amount)
                    name_amount[1] += (price_amount[0] * price_amount[1])
                    selling.update(name_amount[0], name_amount[1])
    return products, selling
        

def find_best_selling_product(file_name):
    selling  = create_products_selling(file_name)[1]
    return max(selling.items()[1])

def find_k_most_expensive_products(file_name, k):
    products = create_products_selling(file_name)[0]
    new_list = []
    while(k < 0 or not products):
        max_price = max(products.items[1][0])
        new_list.append(max_price)
        products.popitem(max_price)
        k-1

    return new_list
