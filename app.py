from flask import Flask
import json
from utils import load_candidates
from utils import get_by_pk
from utils import get_by_skill

app = Flask(__name__)


@app.route("/")
def view_all_candidates():
    """представление для роута / (главная страница)"""
    return f"<pre>\n {load_candidates()}\n </pre>"

@app.route("/candidate/<int:pk>")
def view_candidate(pk):
    url = "https://ru-static.z-dn.net/files/d07/ef107a73dbbe27f857368894ea10f08d.jpg"
    result = f"<img src='{url}'>\n <pre>\n {get_by_pk(pk)}\n </pre>"
    return result


@app.route("/skills/<skill_name>")
def view_skills(skill_name):
    return f"<pre>\n {get_by_skill(skill_name)}\n </pre>\n"


app.run(debug = True)