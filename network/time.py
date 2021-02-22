from typing import Dict
import datetime


def time_from_string(time_string):
    pieces = [int(x) for x in time_string.split(":")]
    if len(pieces) == 3:
        hours, minutes, seconds = pieces
        return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    hours, minutes = pieces
    return datetime.timedelta(hours=hours, minutes=minutes)


def time_range_from_string(time_string):
    pieces = time_string.split("-")
    assert len(pieces) == 2
    return tuple(time_from_string(piece.strip()) for piece in pieces)


def stringify_timedelta(td):
    seconds = td.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))


DAYS_OF_WEEK = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]
