import datetime


def get_age(bday):
    age = (datetime.now() - bday).days / 365
    return age

def check_risk(person, pdn, has_bill):
    """
    аргументы:
    person - модель из анкеты (document_package.BidParticipantInfo)
    pdn - рассчитанный ПДН в другой функции
    has_bill - имеет ли счет в банке
    """
    level = 0
    # возраст
    if get_age(person.date_of_birth) <= 25:
        level += 5
    elif get_age(person.date_of_birth) >= 26 and get_age(person.date_of_birth) <= 55:
        level += 1
    elif get_age(person.date_of_birth) >= 56 and get_age(person.date_of_birth) <= 74:
        level += 3
    else:
        level += 10
    
    # семейное положение
    if person.family_status == 'Холост':
        level += 3
    elif person.family_status == 'Женат/Замужем':
        level += 2
    elif person.family_status == 'В разводе':
        level += 5

    # наличие детей
    if person.has_child:
        level += 3
    else:
        level += 5

    # кредитная история клиента (???)


    # основной источник получения доходов (???)


    # стаж клиента на текущем месте работы
    if person.work_experience_year < 1:
        level += 10
    elif person.work_experience_year >= 1 and person.work_experience_year <= 5:
        level += 3
    else:
        level += 2

    # ПДН клиента
    if pdn < 70:
        level += 1
    elif pdn in range(70, 96):
        level += 10
    else:
        level += 20
    # Уровень доходов клиента (полный)
    income = person.official_work_monthly_income + person.monthly_add_income
    if income > 250_000:
        level += 3
    elif income >= 101_000 and income <= 250_000:
        level += 5
    elif income > 50_000 and income <= 100_000:
        level += 7
    else:
        level += 15
    # У клиента имеются сбережения на счетах в Банке

    if has_bill:
        level += 1
    else:
        level += 5

    # оценка уровня риска
    if level > 70:
        return 'Высокий'
    elif level in range(31, 71):
        return 'Средний'
    return 'Низкий'

