from flask import Flask
from flask_script import Manager, Shell

app = Flask(__name__)

manager = Manager(app)


# 为shell自动导入模块和相关类
def make_shell_context():
    return dict(app=app)


manager.add_command('shell', Shell(make_context=make_shell_context))


# 定义路由和视图函数
@app.route('/', methods=['GET', 'POST'])
def index():
    return 'hello, world!'

from app import app as application
if __name__ == '__main__':
    manager.run()
