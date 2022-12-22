# Collapsable xBlock
### Simple collapsable block with customizable title and content made
with eDx xBlock technology.

***
## How to install

- make a new directory and navigate into it



- create a new virtual environment
```
python3 -m venv venv
```


- activate created virtual environment
```
source venv/bin/activate
```

- clone this repository into the created directory
```
https://github.com/Cerne13/collapsible-xblock.git
```

- clone eDx xBlock SDK into the main directory
```
git clone https://github.com/openedx/xblock-sdk.git
```

- navigate to SDK directory and install needed dependencies
```
cd xblock-sdk
pip install -r requirements/base.txt
```

- make migrations
```
python manage.py migrate
```

- return to main project directory
```angular2html
cd ..
```

- install cloned xBlock so it can be used by development kit
```
pip install -e testxblock
```

- run local server
```
python xblock-sdk\manage.py runserver
```
