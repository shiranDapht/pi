#!/bin/python

# Too ugly for one liner :(
# product is a dict such as the key is the name, and the value is [price, amount, sold]
def load_file(file_name : str):
    products = {}
    def add_product(params : str):
        param_list = params.split(' ')[2:] # ['<name>', '<price>', '<amount>']
        if(param_list[0] not in products):
            products[param_list[0]] = [int(param_list[1]), int(param_list[2]), 0]
    def change_amount(params : str): 
        param_list = params.split(' ')[2:] # ['<name>', '<new amount>']
        if(param_list[0] in products):
            products[param_list[0]][1] += int(param_list[1])
    def ship_order(params : str):
        param_list = [tuple(pair.split(', ')) for pair in params[11:].split(' -- ')] # [(<product name>, <product amount>)...]
        for name, amount_str in param_list:
            if(int(amount_str)>0 and name in products and int(amount_str) <= int(products[name][1])):
                products[name][1] -= int(amount_str)
                products[name][2] += int(amount_str)
    functions_dict = {'add':add_product, 'change':change_amount, 'ship':ship_order}
    with open(file_name) as f:
        for line in f:
            better_line = line.strip()
            if better_line:
                functions_dict[better_line.split(" ")[0]](better_line.strip())
    return products

'''
def find_best_selling_product(file_name):
    products = load_file(file_name)
    if(not products):
        return '', 0
    max_value = products[max(products,key=lambda n: products[n][2])][2]
    max_name = sorted([name for name in products if products[name][2] == max_value])[0]
    return max_name, max_value
'''
def find_best_selling_product(file_name):
    return ('', 0) if not load_file(file_name) else (sorted([name for name in load_file(file_name) if load_file(file_name)[name][2] == load_file(file_name)[max(load_file(file_name),key=lambda n: load_file(file_name)[n][2])][2]])[0], load_file(file_name)[max(load_file(file_name),key=lambda n: load_file(file_name)[n][2])][2])

def find_k_most_expensive_products(file_name, k):
    return [name for v, name in sorted([(v[0], name) for name, v in load_file(file_name).items()], key=lambda t: (t[0],''.join(map(lambda i: chr(0x110000-ord(i)),t[1]))), reverse=True)[:k]]
    # sort by price then anti-name list of (price, name) for all products then slice first k elements into list of names.