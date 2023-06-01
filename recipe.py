def take_recipe(name):
    # открытие файла
    with open("recipes", encoding="utf8") as f:
    # цикл поиска рецепта
        for names in f.readlines():
    # разделяем строку по знаку '-', проверяем совпадение до разделителя
    # и выводим все остальное после разделителя
            if names.split("&")[0] == name:
                recipe = names.split('&')[1]
    return recipe