# jong_imp

Import of notes into joplin from your cloud service

## prerequisite

* Python 3.4 or +
* [joplin terminal](https://joplin.cozic.net/terminal/) installed

## installing

* create a virtualenv and activate it

```python 
python3 -m venv jong_imp
cd jong_imp
source bin/activate
```

* get the source 

```python
git clone https://github.com/foxmask/jong_imp
cd jong_imp
```

## settings 

in `the jong_imp/settings.ini` file set the following properties
 
```python 
[JOPLIN_CONFIG]
# path to the joplin terminal version
JOPLIN_BIN_PATH = /home/foxmask/.joplin-bin/bin/joplin
# path to the profile of the joplin client (terminal/desktop)
JOPLIN_PROFILE_PATH = /home/foxmask/.config/joplin-desktop
# path to the folder of the cloud storage service
joplin_import_folder = /home/foxmask/Dropbox/Applications/Joplin/letterbox/
# default folder where to import notes
JOPLIN_DEFAULT_FOLDER = Home
```

## running

you can set a crontab or a "at" service to trigger the command at the given time you want

```python
python jong_imp/go.py 
```
