# coding: utf-8
# python lib
import configparser
import os
from pathlib import Path
import shlex
import subprocess

"""
    Joplin Importer:
    ================
    
    Use it to import file in markdown from the cloud storage service

    example: 

    >>> from jong_imp.go import go
    >>> go()
    
    or  

    >>> from jong_imp.go import JongImp
    >>> file = '/somewhere/Dropbox/Applications/Joplin/letterbox/foorbar.md'
    >>> ji = JongImp()
    >>> ji.import_note(file)

"""
cwd = Path.cwd()

config = configparser.ConfigParser()
config.read(str(cwd) + '/jong_imp/settings.ini')


class JongImp:
    """
    Jong Importer class to deal with markdown files located on the cloud storage service to import in Joplin
    """

    def _command(self, file):
        """
        command to build
        :param file: file to import
        :return: built command
        """

        command = config['JOPLIN_CONFIG']['JOPLIN_BIN_PATH']

        if config['JOPLIN_CONFIG']['JOPLIN_PROFILE_PATH']:
            command += ' --profile {}'.format(config['JOPLIN_CONFIG']['JOPLIN_PROFILE_PATH'])

        command += ' import {} {}'.format(file, config['JOPLIN_CONFIG']['JOPLIN_DEFAULT_FOLDER'])
        return command

    def _joplin_run(self, file):
        """
        command to run
        :param file: the file to import
        """

        args = shlex.split(self._command(file))

        result = subprocess.run(args)

        if result.returncode == 0:
            os.unlink(file)

    def import_note(self, file):
        """
        importing a file
        :param file: file to import
        """
        self._joplin_run(file)


def go():
    """
    read the folder of the file to import
    """

    ji = JongImp()
    files = Path(config['JOPLIN_CONFIG']['JOPLIN_IMPORT_FOLDER']).glob('*.md')
    for file in files:
        ji.import_note(file)


if __name__ == '__main__':
    go()
