import random
def get_sum_payment(req):
    return random.randint(50_000, 150_000)

def calculate_pdn(salary):
    """
    (заглушка)
    ПДН = 'сумма среднемесячных платежей по всем кредитам и займам заемщика' ДЕЛИТЬ на 'величина среднемесячного дохода заемщика' * 100%
    Существуют риски в случае, если рассчитанное значение ПДН заемщика превышает 50%
    Источник - https://cbr.ru/finstab/instruments/pti/

    - rutern -
    True - есть риск
    False - риск отсутсвует
    """
    pdn = get_sum_payment() / salary * 100

    if pdn > 50:
        return True, pdn
    return False, pdn