import time
import allure

def test_fail_1():
    with allure.step("Ошибка в математике"):
        time.sleep(1)
        assert 10 < 5

def test_fail_2():
    time.sleep(1)
    with allure.step("Ошибка в строке"):
        assert "PYTEST".islower()
