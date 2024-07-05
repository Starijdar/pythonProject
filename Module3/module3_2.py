def send_email(message, recipient, *, sender="university.help@gmail.com"):
    count = 0
    for i in recipient:
        if i == "@":
            count += 1

    if ".com" in recipient or ".ru" in recipient or ".net" in recipient:
        count += 1

    if ".com" in sender or ".ru" in sender or ".net" in sender:
        count += 1

    if sender == recipient:
        print("Нелзья отправлять сообщение самому себе")
        return

    if count >= 3:
        if sender == "university.help@gmail.com":
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
