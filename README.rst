# flask-go
Let you create flask project like use django-admin


# install

	pip install flask-go


# How to use
It has two command now, `startproject` and `startapp`.
If you familiar with Django, use `flask-go` just like django-admin.

## create project

	flask-go startproject project_name

It will create project in current folder.
if you want to create into specific path, you can:

	flask-go startproject project_name destination

## use your own template
If you want to use your own project template files, `flask-go` also support `--template` command option.

	flask-go startproject project_name --template /Users/Cello/Code/my_project_template

`flask-go` will replace `project_name` string in folder, file and code text.

## create blueprint
Like `startproject` command, but change to use `startapp`.

	flask-go startapp myapp

`startapp` also support creat into specific path and `--template` command option.