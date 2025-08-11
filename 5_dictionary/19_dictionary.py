favorite_language = {
    'jen':'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil' : 'python',
    }

new_participates = ['edward', 'maria', 'dexter', 'phil']
for participate in new_participates:
    if participate in favorite_language.keys():
        print(f'Thank you for your attendance, {participate}.')
    else:
        print((f'Hey {participate}, we are here to invite you!'))


# for name in sorted(favorite_language.keys()):
#     print(f'{name.title()}, thank you for taking this poll.')

# print("The following languages have been mentioned:")
# for language in favorite_language.values():
#     print(language.title())
#
# # set()中的每个元素都是独一无二的
# print("The following languages have been mentioned:")
# for language in set(favorite_language.values()):
#     print(language.title())
