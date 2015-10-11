# -*- coding: utf-8 -*-


class BaseCommand(object): 
    def __init__(self):
        pass

    def execute(self, *args):
        pass

    def add_arguments(self, subcmd):
        """parse subcmd from list to directory with key you set
        """        
        pass