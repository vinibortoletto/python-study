from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def notify(self):
        pass


class MessageNotifier(Notifier):
    def __init__(self, profile, followers):
        self.profile = profile
        self.followers = followers
        self.profile.add_notification_system(self)

    def notify(self):
        print(f"Notifying via Messages: {self.followers}")


class PushNotificationNotifier(Notifier):
    def __init__(self, profile, followers):
        self.profile = profile
        self.followers = followers
        self.profile.add_notification_system(self)

    def notify(self):
        print(f"Notifying Push Notification: {self.followers}")


class EmailNotifier(Notifier):
    def __init__(self, profile, followers):
        self.profile = profile
        self.followers = followers
        self.profile.add_notification_system(self)

    def notify(self):
        print(f"Notifying Email: {self.followers}")
