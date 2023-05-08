class Alarm:
    def __init__(self):
        self.task_list = []

    def add_task_to_list(self, task):
        self.task_list.append(task)

    def trigger_all_task(self):
        for task in self.task_list:
            task.trigger_task()

    def trigger_alarm(self):
        print("Alarm triggered")
        self.trigger_all_task()
