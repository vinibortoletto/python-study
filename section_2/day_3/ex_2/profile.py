from notifier import MessageNotifier, EmailNotifier, PushNotificationNotifier


class Profile:
    def __init__(self):
        self.__notification_system_list = []
        self.__new_post = None

    def add_notification_system(self, system):
        self.__notification_system_list.append(system)

    def remove_notification_system(self, system):
        self.__notification_system_list.remove(system)

    def notify_all(self):
        for system in self.__notification_system_list:
            system.notify()

    def show_post(self):
        print(f"\nPost: {self.__new_post}\n")

    def add_post(self, post):
        self.__new_post = post
        self.show_post()
        self.notify_all()


if __name__ == "__main__":
    followers_message = ["Calors", "Claudia"]
    followers_push = ["Carlos"]
    followers_email = ["Cladia", "Betina"]

    my_profile = Profile()
    MessageNotifier(my_profile, followers_message)
    PushNotificationNotifier(my_profile, followers_push)
    EmailNotifier(my_profile, followers_email)

    my_profile.add_post("This is a Hollow World!")
