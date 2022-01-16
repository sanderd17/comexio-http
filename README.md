# comexio-http
Python implementation for the Comexio HTTP API

## Documentation

Go to `/admin/api/home` on your Comexio server and enable the HTTP API with a chosen user and password. Enable access for the wanted endpoints.

This repo includes a demo scrip to test your communication, run it as
```
$ python main.py -h
usage: main.py [-h] [--hostname HOSTNAME] [--user USER] [--password PASSWORD]

options:
  -h, --help           show this help message and exit
  --hostname HOSTNAME
  --user USER
  --password PASSWORD
```

This will prompt you to connect to the Comexio server, and guide you through the proces to get and set variables.
The hostname, user and password are optional, and will be requested when not given as an option.


## Warning

This library uses basic HTTP authentication, as this is the only authentication method offered.
This method sends your password in plain text for every request. This can be sniffed by any device on your WiFi network, or any server or router your signal has to pass.

Only use this library in a local network.

## Legal

License: MIT - http://opensource.org/licenses/MIT

"Comexio" is a trademark owned by Comexio GmbH, see www.comexio.com for more information. I am in no way affiliated with the Comexio organization.
