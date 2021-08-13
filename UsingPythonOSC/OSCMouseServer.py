# OSCMouseCapturer Starting Here
# The Modules
from pythonosc import dispatcher
from pythonosc import osc_server
import argparse

# The Functions
# The Print Functions
def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

def print_compute_handler_var(args, volume):
  volume = args

# The Main Program
# This guy run's the client OSC side for the python
def main():
  global dispatcher
  global osc_server
  # Argparse Arguments for Server Ip Address and Port (Because, it works on the documentation version...)
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  # The Server Part
  # The Dispatchers
  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/MousePos", print)
  # The Server Part
  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  # The try and Except part (to check whether the program is running or not)
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    print('Closing Time!!!')
    server.server_close()

# If statement on when the program starts
if __name__ == "__main__":
  main()
