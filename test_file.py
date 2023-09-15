# Добавить в проект тесты, проверяющие работу команд
# d (удаление из архива) и u (обновление архива). Вынести
# в отдельные переменные пути к папкам с файлами, с архивом
# и с распакованными файлами. Выполнить тесты с ключом -v.

from checks import checkout
import pytest

folderin = '/home/b/Educational_materials/Auto_test_Python_for_Linux/pythonProject2/example/test'
folderout = '/home/b/Educational_materials/Auto_test_Python_for_Linux/pythonProject2/example/out'
folderext = '/home/b/Educational_materials/Auto_test_Python_for_Linux/pythonProject2/example/folder1'


def test_step1():
    assert checkout(f'cd {folderin}; 7z a {folderout}/arh1', 'Everything is Ok'), 'test_step1 FAIL'


# def test_step2():
#     assert checkout(f'cd {folderout}; 7z d arh1.7z', 'Everything is Ok'), 'test_step2 FAIL'
#
#
# def test_step3():
#     assert checkout(f'cd {folderext}; 7z u {folderout}/arh1', 'Everything is Ok'), 'test_step3 FAIL'


def test_step4():
    assert checkout(f'cd {folderout}; 7z l arh1.7z', 'Everything is Ok'), 'test_step4 FAIL'


def test_step5():
    assert checkout(f'cd {folderout}; 7z x arh1.7z', 'Everything is Ok'), 'test_step5 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
