river_country = {
    'nile' :'egypt',
    'yellow river' : 'china',
    'mississippi': 'america',
}

for river_name, country_name in river_country.items():
    print(f'The {river_name.title()} runs through {country_name.title()}')