# main.py - Intramurals Players List
# Uses loops to display and generate the list of players

import random

# ANSI color codes for pink terminal styling
PINK       = "\033[38;5;213m"
HOT_PINK   = "\033[38;5;198m"
LIGHT_PINK = "\033[38;5;218m"
WHITE      = "\033[97m"
RESET      = "\033[0m"
BOLD       = "\033[1m"

# List of players stored in an array
players = [
    "Reyes", "Santos", "Cruz", "Bautista", "Ocampo",
    "Garcia", "Torres", "Flores", "Aquino", "Navarro",
    "Mendoza", "Ramos", "Castillo", "Dela Cruz", "Lim",
    "Soriano", "Aguilar", "Dizon", "Salazar", "Vergara", "Tan"
]

# Shuffle the list so the order is randomized every run
random.shuffle(players)

# Function to print a decorative border
def print_border():
    print(HOT_PINK + "  " + ("*~" * 22) + RESET)

# Function to display the players list in the terminal
def display_players():
    print()
    print_border()
    print(HOT_PINK + BOLD + "        Intramurals SY 2025-2026 - Players List" + RESET)
    print_border()
    print()

    # For loop to go through each player in the list
    for i in range(len(players)):
        number = i + 1

        # Alternate colors between pink shades
        if number % 2 == 0:
            color = LIGHT_PINK
        else:
            color = PINK

        print(color + f"    {number:>2}.  {players[i]}" + RESET)

    print()
    print_border()
    print(LIGHT_PINK + f"        Total Players: {len(players)}" + RESET)
    print_border()
    print()

# Function to generate the players.html file
def generate_html():
    # Build the player list rows using a loop
    rows = ""
    for i in range(len(players)):
        number = i + 1
        rows = rows + f"        <tr><td>{number}</td><td>{players[i]}</td></tr>\n"

    # Full HTML content
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Players - Intramurals</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    body {{
      font-family: Georgia, serif;
      background: #fff0f5;
      min-height: 100vh;
    }}

    nav {{
      background: #d63384;
      padding: 14px 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    nav span {{
      color: #fff;
      font-size: 14px;
      letter-spacing: 1px;
    }}

    nav a {{
      color: #fff;
      text-decoration: none;
      margin-left: 16px;
      font-size: 13px;
      padding: 6px 14px;
      border: 1px solid #fff;
      border-radius: 3px;
    }}

    nav a:hover, nav a.active {{
      background: #fff;
      color: #d63384;
    }}

    .page {{
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: calc(100vh - 50px);
      padding: 40px 20px;
    }}

    .card {{
      background: white;
      border: 1px solid #f5b8d0;
      padding: 40px;
      width: 100%;
      max-width: 420px;
      box-shadow: 4px 4px 0px #d63384;
      text-align: center;
    }}

    h2 {{
      font-size: 22px;
      color: #d63384;
      margin-bottom: 20px;
      border-bottom: 2px solid #f5b8d0;
      padding-bottom: 10px;
      letter-spacing: 1px;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 14px;
    }}

    th {{
      background: #d63384;
      color: white;
      padding: 8px 12px;
      font-weight: normal;
      letter-spacing: 1px;
    }}

    td {{
      padding: 7px 12px;
      border-bottom: 1px solid #fce4ec;
      color: #444;
    }}

    tr:nth-child(even) td {{
      background: #fff0f5;
    }}

    .total {{
      margin-top: 16px;
      font-size: 13px;
      color: #d63384;
      letter-spacing: 1px;
    }}
  </style>
</head>
<body>

  <nav>
    <span>Intramurals SY 2025-2026</span>
    <div>
      <a href="index.html">Sign Up</a>
      <a href="teamchecker.html">Team Checker</a>
      <a href="players.html" class="active">Players</a>
    </div>
  </nav>

  <div class="page">
    <div class="card">
      <h2>Intramurals Players</h2>

      <table>
        <tr>
          <th>#</th>
          <th>Last Name</th>
        </tr>
{rows}      </table>

      <p class="total">Total Players: {len(players)}</p>
    </div>
  </div>

</body>
</html>"""

    # Write the HTML to a file
    file = open("players.html", "w")
    file.write(html)
    file.close()

    print(PINK + "  players.html has been generated successfully." + RESET)
    print()

# Run both functions
display_players()
generate_html()