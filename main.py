meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РЖАКА": "Когда что-то очень смешное",
            "ЗАСКАМИТЬ": "Обмануть"
            }
    
while True:
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in list(meme_dict.keys()):
        print(meme_dict[word])
    elif word == "ВЫХОД":
        break
    else:
        print("Извините,но в нашем словаре нет такого слова.")
        a = input("Хотите добавить его?")
        if a == "ДА":
            b = input("Пожалуйста введите значение слова")
            meme_dict[word] = b
