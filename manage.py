from chief import app
from flask.ext.script import Manager, Server


if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command("runserver", Server())
    manager.run()
