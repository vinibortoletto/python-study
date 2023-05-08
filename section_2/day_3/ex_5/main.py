from alarm import Alarm
from task import MakeCoffee, TurnComputerOn, TurnLightsOn

alarm = Alarm()

TurnLightsOn(alarm)
MakeCoffee(alarm)
TurnComputerOn(alarm)

alarm.trigger_alarm()
