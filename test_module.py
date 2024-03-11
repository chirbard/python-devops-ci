from src.main import add


class TestClass:
    def test_add_int_1(self):
        assert add (3, 5) == 8

    def test_add_int_2(self):
        assert add (3, -6) == -3

    def test_add_float(self):
        assert add (3.5, 5.3) == 8.8

    def test_add_string(self):
        assert add ('Hello ', 'World') == 'Hello World'
