# Collapsable xBlock
### Simple collapsable block with customizable title and content made
with eDx xBlock technology.

***
### How to install

It is strongly recommended that you use Linux/Mac while working with technology.\
Using Windows may cause unpredictable troubles while installing your project and SDK.

- Be sure you're using Python 3.8 to avoid troubles installing the project

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
```
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

***
### Troubleshooting

There can be some cases when SDK doesn't install all the dependencies properly.
In that case you will see a PluginMissingError when attempting to launch the xBlock.

To get rid of the problem you should:

- navigate to the SDK folder
```
cd xblock-sdk
```
- make sure you have a var folder (if not, create it manually)


Then:

- if you are on Linux/Mac\
run
```
make install
```
- if you are on Windows:
```
pip install -qr requirements/dev.txt --exists-action w
```
