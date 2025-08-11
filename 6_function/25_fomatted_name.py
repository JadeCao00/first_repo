def get_formatted_name(first_name,  last_name, middle_name = ''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
        return full_name.title()
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
        return full_name.title()

musician = get_formatted_name("jimi", "phllip")
print(musician)

musician = get_formatted_name("john", "edward", "lee")
print(musician)