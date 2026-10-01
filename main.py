from notification_center import NotificationCenter
from email_channel import EmailChannel
from push_channel import PushChannel
from telegram_channel import TelegramChannel

commands = {
    '1': 'Выбрать канал',
    '2': 'Отправить сообщение',
    '3': 'Выйти из программы'
}

CHOOSE_CHANNEL_COMMAND, SEND_MESSAGE_COMMAND, EXIT_COMMAND = commands.keys()

channels = {
    '1': 'Email',
    '2': 'Телеграм',
    '3': 'Push'
}

CHANNEL_EMAIL, CHANNEL_TELEGRAM, CHANNEL_PUSH = channels.keys()

notification_center = NotificationCenter(None)

is_program_running = True

while is_program_running:

    print()
    for number, command in commands.items():
        print(f'{number}: {command}')

    user_command_number = input('Выберете действие и укажите его номер: ').strip()

    if user_command_number in commands.keys():
        if user_command_number == CHOOSE_CHANNEL_COMMAND:
            for number, command in channels.items():
                print(f'{number}: {command}')

            user_channel_number = input('Укажите номер выбранного канала: ').strip()

            if user_channel_number in channels.keys():
                if user_channel_number == CHANNEL_EMAIL:
                    notification_center.change_channel(EmailChannel())
                elif user_channel_number == CHANNEL_TELEGRAM:
                    notification_center.change_channel(TelegramChannel())
                elif user_channel_number == CHANNEL_PUSH:
                    notification_center.change_channel(PushChannel())
            else:
                print('Неизвестный номер. Попробуйте снова')
        elif user_command_number == SEND_MESSAGE_COMMAND:
            user_message = input('Введите сообщение: ').strip()
            success, message = notification_center.forward_notification(user_message)
            print(message)
        elif user_command_number == EXIT_COMMAND:
            is_program_running = False
            print('Выход из программы')
    else:
        print('Неизвестная команда. Попробуйте снова')
