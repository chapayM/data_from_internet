def min_max_salary_hh(vacancy_salary): #Разбор зарплаты по минимальной, максимальной, валюте и налогам для hh
    min_salary, max_salary = '', ''
    if vacancy_salary[0] == 'з/п не указана':
        return [None, None, None, None]
    elif len(vacancy_salary) == 6: #когда есть только минимальная или максимальная ЗП
        if vacancy_salary[0][0] == 'о':
            for el in vacancy_salary[1]:
                if el.isdigit():
                    min_salary += el
        else:
            for el in vacancy_salary[1]:
                if el.isdigit():
                    max_salary += el
    elif len(vacancy_salary) == 8: #когда есть минимальная и максимальная ЗП
        for el in vacancy_salary[1]:
            if el.isdigit():
                min_salary += el
        for el in vacancy_salary[3]:
            if el.isdigit():
                max_salary += el

    if min_salary == '':
        min_salary = None
    else:
        min_salary = float(min_salary)

    if max_salary == '':
        max_salary = None
    else:
        max_salary = float(max_salary)

    currency = vacancy_salary[-3]
    tax = vacancy_salary[-1]

    return [min_salary, max_salary, currency, tax]

def min_max_salary_sj(vacancy_salary): #Разбор зарплаты по минимальной, максимальной, валюте и налогам для superjob
    min_salary, max_salary = '', ''
    if vacancy_salary[0] == 'По договорённости':
        return [None, None, None, None]
    elif len(vacancy_salary) == 5: #когда есть только минимальная или максимальная ЗП
        if vacancy_salary[0][0] == 'о':
            for el in vacancy_salary[2]:
                if el.isdigit():
                    min_salary += el
        else:
            for el in vacancy_salary[2]:
                if el.isdigit():
                    max_salary += el
        currency = vacancy_salary[2][vacancy_salary[2].rfind(" ")+1:]
        period = vacancy_salary[4]
    elif len(vacancy_salary) == 9: #когда есть минимальная и максимальная ЗП
        for el in vacancy_salary[0]:
            if el.isdigit():
                min_salary += el
        for el in vacancy_salary[4]:
            if el.isdigit():
                max_salary += el
        currency = vacancy_salary[6]
        period = vacancy_salary[8]
    if min_salary == '':
        min_salary = None
    else:
        min_salary = float(min_salary)

    if max_salary == '':
        max_salary = None
    else:
        max_salary = float(max_salary)

    return [min_salary, max_salary, currency, period]

