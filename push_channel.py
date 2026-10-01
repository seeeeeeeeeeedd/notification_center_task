from notification_channel import NotificationChannel


class PushChannel(NotificationChannel):
    def send_notification(self, notification: str) -> tuple[bool, str]:
        return True, f'Вам пришло уведомление на Push {notification}'