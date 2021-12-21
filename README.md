# Tedee Garmin intergation

Simple Tedee Gerda Lock / Garmin watch integration

## Description

I want to go running only with my watch. I like to not remember about
carring keys, phone and other stuff. Purpose for this project is
create Garmin watch (FR945 in my case) integration with my Tedee lock.

When I was creating this simple integration I followed few problems:
* I want to create Garmin ConnectIQ App but Garmin not support key 
authentication for teede key lock
* Garmin Support first bluetooth second is wi-fi connection

According to first point I created own API which is running on
RPI in my local wi-fi network. Garmin watch send request to endpoint
using APICall Garmin App. It is simple request like:
```
curl -X POST "http://192.168.0.108:8080/open"
```
After that my local API send request to Tedee
API and my doors opens (!)
I need only stay in my home wi-fi signal in front of my house doors.

### Running

Export PKEY variable
```
export PKEY="PersonalKey 8XXXXXXXXXXXXXXXXXXXXXXXXXXXX="
```

Run command on RPI
```
poetry run gunicorn tedee_garmin.server:lock_app -b 0.0.0.0 -k uvicorn.workers.UvicornWorker --daemon
```

### Contact
andrzej@michalski.in

