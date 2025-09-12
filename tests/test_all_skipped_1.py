import pytest

@pytest.mark.skip
def test_skipped1():
    with allure.step("Неправильная математика"):
        assert 2 + 2 == 5

@pytest.mark.skip
def test_skipped2():
    with allure.step("Строки не равны"):
        assert "hello" == "bye"

@pytest.mark.skip
def test_skipped3():
    with allure.step("Булево сравнение"):
        assert False

