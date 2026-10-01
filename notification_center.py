from notification_channel import NotificationChannel


class NotificationCenter:
    def __init__(self, channel):
        self.__channel = channel

    def change_channel(self, channel: NotificationChannel):
        self.__channel = channel

    def forward_notification(self, message: str) -> tuple[bool, str]:
        return self.__channel.send_notification(message)
