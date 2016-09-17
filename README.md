# twilio-app

Message to twilio number and get the latest update of cricket Score of Live Matches.

Installation
------------

1. First clone this repository and ```cd``` into it.

```
git clone https://github.com/DeepeshAggarwal/twilio-app.git
cd twilio-app
```
2. If you want to create virtualEnv.
```
virtualenv ENV
source bin/activate
```
more about virtual env. can be read [here](https://virtualenv.pypa.io/en/stable/userguide/)

3. Install the dependencies
```
sudo python -m requirements.txt
```

Usage
------------

1. Run Flask Server
```
export FLASK_APP=main.py
flask run
```

2. Use ngrok to make it accesible to outside Network
```
ngrok http 5000
```

3. Configure your Twilio SMS with URL obtained from previous command like ``` http://ae3c0dfa.ngrok.io ```
```
http://ae3c0dfa.ngrok.io/sms
```
