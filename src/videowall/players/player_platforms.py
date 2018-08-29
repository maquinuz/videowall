from .player_exceptions import PlayerException


class PlayerPlatform(object):
    pass


class PlayerPlatformX86(PlayerPlatform):
    pass


class PlayerPlatformRaspberryPi(PlayerPlatform):
    pass


_string_player_platform_map = {
  "x86": PlayerPlatformX86,
  "rpi": PlayerPlatformRaspberryPi
}

_platform_player_string_map = {
  PlayerPlatformX86: "x86",
  PlayerPlatformRaspberryPi: "rpi"
}


def player_platform_from_string(string):
    try:
        platform = _string_player_platform_map[string]
    except KeyError as e:
        raise PlayerException(e)
    else:
        return platform


def string_from_player_platform(player_platform):
    try:
        string = _platform_player_string_map[player_platform]
    except KeyError as e:
        raise PlayerException(e)
    else:
        return string


def get_player_platform_strings():
    return _string_player_platform_map.keys()


def get_player_platforms():
    return _string_player_platform_map.values()
