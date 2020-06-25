
# DJ-CTC

Call people using Python. Below is a step by step guide on the tools you'll need and how to install and configure each.

List of tools are as follows:
* Python (version 3)
* pip
* virtualenv
* Twilio(free account to use their  API)
* Twilio's python helper library 

## Installation

first things first. Install app dependencies.
```bash
virtualenv phoneapp
```

Invoke the `activate` script with the virtunlenv `bin/` directory to python executable.
```bash 
source phoneapp/bin/activate
```


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Twilio. (Note you will have to create a free twilio account before this. You can create an account here [Twilio](https://www.twilio.com/try-twilio).

```bash
pip install twilio
```

```bash
easy_install twilio
````

Once you have installed twilio and edited the script, you can run the script with the following command:
```bash
python phone_calls.py
````

