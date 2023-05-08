from abc import ABC, abstractmethod


class Task(ABC):
    @abstractmethod
    def trigger_task(self):
        pass


class TurnLightsOn(Task):
    def __init__(self, alarm):
        self.alarm = alarm
        self.alarm.add_task_to_list(self)

    def trigger_task(self):
        print("Lights turned on")


class MakeCoffee(Task):
    def __init__(self, alarm):
        self.alarm = alarm
        self.alarm.add_task_to_list(self)

    def trigger_task(self):
        print("Coffee is done")


class TurnComputerOn(Task):
    def __init__(self, alarm):
        self.alarm = alarm
        self.alarm.add_task_to_list(self)

    def trigger_task(self):
        print("Computer turned on")
