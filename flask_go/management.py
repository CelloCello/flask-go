# -*- coding: utf-8 -*- 

import sys
from importlib import import_module

app_name = "flask_go"
commands = {
    "startproject": "create a project",
    "startapp": "create a blueprint app",
}


def load_command_class(name):
    module = import_module("%s.commands.%s" % (app_name, name))
    return module.Command()


def get_command(name):
    try:
        commands[name]
    except:
        print "Unknow command: %r" % name
        return None

    return load_command_class(name)


def help_text():
    text = [
        "Available subcommands:",
        ""
    ]

    for key, value in commands.iteritems():
        cmd_text = "%s\t\t%s" % (key, value)
        text.append(cmd_text)

    return "\n".join(text) + "\n\n"


def execute_from_command_line():
    try:
        cmd = sys.argv[1]
    except IndexError:
        cmd = "help"

    try:
        subcmd = sys.argv[2:]
    except:
        print "error"

    if cmd == "help":
        sys.stdout.write(help_text())
    else:
        exe = get_command(cmd)
        if exe:
            exe.execute(subcmd)
