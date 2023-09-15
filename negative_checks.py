# Создать отдельный файл для негативных тестов.
# Функцию проверки вынести в отдельную библиотеку.
# Повредить архив (например, отредактировав его в текстовом редакторе).
# Написать негативные тесты работы архиватора с командами распаковки (e)

from checks import checkout_negative
import pytest


folderin = '/home/b/Educational_materials/Auto_test_Python_for_Linux/pythonProject2/example/test'
folderout = '/home/b/Educational_materials/Auto_test_Python_for_Linux/pythonProject2/example/out'
folderext = '/home/b/Educational_materials/Auto_test_Python_for_Linux/pythonProject2/example/folder1'


def test_step1():
    assert checkout_negative(f'cd {folderout}; 7z e arh1.7z -o{folderext}', 'ERROR'), 'test_step1 FAIL'



if __name__ == '__main__':
    pytest.main(['-vv'])