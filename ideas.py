def show_ideas(ideas):
    print("== Лист идей ==")
    for n, t in enumerate(ideas, start=1):
        print(f"{n}. {t['name']} | Тема: {t['topic']} | Сложность: {t['difficulty']}")

def add_ideas(ideas, name, topic, difficulty):
    new_idea = {
        "name": name,
        "topic": topic,
        "difficulty": difficulty
    }

    ideas.append(new_idea)
    print(f"Идея добавлена: {name} | Тема: {topic} | Сложность: {difficulty}")
