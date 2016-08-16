#!/usr/bin/env python
# TODO: add in docstrings
import os
from app import create_app
from app.models import *
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

# TODO: update context names to new table names ex: Post -> Story
# TODO: add docstring
def make_shell_context():
    return dict(app=app, db=db, Story=Story, Tag=Tag, StoryTag=StoryTag,
                Role=Role, User=User, StoryEdit=StoryEdit, Flag=Flag, Feedback=Feedback)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()

