from ideas import *

idea_list = [
    {
        "name": "Трекер привычек",
        "topic": "Консольное приложение",
        "difficulty": "Средняя",
    },
    {
        "name": "Учет расходов",
        "topic": "Финансы",
        "difficulty": "Простая",
    },
    {
        "name": "Генератор паролей",
        "topic": "Утилиты",
        "difficulty": "Простая",
    },
]

show_ideas(idea_list)

check_if_add_new_idea = input("Хотите создать новую идею? (да/нет) ")

if check_if_add_new_idea == "да":
    name = input("Напишите название проекта: ")
    topic = input("Наипшите тему проекта: ")
    difficulty = input("Напишите сложность проекта: ")

    add_ideas(idea_list, name, topic, difficulty)

    print("Обновлённый список: ")
    show_ideas(idea_list)