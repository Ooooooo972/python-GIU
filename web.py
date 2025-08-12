from flask import Flask

# Create Flask app
app = Flask(__name__)

# Route for the homepage
@app.route("/")
def home():
    return """
    <header>
    <nav class="nav">
      <div class="head-lago">
      <h1 class="logo">My Website</h1>
      <input type="search" class="search"placeholder="Search...">
      <a href="f"><button type="submit" class="search1">Search</button></a>
      </div>
      <div class="but-24">
        <button class="but1">Allmovie </button>
      </div>
      <div class="cattgry1">
        <a href="f"><button class="but">Hindi</button></a>
        <a href="#"><button class="but">allmusic</button></a>
        <a href="#"><button class="but">allbooks</button> </a>
        <a href="#"><button class="but">allgames</button></a>
        <a href="#"><button class="but">allapps</button></a>
        <a href="#"><button class="but">allpodcasts</button></a>
        <a href="#"><button class="but">allnews</button></a>
        <a href="#"><button class="but">allvideos</button></a>
      </div>
    """

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
