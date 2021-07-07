from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
<style>
h1 {
  font-family: monospace;
  color: #33b343;
}
</style>
<h1>Rock Paper Scissors</h1>
<small>see if you can beat the computer</small>

<form action="/">
<input type="submit" value="rock" name="weapon">
<input type="submit" value="paper" name="weapon">
<input type="submit" value="scissors" name="weapon">
</form>
<pre>
</pre>
"""
