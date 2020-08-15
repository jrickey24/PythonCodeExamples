# SAMPLE CODE FOR CREATING DICTIONARY VARIABLE
# PYTHON AUTOMATICALLY UNDERSTANDS THIS AS DATA TYPE DICT

caffeine_content_mg = {
    'Mr. Goodbar chocolate': 122,
    'Red Bull': 33,
    'Monster Hitman Sniper energy drink': 270,
    'Lipton Brisk iced tea - lemon flavor': 2,
    'dark chocolate coated coffee beans': 869,
    'Regular drip or percolated coffee': 60,
    'Buzz Bites Chocolate Chews': 1639,
    '53 Proof Coffee Liquer': 9,
}

print(caffeine_content_mg)

# CHANGES AN EXISTING KEY'S VALUE, OR CREATES THE KEY/VALUE PAIR IF IT DOESN'T ALREADY EXIST
caffeine_content_mg['Mr. Goodbar chocolate'] = 120
print(caffeine_content_mg['Mr. Goodbar chocolate'])

# REMOVES AN ENTRY IF IT EXISTS
del caffeine_content_mg['Monster Hitman Sniper energy drink']
print(caffeine_content_mg)
