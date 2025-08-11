sandwich_orders = ['mayo tuna', 'pastrami', 'ham', 'pastrami', 'roast chicken', 'pastrami']
print('Pastrami sandwich is sold out!')
while "pastrami" in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwich = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwich.append(current_sandwich)
