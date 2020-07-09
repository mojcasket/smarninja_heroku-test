from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route( "/" )
def index():
    name = "Mojca"
    current_year = "2020"
    cities = { "Vienna", "Ljublana", "Maribor"}
    return render_template ( "index.html", name=name, current_year=current_year, cities=cities )

@app.route( "/about", methods=[ "GET" ])
def about():
    return render_template( "about.html" )

@app.route( "/contact", methods=[ "POST"])
def contact():
    contact_name = request.form.get( "contact-name" )
    contact_surname = request.form.get( "contact-surname" )
    contact_message = request.form.get ( " contact_message" )

    return render_template( "success.html" )

@app.route( "/message", methods=[ "POST"])
def message():
    contact_message = request.form.get ( "contact_message" )

    return render_template( "message.html" )

@app.route( "/base" )
def base():
    return render_template( "base.html" )

@app.route( "/portfolio" )
def porfolio():
    return render_template( "portfolio.html" )

if __name__ == '__main__':
    app.run()
