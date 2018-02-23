from re import *

def fbin(num = "0"):
    return int("0b" + num,  2)

def ibin(num = 0):
    return sub(r"0b",  " ",  str(bin(num)))



def foct(num = "0"):
    return int("0o" + num,  8)

def ioct(num = 0):
    return sub(r"0o",  " ",  str(oct(num)))



def fhex(num = "0"):
    return int("0x" + num,  16)

def ihex(num = 0):
    return sub(r"0x",  " ",  str(hex(num)))
