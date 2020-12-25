#

from nb import app
from flask import redirect, render_template, request, url_for, flash, make_response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from nb.models import *
from functools import wraps
import uuid

#

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        user = LoginData.query.filter_by(username = auth.username).first() if auth else None
        if auth and auth.username == user.username:
            result = check_password_hash(user.hashed_password, auth.password)
            if result:
                return f(*args, **kwargs)
        return make_response('Could not verify login!', 401, {'WWW-Authenticate':'Basic realm="Login Required!"'})
    return decorated

@app.route("/hshd/<uniqueurl>")
def hshd(uniqueurl):
    try:
        urlobj = UrlData.query.filter_by(hashed_url=uniqueurl).first()
        urlobj.count+=1
        db.session.commit()
        return redirect(f"{urlobj.url}")
    except Exception as err:
        return jsonify({"status":"Failure", "Error":repr(err)})


@app.route("/home", methods = ["GET", "POST"])
@login_required
def home():
    
    if request.method == "POST":
        data = request.form
        url = data.get("url")
        utmstartindex = url.find("?") + 1
        utmparams = [obj.split("=") for obj in url[utmstartindex:].split("&")]
        utmjson = {}
        for obj in utmparams:
            utmjson[obj[0]] = obj[1]
        if not UrlData.query.filter_by(url=url).first():
            hashed_url = uuid.uuid5(uuid.NAMESPACE_URL, url)
            newURL = UrlData(url = url, hashed_url = str(hashed_url))
            db.session.add(newURL)
            db.session.commit()
        else:
            flash("URL EXISTS in the database!")
            return redirect(url_for("dashboard"))
        
    else:
        urls = UrlData.query.all()
        return render_template("dashboard.html", urls = urls)


