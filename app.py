from flask import Flask
from bss import Bss
from ecs import Ecs
from rds import Rds

app = Flask(__name__)


@app.route('/metrics')
def metrics():
    B = Bss()
    E = Ecs()
    R = Rds()
    return '\n'.join(B.get_metrics_list() + E.get_metrics_list() + R.get_metrics_list())


if __name__ == '__main__':
    app.run()
