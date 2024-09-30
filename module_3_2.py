def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    #check_list = ("@", ".com", ".ru", ".net")
    #check = all(item not in (recipient and sender) for item in check_list)
    #if check:
    if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    return send_email

#send_email("jnjnfjfn", "univer.help@gmail.com", sender = "univer@gmail.com")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = "urban.info@gmail.com")
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = "urban.teacher@mail.uk")
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = "urban.teacher@mail.ru")
