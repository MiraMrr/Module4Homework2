def test_function(a):
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function(1)

# inner_function()
# При попытке вызвать функцию inner_function вне функции test_function получаем следующую ошибку:
# Traceback (most recent call last):
#   File "D:\Карина\IT\Python\PyCharmProjects\UrbanModule4\Module4Homework2.py", line 7, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
