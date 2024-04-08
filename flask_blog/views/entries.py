from flask_blog import app

@app.route('/')
def show_entities():
    return "全ての記事を表示"

# @app.route('URL')の形でURLを記載
# HTTPメソッドはmethodsの中に指定。
# データの取得に係るものはGET、更新にかかわるものはPOST
@app.route('/entries', methods=['POST'])
def add_entry():
    return '新しく記事が作成されました'

@app.route('/entries/new', methods=['GET'])
def new_entry():
    return '記事の入力フォームを表示'

@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
    return f'記事{id}を表示'

# URL中に<int:id>と書くことで、該当の個所を変数として扱うことが出来る。
@app.route('/entries/<int:id>/edit', methods=['GET'])
def edit_entry(id):
    return f'記事{id}の編集フォームを表示'

@app.route('/entries/<int:id>/update', methods=['POST'])
def update_entry(id):
    return f'記事{id}が更新されました'

@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    return f'記事{id}が削除されました'