# bitget balance file generator
this creates and constantly updates a text
file with your bitget futures account balance in USDT
in order to use as a source for OBS

## How to use
### Requirements
- python >= 3.10 
- bitget readonly api

<br />
<br />

run
```
pip install -r requirements.txt
```

create a .env file in the project and populate it like this
```
API_KEY = "yourbitgetapikey"
SECRET_KEY = "yourbitgetsecretkey"
PASSPHRASE ="yourbitgetpassphrase"
```

run
```
python main.py
```

this will generate a `balance.txt` file that will update every 2 seconds
you can then use this as a source in obs