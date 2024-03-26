import pytest

@pytest.fixture(scope='module')   #名为login的fixture，完成登陆和注册操作
def login():
    print('登陆操作~~~')
    yield
    print('注销操作~~~')

@pytest.mark.usefixtures("login")
class TestClass1:
    def test_case1(self):
        print("TestClass1:test_case1")

    def test_case2(self):
        print("TestClass1:test_case2")

class TestClass2:
    def test_case1(self):
        print("TestClass2:test_case1")

    def test_case2(self):
        print("TestClass2:test_case2")
