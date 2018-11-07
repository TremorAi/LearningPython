__author__ = "Tremor"
from register import register
import random

@register("coin", False)
async def command_coin():
    print("test")
