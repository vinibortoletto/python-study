from statistic import Statistic


def test_create_statistic():
    statistic = Statistic()
    assert statistic._number_list == [1, 2, 3]


def test_average():
    statistic = Statistic()
    assert statistic.average() == 2


def test_median():
    statistic = Statistic()
    assert statistic.median() == 2


def test_mode():
    statistic = Statistic()
    assert statistic.mode() == 1
