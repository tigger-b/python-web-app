from flask import Flask
from flask import request
import random

app = Flask(__name__)

@app.route("/")
def index():
    weapon = request.args.get("weapon")
    if weapon is None:
        weapon = ""
    computer = random.randint(1,3)
    if computer == 1:
        computer = 'rock'
    elif computer == 2:
        computer = 'paper'
    else:
        computer = 'scissors'

    if weapon == computer:
        result ='tie,you both select same'
    elif weapon == 'rock' and computer == 'paper':
        result ='you loose, computer selected paper'
    elif weapon == 'rock' and computer == 'scissors':
        result ='you win, computer selected scissors'
    elif weapon == 'paper' and computer == 'scissors':
        result ='you loose, computer selected scissors'
    elif weapon == 'paper' and computer == 'rock':
        result ='you win, computer selected rock'
    elif weapon == 'scissors' and computer == 'rock':
        result ='you loose,computer selected rock'
    elif weapon == 'scissors' and computer == 'paper':
        result ='you win, computer selected paper'
    else:
        result ='invalid: choose any one -- rock, paper, scissors'
    


    
    return """

 <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto+Slab&display=swap" rel="stylesheet">


    
 <!-- Add your site or application content here -->
  <style>
    body {
      font-family: 'Roboto Slab', serif;
      max-width: 1000px;
      padding-top: 50px;
      padding-bottom: 50px;
      margin: auto;
    }
    h1 {
      
      color: #33b343;
      display: flex;
      justify-content: center;
      font-size: 70px;
    }
    p {
      
      display: flex;
      justify-content: center;
      font-size: 20px;
      margin: 50px;
    
    }

   
    .weapon {
      position: relative;

    }
    .weapon svg {
      position: absolute;
      left: 0;
      top: 0;
    
    }
    .weapon input {
      width: 200px;
      height: 200px;
      border: none;
      background-color: transparent;
      color: transparent;
    }
    
    input{
      z-index:99;
      position: relative;
      
    
    }

    .choice{
      color: red;
      font-size: 1.5rem;
    }
    .flex-row {
      display: flex;
      justify-content: space-between;
    }
    </style>
    <h1>Rock Paper Scissors.</h1>
    <p>see if you can beat the computer</p>
    
    
    
    
  <form action="/">
    <div class="flex-row">
        <div class="weapon">
          <input type="submit" value="rock" name="weapon">
          <svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="hand-rock" class="svg-inline--fa fa-hand-rock fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M408.864 79.052c-22.401-33.898-66.108-42.273-98.813-23.588-29.474-31.469-79.145-31.093-108.334-.022-47.16-27.02-108.71 5.055-110.671 60.806C44.846 105.407 0 140.001 0 187.429v56.953c0 32.741 14.28 63.954 39.18 85.634l97.71 85.081c4.252 3.702 3.11 5.573 3.11 32.903 0 17.673 14.327 32 32 32h252c17.673 0 32-14.327 32-32 0-23.513-1.015-30.745 3.982-42.37l42.835-99.656c6.094-14.177 9.183-29.172 9.183-44.568V146.963c0-52.839-54.314-88.662-103.136-67.911zM464 261.406a64.505 64.505 0 0 1-5.282 25.613l-42.835 99.655c-5.23 12.171-7.883 25.04-7.883 38.25V432H188v-10.286c0-16.37-7.14-31.977-19.59-42.817l-97.71-85.08C56.274 281.255 48 263.236 48 244.381v-56.953c0-33.208 52-33.537 52 .677v41.228a16 16 0 0 0 5.493 12.067l7 6.095A16 16 0 0 0 139 235.429V118.857c0-33.097 52-33.725 52 .677v26.751c0 8.836 7.164 16 16 16h7c8.836 0 16-7.164 16-16v-41.143c0-33.134 52-33.675 52 .677v40.466c0 8.836 7.163 16 16 16h7c8.837 0 16-7.164 16-16v-27.429c0-33.03 52-33.78 52 .677v26.751c0 8.836 7.163 16 16 16h7c8.837 0 16-7.164 16-16 0-33.146 52-33.613 52 .677v114.445z"></path></svg>
        </div>
        <div class="weapon">
            <input type="submit" value="paper" name="weapon">
            <svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="hand-paper" class="svg-inline--fa fa-hand-paper fa-w-14" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M372.57 112.641v-10.825c0-43.612-40.52-76.691-83.039-65.546-25.629-49.5-94.09-47.45-117.982.747C130.269 26.456 89.144 57.945 89.144 102v126.13c-19.953-7.427-43.308-5.068-62.083 8.871-29.355 21.796-35.794 63.333-14.55 93.153L132.48 498.569a32 32 0 0 0 26.062 13.432h222.897c14.904 0 27.835-10.289 31.182-24.813l30.184-130.958A203.637 203.637 0 0 0 448 310.564V179c0-40.62-35.523-71.992-75.43-66.359zm27.427 197.922c0 11.731-1.334 23.469-3.965 34.886L368.707 464h-201.92L51.591 302.303c-14.439-20.27 15.023-42.776 29.394-22.605l27.128 38.079c8.995 12.626 29.031 6.287 29.031-9.283V102c0-25.645 36.571-24.81 36.571.691V256c0 8.837 7.163 16 16 16h6.856c8.837 0 16-7.163 16-16V67c0-25.663 36.571-24.81 36.571.691V256c0 8.837 7.163 16 16 16h6.856c8.837 0 16-7.163 16-16V101.125c0-25.672 36.57-24.81 36.57.691V256c0 8.837 7.163 16 16 16h6.857c8.837 0 16-7.163 16-16v-76.309c0-26.242 36.57-25.64 36.57-.691v131.563z"></path></svg>
        </div>
        <div class="weapon">
          <input type="submit" value="scissors" name="weapon">
          <svg data-icon="hand-scissors" class="svg-inline--fa fa-hand-scissors fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M256 480l70-.013c5.114 0 10.231-.583 15.203-1.729l118.999-27.427C490.56 443.835 512 417.02 512 386.277V180.575c0-23.845-13.03-45.951-34.005-57.69l-97.999-54.853c-34.409-19.261-67.263-5.824-92.218 24.733L142.85 37.008c-37.887-14.579-80.612 3.727-95.642 41.201-15.098 37.642 3.635 80.37 41.942 95.112L168 192l-94-9.141c-40.804 0-74 32.811-74 73.14 0 40.33 33.196 73.141 74 73.141h87.635c-3.675 26.245 8.692 51.297 30.341 65.006C178.657 436.737 211.044 480 256 480zm0-48.013c-25.16 0-25.12-36.567 0-36.567 8.837 0 16-7.163 16-16v-6.856c0-8.837-7.163-16-16-16h-28c-25.159 0-25.122-36.567 0-36.567h28c8.837 0 16-7.163 16-16v-6.856c0-8.837-7.163-16-16-16H74c-34.43 0-34.375-50.281 0-50.281h182c8.837 0 16-7.163 16-16v-11.632a16 16 0 0 0-10.254-14.933L106.389 128.51c-31.552-12.14-13.432-59.283 19.222-46.717l166.549 64.091a16.001 16.001 0 0 0 18.139-4.812l21.764-26.647c5.82-7.127 16.348-9.064 24.488-4.508l98 54.854c5.828 3.263 9.449 9.318 9.449 15.805v205.701c0 8.491-5.994 15.804-14.576 17.782l-119.001 27.427a19.743 19.743 0 0 1-4.423.502h-70z"></path></svg>
        </div>
    </div>
</form>
    
    <p>You decided to play</p>
    <p class="choice">""" + weapon + """</p>
    <p> computer decided to play </p>
    <p class="choice">""" + computer + """</p>
    <p class="result">""" + result + """</p>"""


