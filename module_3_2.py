def send_email(message, recipient, sender="university.help@gmail.com"):
    def is_correct_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))
# чек на корректность написания адреса
    if not is_correct_email(sender) or not is_correct_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        # чек на адресацию отправителя и получателя
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        # чек на разговоры с самим собой. Хотя отправить письмо себе же порой вполне себе нужно
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        # чек на стандартного отправителя
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Раз-раз, звуки щелчка об микрофон', 'crazyjoe@gmail.com')
send_email('Вас заметили учителя, сами виноваты!', 'poorstudent@mail.ru', sender='urban.info@gmail.com')
send_email('И вновь продолжается работа над ошибками', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Не спи после работы, у нас сеанс связи', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# хотелось поменять все тексты. Но я сдержался