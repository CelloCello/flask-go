# -*- coding: utf-8 -*-
import os
import argparse
import re

import flask_go
from base import BaseCommand


class Command(BaseCommand): 
    def __init__(self):
        pass

    def execute(self, subcmd):
        subcmd_dict = self.parse_subcmd(subcmd)
        proj_name = subcmd_dict["project_name"]
        directory = subcmd_dict["directory"]
        tmp_from_path = subcmd_dict["template"]
        if directory:
            directory = os.path.abspath(os.path.expanduser(directory))
            directory = os.path.join(directory, app_name)
        else:
            directory = os.path.join(os.getcwd(), proj_name)

        template_path = self.get_template(tmp_from_path)
        prefix_length = len(template_path) + 1
        #print "temp path: " + template_path
        print "create projcet [%s] in direct: %s" % (proj_name, directory)
        for root, dirs, files in os.walk(template_path):
            
            # make dirs
            path_rest = root[prefix_length:]
            root_reset = path_rest.replace("project_template", proj_name)
            root_reset = root_reset.replace("project_name", proj_name)
            dir_path = os.path.join(directory, root_reset)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

            # read template files and write to directory
            for filename in files:
                if filename.endswith(('.pyo', '.pyc', '.py.class')):
                    # Ignore some files as they cause various breakages.
                    continue

                # read template
                tmp_path = os.path.join(root, filename)
                with open(tmp_path, 'rb') as tmp_file:
                    content = tmp_file.read()
                    content = re.sub(r"%(?!\(\w+\)s)", "%%", content)
                    content %= subcmd_dict

                # write to directory
                dest_path = os.path.join(dir_path, filename.replace("project_name", proj_name))
                with open(dest_path, 'wb') as new_file:
                    new_file.write(content)

    def parse_subcmd(self, subcmd):
        """parse subcmd from list to directory with key you set
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('project_name', help='Name of the application or project.')
        parser.add_argument('directory', nargs='?', help='Optional destination directory')
        parser.add_argument('--template', help='The path to load the template from.')
        args = parser.parse_args(subcmd)
        return vars(args)

    def get_template(self, from_path):
        if from_path is None:
            return os.path.join(flask_go.__path__[0], "project_template")
        else:
            expanded_template = os.path.expanduser(from_path)
            expanded_template = os.path.normpath(expanded_template)
            if os.path.isdir(expanded_template):
                return expanded_template

        raise Exception("error in template: " + from_path)