from collections import Counter


class Statistic:
    def __init__(self):
        self._number_list = [1, 2, 3]

    def average(self):
        total_sum = sum(self._number_list)
        length = len(self._number_list)
        return total_sum / length

    def median(self):
        sorted_number_list = sorted(self._number_list)
        number_list_length = len(sorted_number_list)
        index = number_list_length // 2

        if number_list_length % 2 == 0:
            middle = sorted_number_list[index - 1] + sorted_number_list[index]
            return middle / 2

        return sorted_number_list[index]

    def mode(self):
        number, _ = Counter(self._number_list).most_common()[0]
        return number
