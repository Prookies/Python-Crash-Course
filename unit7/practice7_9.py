sandwich_orders = ['ham', 'pastrami', 'bacon', 'pastrami', 'cheese', 'pastrami']
print(sandwich_orders)
print("\nAll pastrami sandwich were sold.")
active = True
while active:
    if 'pastrami' not in sandwich_orders:
        active = False
    else:
        sandwich_orders.remove('pastrami')

print(sandwich_orders)
