<h1>TACTICAL SEA COMBAT</h1>

Tactical Sea Combat is a python game, which runs in Heroku

Users are tasked with destroying an enemy submarine without running out of
missiles. The enemy sub will take up one square on the 5 by 5 game board.

<h2>How To Play</h2>

Tactical Sea Combat is a version of the classic pen and paper and board game "Battleships".

In this version, the player is asked to enter their name to confirm their identity. They are then taken
to the "War Room" where they are given the basics rules of the game and are asked to confim they want to continue.

Upon confirming they want to play, two boards are created, a blank guess board and the computer's board which contains a single square containing a "#" symbol which is the location of the enemy submarine but isn't displayed to the user.

The player then has up to 10 guess to try and find the correct square containing the "#" and locate the enemy sub.

For every unsuccessful guess, a "x" will be added to both the guess and computer boards. This is so user knows where they have guessed and the computer can alert if a duplicate guess is made.

If the player is able to find the enemy sub within 10 turns they are deemed the winner but if they fail the enemy sub will escape and they will lose.
## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!