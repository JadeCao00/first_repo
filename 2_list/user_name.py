current_usernames = ['Jason', 'Chole', 'Hailey', 'Peter', 'Fiona']
new_usernames = ['Nicky', 'Ray', 'Lily', 'peter', 'jason']

# 集合推导式 Set Comprehension
current_lower = {name.lower() for name in current_usernames}

for username in new_usernames:
    if username.lower() in current_lower:
        print(f"Sorry, '{username}' is used. Please type another name.")
    else:
        print(f"'{username}' is available")