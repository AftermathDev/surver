# le epic surver for gaem

import sys
import numpy
import socket
import selectors
import argparse

parser = argparse.ArgumentParser()

fallback = {         # in case the user did not supply any arguments
  ip = "127.0.0.1",
  port = 25454
}

parser.add_argument("-ip", type=str)
parser.add_argument("-port","-p", type=int)

