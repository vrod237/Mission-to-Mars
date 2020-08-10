from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrap2

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scrap2.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return render_template("backtoindex.html", mars=mars)

if __name__ == "__main__":
   app.run()

