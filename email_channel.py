from notification_channel import NotificationChannel


class EmailChannel(NotificationChannel):
    def send_notification(self, notification: str) -> tuple[bool, str]:
        return True, 'Вам пришло письмо на Email'
