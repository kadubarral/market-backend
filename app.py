import os

from app import blueprint
from app.main import create_app
from app.main.model import user
from dotenv import load_dotenv

load_dotenv()

app = create_app(os.getenv('APP_SETTINGS'))
app.register_blueprint(blueprint)

app.app_context().push()

if __name__ == '__main__':
    app.run()