#!/usr/bin/env python
"""
   isort:skip_file
"""
import os
import subprocess
import sys
from flask_script import Manager, Shell, Command
from app import create_app, db
from flasgger import Swagger


STAGE= "dev"
app = create_app(STAGE)

Swagger(app)
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command('shell', Shell(make_context=make_shell_context))
@manager.command
def runprod():
    cmd = 'uwsgi --ini uwsgi.ini'
    print('Running {}'.format(cmd))
    subprocess.call(cmd, shell=True)


@manager.command
def utest():
    import unittest
    tests = unittest.TestLoader().discover('utest')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def test():
    import pytest
    args = ['utest/', '-p', 'no:warnings', '-v']
    pytest.main(args)


@manager.add_command
class TestCommand(Command):
    name = 'pytest'
    capture_all_args = True

    # ex: args='utest/test_alerts.py -k test_miss_AppSecret_header_400'
    def run(self, args):
        import pytest
        default_arg = ['-p', 'no:warnings', '-rf']
        args += default_arg
        print(args)
        pytest.main(args)


@manager.command
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py src/app/'
    yapf = 'yapf -r -i *.py src/app/'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)

@manager.command
def pep(f):
    """Runs the yapf and isort formatters over the project."""
    pep = 'autopep8 --in-place --aggressive {}'.format(f)

    print('Running {}'.format(pep))
    subprocess.call(pep, shell=True)


@manager.command
def clean():
    """remove python cache"""
    cmd = 'find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf'
    print('Running {}'.format(cmd))
    subprocess.call(cmd, shell=True)
    print('cache cleaned')


@manager.command
def dockerup():
    up = 'docker-compose -f rd/docker-compose.yml up -d'
    print('Running {}'.format(up))
    subprocess.call(up, shell=True)


@manager.command
def dockerdown():
    up = 'docker-compose -f rd/docker-compose.yml down -v'
    print('Running {}'.format(up))
    subprocess.call(up, shell=True)


if __name__ == '__main__':
    manager.run()
