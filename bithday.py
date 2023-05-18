from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    today = datetime.now().date()

    # Визначаємо дату початку тижня (понеділок)
    start_of_week = today - timedelta(days=today.weekday())

    # Визначаємо дату кінця тижня (неділя)
    end_of_week = start_of_week + timedelta(days=6)

    # Створюємо словник, де ключ - день тижня, а значення - список імен користувачів
    birthdays_per_day = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }

    # Проходимо по користувачам і додаємо їх імена до відповідних списків залежно від дня народження
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        
         # Визначаємо дату народження з поточним роком
        birthday_this_year = datetime(
            today.year, birthday.month, birthday.day).date()

        # Перевіряємо, чи день народження користувача потрапляє в поточний тиждень
        if start_of_week <= birthday <= end_of_week:
            # Визначаємо день тижня для дня народження
            if birthday.weekday() >= 5:  # Якщо день народження - субота або неділя
                weekday = 'Monday'  # Привітання в понеділок
            else:
                weekday = birthday.strftime('%A')

            # Додаємо ім'я користувача до списку відповідного дня тижня
            birthdays_per_day[weekday].append(name)

    # Виводимо список користувачів по днях народження
    for weekday, names in birthdays_per_day.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")


# Приклад використання функції
users = [
    {'name': 'John', 'birthday': datetime(2023, 5, 16)},
    {'name': 'Alice', 'birthday': datetime(2023, 5, 17)},
    {'name': 'Bill', 'birthday': datetime(2023, 5, 18)},
    {'name': 'Jill', 'birthday': datetime(2023, 5, 18)},
    {'name': 'Kim', 'birthday': datetime(2023, 5, 20)},
    {'name': 'Jan', 'birthday': datetime(2023, 5, 20)},
]

get_birthdays_per_week(users)
