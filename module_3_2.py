# создаём функцию send_email
def send_email(message,recipient,sender = "univerity.help@gmail.com"):
    if("@"and(".com"or".ru"or".net")) not in (recipient or sender) or("@" or(".com"or"ru"or".net")) not in (recipient or sender):
        # создаём  1 условие
        print(f"Невозможно отправить письмо с адреса {sender}на адрес {recipient}")
    elif recipient == sender:
        # создём 2 условие
        print("Нельзя отправить письмо самому себе!")
        # создаём 3 условие
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса{sender} на адрес {recipient}.")
        # создаём 4 условие
    elif sender !="university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        # вывод результата
        send_email('messagje','university.help@mail.com','@.com')
        send_email('messagje','university.help@mail.com')
        send_email('messagje','universi@.com')
        send_email('messagje','universi@.co')
        send_email('messagje','universi@.com')