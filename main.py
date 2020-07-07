from flask import Flask, render_template

app = Flask(__name__)

@app.route( "/" )
def index():
    name = "Mojca"
    current_year = "2020"
    cities = { "Vienna", "Ljublana", "Maribor"}
    return render_template ( "index.html", name=name, current_year=current_year, cities=cities )

@app.route( "/about" )
def about():
    return render_template( "about.html" )

@app.route( "/base" )
def base():
    return render_template( "base.html" )

@app.route( "/portfolio" )
def porfolio():
    return render_template( "portfolio.html" )

if __name__ == '__main__':
    app.run()
