import random

#ниже функция реализующая алгоритм быстрого возведения в степень
def quick_exponentiation(base, stepenCheck, mod):
    tmpResult = 0
    if stepenCheck == 0:
        return 1
    tmpResult = quick_exponentiation(base, int(stepenCheck / 2), mod)
    if stepenCheck % 2 == 0:
        return tmpResult * tmpResult % mod
    else:
        return base * tmpResult * tmpResult % mod


def gcd_two(number_one, number_two):
    print('шаг функции Алгоритма Евклида')
    if number_one == 0:
        return number_two
    return gcd_two(number_two % number_one, number_one)


def gcd_Evclid_alg_extend(number_one, number_two):
    print('extended Evklid')
    if number_one == 0:
        return number_two, 0, 1
    gcd, x, y = gcd_Evclid_alg_extend(number_two % number_one, number_one)
    x = y - (number_two // number_one) * x
    y = x
    return gcd, x, y


def extended_number_mod(number_one, number_two):
    print('extended number mod func')
    extended_number = 1
    while extended_number < number_two:
        if ((number_one * extended_number) % number_two) == 1:
            return extended_number
        else:
            extended_number += 1
    return "обратного элемента нет"


tableOfSimpleNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
                        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
                        149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
                        227, 229, 233, 239, 241, 251, 257, 263]


def gen_Key_After_Check(n):
    while True:
        random_key = random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)
        for item in tableOfSimpleNumbers:
            if item ** 2 <= random_key and random_key % item == 0:
                break
        else:
            return random_key


def miller_rabin_Algoritms(key):
    max_div_by_two = 0
    ec = key - 1
    while ec % 2 == 0:
        ec >>= 1
        max_div_by_two += 1
    assert (2 ** max_div_by_two * ec == key - 1)

    checkCounerForRabinAlgoritms = 37
    for i in range(checkCounerForRabinAlgoritms):
        round_tester = random.randrange(2, key)
        if trial_composite(round_tester, ec, key, max_div_by_two):
            return False
    return True

def trial_composite(round_tester, ec, key, max_div_by_two):
    if pow(round_tester, ec, key) == 1:
        return False
    for i in range(max_div_by_two):
        if pow(round_tester, 2 ** i * ec, key) == key - 1:
            return False
    return True


def start_my_main_program():
    while True:
        menuForUserSelectNum = input(
            "\nВыберите режим работы:" +
            "\n1. Возведение целого числа в степень по модулю" +
            "\n2. Вычисление НОД двух целых чисел" +
            "\n3. Вычисление обратного числа к данному числу в кольце вычетов" +
            "\n4. Выработка большого простого числа" +
            "\nНажмите: 5. Выйти из программы\nВаш выбор: ")
        try:
            menuForUserSelectNum = int(menuForUserSelectNum)

            if menuForUserSelectNum == 1:
                print("\nВозведение целого числа в степень по модулю")
                try:
                    the_basis_of_the_degree_Input = int(input("Введите основание: "))
                    degree_input = int(input("Введите степень: "))
                    mod_input = int(input("Введите модуль: "))
                    result = quick_exponentiation(the_basis_of_the_degree_Input, degree_input, mod_input)
                    print(f"Результат возведения в степень: {result}")
                except ValueError:
                    print("Ошибка, значение некорректно")
            elif menuForUserSelectNum == 2:
                print("\nВычисление НОД двух целых чисел")
                try:
                    number_one_by_user_input = int(input("Введите число 1: "))
                    number_two_by_user_input = int(input("Введите число 2: "))
                    result = gcd_two(number_one_by_user_input, number_two_by_user_input)
                    print(f"НОД чисел ({number_one_by_user_input}, {number_two_by_user_input}): {result}")
                except ValueError:
                    print("Ошибка, значение некорректно")
            elif menuForUserSelectNum == 3:
                print("\nВычисление обратного значения в кольце вычетов")
                number_one_by_user_input = int(input("Ваше число 1: "))
                number_two_by_user_input = int(input("Ваше число 2: "))
                result = extended_number_mod(number_one_by_user_input, number_two_by_user_input)
                print(f"Обратное значение в кольце ({number_one_by_user_input}, {number_two_by_user_input}): {result}")
            elif menuForUserSelectNum == 4:
                print("\nГенерация большого простого числа")
                length_key_by_user_input = int(input("Введите длину ключа: "))
                while True:
                    n = length_key_by_user_input
                    key_check = gen_Key_After_Check(n)
                    if not miller_rabin_Algoritms(key_check):
                        continue
                    else:
                        print(f"результат генерации ключа: {key_check}")
                        break
            elif menuForUserSelectNum == 5:
                break
            else:
                print("вы ошиблись, выберете правильный пункт меню")
        except ValueError:
            print("ошибка, введите число")


if __name__ == '__main__':
    start_my_main_program()
