from tv import Tv
import pytest


def test_create_tv():
    tv = Tv(40)
    assert tv._volume == 50
    assert tv._channel == 1
    assert tv._size == 40
    assert tv._is_on is False


def test_turn_volume_up():
    tv = Tv(40)
    tv.turn_volume_up()
    assert tv._volume == 51


def test_turn_volume_down():
    tv = Tv(40)
    tv.turn_volume_down()
    assert tv._volume == 49


def test_change_channel():
    tv = Tv(40)
    tv.change_channel(5)
    assert tv._channel == 5

    with pytest.raises(ValueError):
        tv.change_channel(0)

    with pytest.raises(ValueError):
        tv.change_channel(100)


def test_turn_on_off():
    tv = Tv(40)

    tv.turn_on_off()
    assert tv._is_on is True

    tv.turn_on_off()
    assert tv._is_on is False
