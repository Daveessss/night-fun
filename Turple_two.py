products = [
        ("laptop",1200),
        ("Mouse",25),
        ("Keyboard",45),
        ("Monitor",300),
        ("Usb Cable",10),
]

def products_greater_than(numbers):
    if numbers[1] > 100:
        return numbers
cost = filter(products_greater_than, products)
for product, price in cost:
    print(f'{product}   {price}')



sum = 0
for product, price in products:
    sum = sum + price
print(sum)



for product, price in products:
    print(product)
    print(price)
