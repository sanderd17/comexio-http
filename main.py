#! /bin/python

import asyncio
import argparse

from aiohttp import ClientSession
from getpass import getpass

from comexio import Auth, IO, Marker, Onewire

def choose(*options):
  print("Please choose:")
  for idx, element in enumerate(options):
    print(" {}) {}".format(idx+1,element))
  i = input("Enter number: ")
  try:
    if 0 < int(i) <= len(options):
      return options[int(i) - 1]
  except:
    pass
  return None

def get_tag(auth: Auth):
  type = choose("io", "marker", "onewire")
  if type == "io":
    ext = input("Extension name (i.e. \"IO-Server\"): ")
    io = input("Address (i.e. \"Q1\"): ")
    return IO(ext, io, auth)
  elif type == "marker":
    address = input("Address (i.e. \"M1\"): ")
    return Marker(address, auth)
  elif type == "onewire":
    address = input("Address (i.e. \"OT1\"): ")
    return Onewire(address, auth)

def get_value(auth: Auth):
  tag = get_tag(auth)
  asyncio.run(tag.async_get())
  print(f"Value: {tag.value}")

def set_value(auth: Auth):
  tag = get_tag(auth)
  value = input("Value: ")
  asyncio.run(tag.async_set(value))
  print(f"Value: {tag.value}")

def main(auth: Auth):
  choice = input("g/s/q/h? ")
  if choice == "g":
    get_value(auth)
  elif choice == "s":
    set_value(auth)
  elif choice == "q":
    asyncio.run(auth.session.close())
    exit()
  else:
    print("Choose an option:")
    print(" g) Get value")
    print(" s) Set value")
    print(" q) Quit")
    print(" h) Help")
  main(auth)

async def create_session():
    return ClientSession()

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--hostname', type=str)
  parser.add_argument('--user', type=str)
  parser.add_argument('--password', type=str)
  args = parser.parse_args()

  host = args.hostname or input("Hostname: ")
  user = args.user or input("User: ")
  password = args.password or getpass()
  session = asyncio.run(create_session())
  auth = Auth(session, host, user, password)
  main(auth)