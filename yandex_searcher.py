import time
class User:
    def __init__(self, first_name, last_name, middle_name, email):
        self.firstname = first_name
        self.lastname = last_name
        self.middlename = middle_name
        self.email = email

users = [
    User('Иван', 'Иванов', 'Иванович', 'ivanchik@yandex.ru'),
    User('Петька', 'Петров', 'Иванович', 'petya@yandex.ru'),
    User('Александр', 'Петров', 'Эдуардович', 'sanya@yandex.ru'),
    User('Александр', 'Иванов', 'Иванович', 'kek@yandex.ru'),
]

def search_users(query):
    results = []
    query_parts = query.split()

    for user in users:
        full_name = f"{user.firstname}{user.middlename}{user.lastname}{user.email}"
        if all(part.lower() in full_name.lower() for part in query_parts):
            results.append(user)
    return results

print("База данных пользователей:")

for user in users:
    print(f"{user.firstname} {user.lastname} {user.middlename} - {user.email}")
print("- - - - - - - - - ")
query = input("Введите запрос для поиска по базе данных (это может быть неполное имя или строка): ")
found_users = search_users(query)
for user in found_users:
    print(f"{user.firstname} {user.lastname} {user.middlename} - {user.email}")

print("Программа закроется через 30 секунд")
time.sleep(30)