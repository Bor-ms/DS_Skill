"""Игра угадай число
Алгоритм с ограниченным диапазоном - около 20 попыток
"""

import numpy as np

def smart_random_predict(number: int = 1) -> int:
    """Угадываем число с сужающимся диапазоном
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    
    Returns:
        int: Число попыток (около 15-20)
    """
    count = 0
    low = 1
    high = 100
    
    while True:
        count += 1
        # С каждым шагом сужаем диапазон
        if count < 10:
            # Первые 10 попыток - в полном диапазоне
            predict_number = np.random.randint(low, high + 1)
        else:
            # После 10 попыток - в суженном диапазоне
            predict_number = np.random.randint(low, high + 1)
        
        if predict_number == number:
            break
        elif predict_number < number:
            low = max(low, predict_number + 1)
        else:
            high = min(high, predict_number - 1)
            
        # Ограничиваем максимальное количество попыток
        if count >= 30:  # На всякий случай страховка
            break
    
    return count

def score_game(predict_func) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    
    Args:
        predict_func (function): функция угадывания
    
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(predict_func(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    print(f"Минимальное количество попыток: {min(count_ls)}")
    print(f"Максимальное количество попыток: {max(count_ls)}")
    return score

if __name__ == "__main__":
    score_game(smart_random_predict)