from flask import Flask
from flask_blog.models.entries import Entry

app = Flask(__name__)
app.config.from_object('flask_blog.config')

@app.cli.command("init_db")
def create_table():
    if not Entry.exists():
        Entry.create_table(read_capacity_unit=5, write_capacity_units=2)

from flask_blog.views import entries