import datetime
import random

def handle(cmd):
    if not cmd:
        return "Не расслышал"
    if "привет" in cmd:
        return "Привет! Я твой ассистент."
    if "время" in cmd:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"Сейчас {now}"
    if "дата" in cmd or "число" in cmd:
        today = datetime.datetime.now().strftime("%d.%m.%Y")
        return f"Сегодня {today}"
    if "шутка" in cmd or "анекдот" in cmd:
        jokes = [
            "Почему программисты путают Хэллоуин и Рождество? Потому что OCT 31 == DEC 25.",
            "Я не ленивый, я в энергосберегающем режиме."
        ]
        return random.choice(jokes)
    if "пока" in cmd or "стоп" in cmd or "выключи" in cmd:
        return "Пока!"
    return "Не понял команду"

def main():
    print("Ассистент запущен (тестовая версия)")
    while True:
        try:
            cmd = input("Введи команду: ")
        except EOFError:
            break
        print("Ты:", cmd)
        if "пока" in cmd or "стоп" in cmd or "выключи" in cmd:
            print("Ассистент: Пока")
            break
        answer = handle(cmd)
        print("Ассистент:", answer)

if __name__ == "__main__":
    main()
