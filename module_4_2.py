def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()     # ничего не выводит, не вызвана внешняя ф-ия test_function()
test_function()          # вызов внешней ф-ии, inner_function() в области видимости
inner_function()         # выдает ошибку, inner_function() находится в локальном пространстве ( внутри)
                         #  ф-ии test_function() ) вызов из глобального пространства имен не возможен