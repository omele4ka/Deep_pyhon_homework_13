# Задача из ДЗ №2
# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
# Добавлен класс исключения

class InvalidInputError(Exception):
    def __init__(self, message="Некорректный ввод! Введите целое число"):
        self.message = message
        super().__init__(self.message)


class HexConverter:
    HEX_NUM = 16

    def int_to_hex(self, num: int) -> str:
        if num == 0:
            return '0'

        hex_map = {
            0: '0', 1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9', 10: 'a', 11: 'b',
            12: 'c', 13: 'd', 14: 'e', 15: 'f'
        }

        hex_str = ""
        negative = False

        if num < 0:
            negative = True
            num = abs(num)

        while num > 0:
            hex_digit = num % self.HEX_NUM
            hex_str = hex_map[hex_digit] + hex_str
            num = num // self.HEX_NUM

        if negative:
            hex_str = '-' + hex_str

        return hex_str

    def convert_and_print(self, user_input):
        try:
            user_number = int(user_input)
            hex_user_number = self.int_to_hex(user_number)
            print('Шестнадцатеричное представление Вашего числа:', hex_user_number)
            print('Проверка:', hex(user_number))
        except ValueError:
            raise InvalidInputError()

if __name__ == "__main__":
    try:
        user_input = input('Введите целое число: ')
        converter = HexConverter()
        converter.convert_and_print(user_input)
    except InvalidInputError as e:
        print(e)
