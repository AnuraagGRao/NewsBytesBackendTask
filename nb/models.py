#

from nb import db

class LoginData(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(40), unique = True)
    username = db.Column(db.String(20))
    hashed_password = db.Column(db.String())


class UrlData(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    hashed_url = db.Column(db.String(), unique = True)
    clicks = db.Column(db.Integer, default = 0)
    url = db.Column(db.String(), unique = True)
    utm = db.Column(db.JSON)
