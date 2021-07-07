from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    weapon = request.args.get("weapon")
    if weapon is None:
        weapon = ""
    return """
<style>
h1 {
  font-family: monospace;
  color: #33b343;
}
.choice {
  font-family: monospace;
}
</style>
<h1>Rock Paper Scissors</h1>
<small>see if you can beat the computer</small>

<form action="/">
<input type="submit" value="rock" name="weapon">
<input type="submit" value="paper" name="weapon">
<input type="submit" value="scissors" name="weapon">
</form>

You decided to play
<span class="choice">""" + weapon + """</span>"""
