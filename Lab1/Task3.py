def show_even_list():
    list_of_all_numbers = [i for i in range(0, 100)]
    even_list = [i for i in list_of_all_numbers if i % 2 == 0]
    print(even_list)

