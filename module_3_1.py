calls = 0
def count_calls():#подсчитывает вызовы остальных функций
    global calls
    calls += 1
    
def string_info(string):#принимает аргумент-строку и возвращает кортеж из длины этой строки+строку в верхнем регистре+
                        # строку в нижнем регистре
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):#принимает два аргумента - строку и список и возвращает True,
                                        # если строка находится в этом списке или False - если отсутствует.
                                        # Регистром при проверке можно принебречь
    count_calls()
    for word in list_to_search:
        if string.lower() == word.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)