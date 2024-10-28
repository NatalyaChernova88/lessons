def send_email(message, recipient, *, sender='univercity.help@gmail.com'):
    if '@' not in sender or '@' not in recipient or not sender.endswith(('.com', '.ru', '.net')) or not recipient.endswith(('.com', '.ru', '.net')):
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
    elif sender == recipient:
        print ('Невозможно отправить письмо самому себе!')
    elif sender == 'univercity.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ',recipient)
    else:
        print('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
send_email('message', 'univercity.he@gmail.com')
