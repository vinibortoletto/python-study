GREEN = "\033[92m"
ORANGE = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


class Log:
    def send_log(self, message):
        return message


class LogError:
    def __init__(self, log):
        self.log = log

    def send_log(self, message):
        return f"{RED}{self.log.send_log(message)}{RESET}"


class LogWarning:
    def __init__(self, log):
        self.log = log

    def send_log(self, message):
        return f"{ORANGE}{self.log.send_log(message)}{RESET}"


class LogSuccess:
    def __init__(self, log):
        self.log = log

    def send_log(self, message):
        return f"{GREEN}{self.log.send_log(message)}{RESET}"


if __name__ == "__main__":
    log = Log()
    print(LogError(log).send_log("The system has errors."))
    print(LogWarning(log).send_log("The system is slow."))
    print(LogSuccess(log).send_log("The system is working."))
