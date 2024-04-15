def nom1():
    import json
    with open("json1.json", "r", encoding="utf8") as file:
        a = json.load(file)
    products = a['products']

    # Перебираем каждый продукт
    for product in products:
        name = product['name']
        price = product['price']
        weight = product['weight']
        available = product['available']

        # Выводим информацию о продукте
        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Вес: {weight}")
        if available:
            print("В наличии")
        else:
            print("Нет в наличии!")

def nom2():
    import json
    with open("json2.json", "r", encoding="utf8") as file:
        a = json.load(file)
    products = a['products']

    # Перебираем каждый продукт
    for product in products:
        name = product['name']
        price = product['price']
        weight = product['weight']
        available = product['available']

        # Выводим информацию о продукте
        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Вес: {weight}")
        if available:
            print("+В наличии")
        else:
            print("-Нет в наличии")

    name_new = input("Введите название продукта: ")
    price_new = int(input("Введите цену продукта: "))
    available_new = input("Продукт доступен? (да/нет): ").lower() == "да"
    weight_new = int(input("Введите вес продукта: "))
    print("Итоговый файл:")

    # Создаем новый объект продукта
    product_new = {
        "name": name_new,
        "price": price_new,
        "available": available_new,
        "weight": weight_new
    }

    # Добавляем новый продукт в список
    a["products"].append(product_new)

    # Записываем обновленные данные в файл
    with open('json2.json', 'w') as file:
        json.dump(a, file, indent=4)

    with open("json2.json", "r", encoding="utf8") as j_file:
        new_data = json.load(j_file)

        for x in new_data['products']:
            print(f'Название: {x['name']}')
            print(f"Цена: {x['price']}")
            print(f"Вес: {x['weight']}")
            if available:
                print("+В наличии")
            else:
                print("-Нет в наличии")
def nom3():
    # Создаем пустой словарь для англ-рус слов
    eng_rus_dict = {}

    # Открываем файл с англо-русским словарем для чтения
    with open("en_ru.txt", 'r', encoding='utf-8') as file:
        # Читаем все строки из файла
        a = file.readlines()

        # Обрабатываем каждую строку
        for stroch in a:
            # Разделяем строку по символу "-" и получаем список из двух элементов
            words = stroch.strip().split(' - ')
            english_word = words[0]

            # Если в списке есть два элемента
            if len(words) == 2:
                # Разделяем второй элемент по запятой и получаем список переводов
                russian_translations = words[1].split(', ')
                eng_rus_dict[english_word] = russian_translations

    #Сортируем словарь
    sorted_eng_rus_dict = dict(sorted(eng_rus_dict.items()))

    #Вывод отсортированных слов в словаре
    with open("en_ru.txt", "w", encoding="utf8") as file:
        for english_word, russian_translations in sorted_eng_rus_dict.items():
            file.write(f"{english_word} - {", ".join(russian_translations)}\n")

    # Создаем пустой словарь для рус-англ слов
    rus_eng_dict = {}
    for stroch in a:
        eng_word, rus_translation = stroch.strip().split(" - ")
        rus_words = rus_translation.split(", ")
        # Добавляем каждый перевод в словарь
        for rus_word in rus_words:
            # Если перевод уже есть в словаре, добавляем переводимое слово в значение
            if rus_word in rus_eng_dict:
                rus_eng_dict[rus_word].append(eng_word)
                # Иначе создаем новую запись в словаре
            else:
                rus_eng_dict[rus_word] = [eng_word]

    # Открываем файл для записи русско-английского словаря
    with open('ru_en.txt', 'w', encoding='utf-8') as file:
        # Обрабатываем каждую запись в словаре
        for rus_word in sorted(rus_eng_dict.keys()):
            eng_words = ", ".join(rus_eng_dict[rus_word])
            # Записываем русское слово и переводы в файл
            file.write(f'{rus_word} – {eng_words}\n')