class NotificationChannel:
    def send_notification(self, notification: str) -> tuple[bool, str]:
        return False, 'Канал не настроен'
