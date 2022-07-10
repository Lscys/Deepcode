from cgitb import reset
from operator import ne
import re

def verify_format(hours_format=""):
    reg = re.compile("^(?:[01]?\d|2[0-3]):([0-5]\d):([0-5])\d$")
    return reg.search(hours_format) != None

def parse_format(hours_format=""):
    [hours, minutes, seconds] = hours_format.split(":")
    return (int(hours), int(minutes), int(seconds))

def assing_zero(num):
    return num if num > 9 else f"0{num}"

def parse_format_human(hours_to_seconds):
    hours = hours_to_seconds // 3600 
    hours_seg = hours * 3600

    minutes = (hours_to_seconds - hours_seg) // 60
    minutes_seg = minutes * 60

    seconds = hours_to_seconds - (hours_seg + minutes_seg)

    # add cero
    hours = assing_zero(hours)
    minutes = assing_zero(minutes)
    seconds = assing_zero(seconds)

    # return 
    return f"{hours}:{minutes}:{seconds}"


def add_minutes():
    hours_format = input("Ingrese la hora del dia en el formato (HH:MM:SS): ")
    if (not verify_format(hours_format)):
        return print("Formato incorrecto")

    next_minute = input("Ingrese los minutos de deseas sumar(45): ")

    next_minute = int(next_minute) if len(next_minute) > 0 else 45

    (hours, minutes, seconds ) = parse_format(hours_format)

    next_minute_seg = next_minute * 60
    hours_seg = int((minutes * 60 + seconds+ hours * 3600)+next_minute_seg)

    result = parse_format_human(hours_seg)

    print(result)

add_minutes()