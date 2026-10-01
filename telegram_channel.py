from notification_channel import NotificationChannel


class TelegramChannel(NotificationChannel):
    def send_notification(self, notification: str) -> tuple[bool, str]:
        return True, f'Вам пришло сообщение в Telegram: {notification}'