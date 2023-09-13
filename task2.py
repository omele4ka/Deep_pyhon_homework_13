# Задача из ДЗ № 5
# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа
# и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


class SalaryError(Exception):
    def __init__(self, name, message="Ошибка в расчете зарплаты"):
        self.name = name
        self.message = message
        super().__init__(self.message)


def award_gen(names: list, salaries: list, awards: list) -> dict:
    if len(names) != len(salaries) or len(names) != len(awards):
        raise ValueError("Списки 'names', 'salaries', и 'awards'"
                         " должны иметь одинаковую длину.")

    awards_dict = {}

    for name, salary, award_str in zip(names, salaries, awards):
        try:
            award_percentage = float(award_str[:-1]) / 100
        except ValueError:
            raise SalaryError(name, f"Некорректный формат премии для {name}")

        award_amount = salary * award_percentage
        awards_dict[name] = award_amount

    return awards_dict


my_names = ['Alex', 'Gael', 'Yarik']
my_salaries = [6000, 2000, 4000]
my_awards = ['10.25%', '8.5%', '9.9%']

try:
    result = award_gen(my_names, my_salaries, my_awards)
    print(result)
except ValueError as e:
    print(e)
except SalaryError as e:
    print(f"{e.name}: {e.message}")
