# Georide_api_usage

georide_api_usage is a repo used to store multiple ways of usage of the api.georide.fr

With the current script you can:
  - Lock/Unlock your first tracker
  - Lock/Unlock by tracker ID
  - Lock/Unlock by tracker Name
  - List all of you trackers

## Setup

  - Refer your login and password in the two variables and let's go !


### Usage

georide_api_usage requires python3 to run.

To lock your first tracker
```sh
$ python usage.py --action lock
```

To unlock the XXX tracker
```sh
$ python usage.py --action unlock --id XXX
```

To lock the SSS tracker
```sh
$ python usage.py --action lock --name SSS
```

To list all of your trackers
```sh
$ python usage.py --action list
```
