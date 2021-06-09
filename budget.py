from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/hasan/ButceTakibi/budget.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    butcem = Butce.query.all()
    return render_template("index.html",butcem = butcem)


@app.route("/gelirekle", methods = ["POST"])
def gelirEkle():
    adi = request.form.get("islemAdi")
    fiyat = request.form.get("islemTutari")
    newbutce = Butce(tur= "gelir", adi = adi, fiyat = fiyat)
    db.session.add(newbutce)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/giderekle", methods = ["POST"])
def giderEkle():
    adi = request.form.get("islemAdi")
    fiyat = request.form.get("islemTutari")
    fiyat = 0 - float(fiyat)
    newbutce = Butce(tur= "gider", adi = adi, fiyat = fiyat )
    db.session.add(newbutce)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/hesapla")
def hesapla():
    net = 0
    hesapla = Butce.query.all()
    for i in range(len(hesapla)):
        dene = Butce.query.order_by(Butce.fiyat).all()
        net += dene[i].fiyat
         
    net = round(net,2)
    return render_template("index.html",net = net, butcem = hesapla)

 
@app.route("/sil/<string:id>")
def islemSil(id):
    varmi = Butce.query.all()
    if(int(id) <= len(varmi)):
        silinsin = Butce.query.filter_by(id=id).first()
        db.session.delete(silinsin)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


@app.route("/hepsinisil")
def hepsiniSil():
    silinsin = Butce.query.all()
    for i in range(len(silinsin)):
        db.session.delete(silinsin[i])
        
    db.session.commit()
    return redirect(url_for("index"))


class Butce(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tur = db.Column(db.Text)
    adi = db.Column(db.Text)
    fiyat = db.Column(db.Integer)
    

app.run(debug=True)