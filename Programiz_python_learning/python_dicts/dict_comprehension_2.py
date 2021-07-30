old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76

new_price = {k: v * dollar_to_pound for (k,v) in old_price.items()}
print(new_price)



original_dict = { 'bharath': 50, 'Lee': 35, 'Ion': 24, 'Senthil': 17}

even_dict = { k: v for (k,v) in original_dict.items() if v%2 == 0}
print(even_dict)

new_dict = { k: v for (k,v) in original_dict.items() if v%2 !=0 if v < 30}
print(new_dict)


new_dict_1 = { k: ('old' if v > 40 else 'young') for (k,v) in original_dict.items()}
print(new_dict_1)

