from datetime import date, datetime, timedelta

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def get_birthdays_per_week(users):
    """
    input is a dictionary with a list of users and their birthdays in datetime format and return type is dictionary,
    with keys as week days and value names of users that should be congratulated
    :param users: dict {Name : string
                        birthday: datetime}
    :return: return dict {'Monday': ['Bill', 'Jan'],
                          'Wednesday': ['Kim']}
    """
    # Реалізуйте тут домашнє завдання
    birthday_per_day = dict()
    week = (datetime.today() + timedelta(days=7)).date()
    year = datetime.today().year

    for user in users:
        if (user['birthday'].year - year) < -1:  # Перевіряю вказаний рік у днях народженні
            user['birthday'] = datetime(year=year, month=user['birthday'].month, day=user['birthday'].day).date()
        if date.today() <= user['birthday'] <= week:  # main check function, if birthday will be next week
            birth_day = user['birthday'].weekday() if user['birthday'].weekday() < 5 else 0
            # print(user['birthday'], "Yes", days_name[user['birthday'].weekday()])
            if days_name[birth_day] in birthday_per_day:
                birthday_per_day[days_name[birth_day]].append(user["name"])
            else:
                birthday_per_day[days_name[birth_day]] = [user["name"]]

    # print(birthday_per_day)
    return birthday_per_day


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2024, 1, 9).date()},
        {"name": "Juan", "birthday": datetime(2024, 1, 11).date()},
        {
            "name": "Alice",
            "birthday": (datetime(2021, 1, 14)).date(),
        },

    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
