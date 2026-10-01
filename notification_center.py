from notification_channel import NotificationChannel


class NotificationCenter:
    def __init__(self, channel):
        self.__channel = channel

    def change_channel(self, channel: NotificationChannel):
        self.__channel = channel

    def forward_notification(self, message: str) -> tuple[bool, str]:
        if not self.__channel:
            return False, 'Ошибка. Канал не выбран'

        return self.__channel.send_notification(message)
