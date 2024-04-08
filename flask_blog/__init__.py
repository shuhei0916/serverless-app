from flask import Flask

app = Flask(__name__)
app.config.from_object('flask_blog.config') # flask_blog以下にあるconfig.pyをconfigとして読み込む

from flask_blog.views import entries # ビューファイルをインポート