from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from datetime import datetime
import os


@app.route('/')
def show_entries():
    # 仮の記事データを取得
    entries = [
        {
            'id': 1,
            'title': '初めての投稿',
            'text': 'はじめての内容',
            'created_at': datetime.now()
        }, 
        {
            'id': 2,
            'title': 'ふたつめの投稿',
            'text': 'ふたつめの内容',
            'created_at': datetime.now()
        },
    ]
    return render_template('entries/index.html', entries=entries)


@app.route('/')
def add_entry():
    # 記事の作成処理を実装
    return '新しく記事が作成されました'


@app.route('/entries/new', methods=['GET'])
def new_entry():
    print(os.listdir())
    return render_template('entries/new.html')

@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
    entry = {
        'id' :1,
        'title': '初めての投稿',
        'text': 'はじめての内容',
        'created_at': datetime.now(),
    }
    return render_template('entries/show.html', entry=entry)

@app.route('/entries/<int:id>/edit', methods=['GET'])
def edit_entry(id):
    entries = [
        {
            'id': 1,
            'title': '初めての投稿',
            'text': 'はじめての内容',
            'created_at': datetime.now()
        }, 
        {
            'id': 2,
            'title': 'ふたつめの投稿',
            'text': 'ふたつめの内容',
            'created_at': datetime.now()
        },
    ]
    entry = None
    for e in entries:
        if e['id'] == id:
            entry = e        
    return render_template('entries/edit.html', entry=entry)

@app.route('/entries/<int:id>/update', methods=['POST'])
def update_entry(id):
    # 記事の更新処理を実装
    return f'記事{id}が更新されました'

@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    # 記事の削除処理を実装
    return f'記事{id}が削除されました'