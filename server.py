import websockets
import asyncio
import numpy
import json

from typing import *
from dataclasses import dataclass, field
from _thread import start_new_thread

def encode_msg(msg: Dict) -> str:
  return json.dumps(msg, ensure_ascii=False)

def decode_msg(msg: str) -> Dict:
  return json.loads(msg)


@dataclass
class Client:
  socket: Any 
  id: int
  disconnected: bool = False

