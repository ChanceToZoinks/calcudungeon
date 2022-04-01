```
   ______      __                     __                                 
  / ____/___ _/ /______  __      ____/ /_  ______  ____ ____  ____  ____ 
 / /   / __ `/ / ___/ / / /_____/ __  / / / / __ \/ __ `/ _ \/ __ \/ __ \
/ /___/ /_/ / / /__/ /_/ /_____/ /_/ / /_/ / / / / /_/ /  __/ /_/ / / / /
\____/\__,_/_/\___/\__,_/      \__,_/\__,_/_/ /_/\__, /\___/\____/_/ /_/ 
                                                /____/                   

Play the game -> get the answers. No two games are the same!
```

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Running the game](#running-the-game)
- [How to play](#how-to-play)
  - [Example Calculation Basics (5 + 5 = 10)](#example-calculation-basics-5--5--10)
  - [Example Calculation Operator Precedence (random event)](#example-calculation-operator-precedence-random-event)
  - [Actual Example Calculation Operator Precedence (2 + 3 * 4 = 14)](#actual-example-calculation-operator-precedence-2--3--4--14)
  - [Example Backspace](#example-backspace)
  - [Example Default Zeros](#example-default-zeros)

## Running the game
```
git clone git@github.com/ChanceToZoinks/calcudungeon.git
cd calcudungeon
pip install -r requirements.txt
python3 calcudungeon.py
```

or if you dont have python installed there is Docker:
```
git clone git@github.com/ChanceToZoinks/calcudungeon.git
cd calcudungeon
docker run --rm -it $(docker build -q .)
```

or if you dont have python or Docker installed (in 2022???) there is an executable (for Windows):

See the [releases page](https://github.com/ChanceToZoinks/calcudungeon/releases/latest)

## How to play
Input commands to get objects from each room and move between them.

Moving between rooms adds a binary arithmetic operation to the queue along with the contents of the room you left. When you're ready compute give the signal to exit. 

The arithmetic operations are randomized every game, and if you REALLY want to see the possible commands just look at the tuples defined at the top of `calcudungeon.py`. Maybe I'll update that part to be a little more flexible (probably not).

### Example Calculation Basics (5 + 5 = 10)
```
   ______      __                     __                                 
  / ____/___ _/ /______  __      ____/ /_  ______  ____ ____  ____  ____ 
 / /   / __ `/ / ___/ / / /_____/ __  / / / / __ \/ __ `/ _ \/ __ \/ __ \
/ /___/ /_/ / / /__/ /_/ /_____/ /_/ / /_/ / / / / /_/ /  __/ /_/ / / / /
\____/\__,_/_/\___/\__,_/      \__,_/\__,_/_/ /_/\__, /\___/\____/_/ /_/ 
                                                /____/                   

-------------------
You find yourself in a spooky zoom meeting.
To your north is a movie theater. You think you see a - sign as well.
To your south is a dungeon. You think you see a * sign as well.
To your east is a field. You think you see a / sign as well.
To your west is a field. You think you see a + sign as well.
In front of you lies a chest full of bananas.
-------------------
What would you like to do?
> take 5 bananas
You take 5 bananas.
-------------------
What would you like to do?
> go west
You go west.
-------------------
You're now in a dark and foreboding field.
To your north is a dungeon. You think you see a - sign as well.
To your south is a Among Us game. You think you see a * sign as well.
To your east is a zoom meeting. You think you see a / sign as well.
To your west is a movie theater. You think you see a + sign as well.
You see a few diamonds.
-------------------
What would you like to do?
> take 5 diamonds
You take 5 diamonds.
-------------------
What would you like to do?
> compute
You are holding 5.0 bananas and 5.0 diamonds.
-------------------
In total that leaves you with 10.0 items!
```
And there you go! 5+5 is in fact 10!

Commands are executed as you'd expect NOT in order, but in operator precendence order. Let's see an example of that:

### Example Calculation Operator Precedence (random event)
```
   ______      __                     __                                 
  / ____/___ _/ /______  __      ____/ /_  ______  ____ ____  ____  ____ 
 / /   / __ `/ / ___/ / / /_____/ __  / / / / __ \/ __ `/ _ \/ __ \/ __ \
/ /___/ /_/ / / /__/ /_/ /_____/ /_/ / /_/ / / / / /_/ /  __/ /_/ / / / /
\____/\__,_/_/\___/\__,_/      \__,_/\__,_/_/ /_/\__, /\___/\____/_/ /_/ 
                                                /____/                   

-------------------
You enter into a well lit haunted house.
To your north is a house. You think you see a / sign as well.
To your south is a call with your product manager. You think you see a + sign as well.
To your east is a board room. You think you see a * sign as well.
To your west is a dungeon. You think you see a - sign as well.
In front of you lies a whole lot of gold dubloons.
-------------------
What would you like to do?
> yoink 2 dubloons
You yoink 2 gold dubloons.
-------------------
What would you like to do?
> go south
You go south.
Uh oh! A test failed--you have to rewrite that code! You lost half your gold dubloons.
-------------------
You're now in a bright call with your product manager.
To your north is a haunted house. You think you see a / sign as well.
To your south is a White House. You think you see a + sign as well.
To your east is a dungeon. You think you see a * sign as well.
To your west is a haunted house. You think you see a - sign as well.
In front of you lies a chest full of bananas.
-------------------
What would you like to do?
> steal 3 bananas
You steal 3 bananas.
-------------------
What would you like to do?
> walk east
You walk east.
-------------------
You enter into a boring dungeon.
To your north is a house. You think you see a / sign as well.
To your south is a Among Us game. You think you see a + sign as well.
To your east is a haunted house. You think you see a * sign as well.
To your west is a call with your product manager. You think you see a - sign as well.
You see some bananas.
-------------------
What would you like to do?
> take 4 bananas
You take 4 bananas.
-------------------
What would you like to do?
> compute
You are holding 1.0 gold dubloons and 3.0 bananas and 4.0 bananas.
-------------------
In total that leaves you with 13.0 items!
```

Wait... we got 13? What happened here? A random event is what happened! There's a 20% chance a random event occurs in every room causing you to lose 50% of a randomly chosen held item! Hope you're good at doing some quick head-math if you want to fix it on the fly. Haha, cool right? Let's try that calculation again.

### Actual Example Calculation Operator Precedence (2 + 3 * 4 = 14)
```
   ______      __                     __                                 
  / ____/___ _/ /______  __      ____/ /_  ______  ____ ____  ____  ____ 
 / /   / __ `/ / ___/ / / /_____/ __  / / / / __ \/ __ `/ _ \/ __ \/ __ \
/ /___/ /_/ / / /__/ /_/ /_____/ /_/ / /_/ / / / / /_/ /  __/ /_/ / / / /
\____/\__,_/_/\___/\__,_/      \__,_/\__,_/_/ /_/\__, /\___/\____/_/ /_/ 
                                                /____/                   

-------------------
You stumble into a spooky board room.
To your north is a ice cream parlor. You think you see a - sign as well.
To your south is a movie theater. You think you see a + sign as well.
To your east is a graveyard. You think you see a / sign as well.
To your west is a haunted house. You think you see a * sign as well.
You see a sack of apples.
-------------------
What would you like to do?
> grab 2 apples
You grab 2 apples.
-------------------
What would you like to do?
> go south
You go south.
-------------------
You enter into a musty movie theater.
To your north is a board room. You think you see a - sign as well.
To your south is a movie theater. You think you see a + sign as well.
To your east is a house. You think you see a / sign as well.
To your west is a ice cream parlor. You think you see a * sign as well.
Before you there lies a gargantuan amount of diamonds.
-------------------
What would you like to do?
> yoink 3 diamonds
You yoink 3 diamonds.
-------------------
What would you like to do?
> bag
You are holding 2.0 apples and 3.0 diamonds.
-------------------
What would you like to do?
> head west
You head west.
-------------------
You enter into a spooky ice cream parlor.
To your north is a house. You think you see a - sign as well.
To your south is a house. You think you see a + sign as well.
To your east is a movie theater. You think you see a / sign as well.
To your west is a dungeon. You think you see a * sign as well.
Before you there lies a whole lot of Obamas.
-------------------
What would you like to do?
> steal 4 obamas
You steal 4 Obamas.
-------------------
What would you like to do?
> bag
You are holding 2.0 apples and 3.0 diamonds and 4.0 Obamas.
-------------------
What would you like to do?
> compute
You are holding 2.0 apples and 3.0 diamonds and 4.0 Obamas.
-------------------
In total that leaves you with 14.0 items!
```
Ah, much better. 2 + 3 * 4 = 14 as expected. I threw in the `> bag` command as an added bonus on that one. If you ever forget what you're holding just use that or one of it many aliases, and you'll be reminded -- I'm a merciful god after all. There's also an `> inspect` command (with aliases) but I think you can figure that one out.

Oh, one last thing. If you ever backtrack you lose everything you picked up in that room the first time! Think of it as a "backspace" button. Another example coming up:
### Example Backspace
```
   ______      __                     __                                 
  / ____/___ _/ /______  __      ____/ /_  ______  ____ ____  ____  ____ 
 / /   / __ `/ / ___/ / / /_____/ __  / / / / __ \/ __ `/ _ \/ __ \/ __ \
/ /___/ /_/ / / /__/ /_/ /_____/ /_/ / /_/ / / / / /_/ /  __/ /_/ / / / /
\____/\__,_/_/\___/\__,_/      \__,_/\__,_/_/ /_/\__, /\___/\____/_/ /_/ 
                                                /____/                   

-------------------
You stumble into a dark house.
To your north is a graveyard. You think you see a + sign as well.
To your south is a dungeon. You think you see a - sign as well.
To your east is a house. You think you see a * sign as well.
To your west is a Among Us game. You think you see a / sign as well.
You see a chest full of bananas.
-------------------
What would you like to do?
> take 5 bananas
You take 5 bananas.
-------------------
What would you like to do?
> go north
You go north.
-------------------
You stumble into a dark and foreboding graveyard.
To your north is a movie theater. You think you see a + sign as well.
To your south is a house. You think you see a - sign as well.
To your east is a call with your product manager. You think you see a * sign as well.
To your west is a movie theater. You think you see a / sign as well.
You see a mountain of gold dubloons.
-------------------
What would you like to do?
> bag
You are holding 5.0 bananas and 0 gold dubloons.
-------------------
What would you like to do?
> go south
You go south.
-------------------
You stumble into a dark house.
To your north is a graveyard. You think you see a + sign as well.
To your south is a dungeon. You think you see a - sign as well.
To your east is a house. You think you see a * sign as well.
To your west is a Among Us game. You think you see a / sign as well.
You see a chest full of bananas.
-------------------
What would you like to do?
> bag
You are holding 0 bananas and 0 gold dubloons.
-------------------
What would you like to do?
> compute
You are holding 0 bananas and 0 gold dubloons.
-------------------
In total that leaves you with 0 items!
```

Also, the default number of items you pick up in a room is zero. So make sure your formula doesn't get messed up by handing a random 0 in it. Let's see a quick example to demonstrate.

### Example Default Zeros
```
   ______      __                     __                                 
  / ____/___ _/ /______  __      ____/ /_  ______  ____ ____  ____  ____ 
 / /   / __ `/ / ___/ / / /_____/ __  / / / / __ \/ __ `/ _ \/ __ \/ __ \
/ /___/ /_/ / / /__/ /_/ /_____/ /_/ / /_/ / / / / /_/ /  __/ /_/ / / / /
\____/\__,_/_/\___/\__,_/      \__,_/\__,_/_/ /_/\__, /\___/\____/_/ /_/ 
                                                /____/                   

-------------------
You're now in a bright graveyard.
To your north is a call with your product manager. You think you see a - sign as well.
To your south is a house. You think you see a / sign as well.
To your east is a field. You think you see a * sign as well.
To your west is a ice cream parlor. You think you see a + sign as well.
You see a mountain of bananas.
-------------------
What would you like to do?
> take 5 bananas
You take 5 bananas.
-------------------
What would you like to do?
> go east
You go east.
-------------------
You walk into a misty field.
To your north is a board room. You think you see a - sign as well.
To your south is a graveyard. You think you see a / sign as well.
To your east is a graveyard. You think you see a * sign as well.
To your west is a graveyard. You think you see a + sign as well.
You see a gargantuan amount of rocketships.
-------------------
What would you like to do?
> go north
You go north.
-------------------
You enter into a colorful board room.
To your north is a field. You think you see a - sign as well.
To your south is a field. You think you see a / sign as well.
To your east is a White House. You think you see a * sign as well.
To your west is a dungeon. You think you see a + sign as well.
Before you there lies a shitload of gold dubloons.
-------------------
What would you like to do?
> grab 2 dubloons
You grab 2 gold dubloons.
-------------------
What would you like to do?
> compute
You are holding 5.0 bananas and 0 rocketships and 2.0 gold dubloons.
-------------------
In total that leaves you with -2.0 items!
```
The calculation we just did is equivalent to 5 * 0 - 2 which is of course -2. So, don't forget about the default zero!

That's basically everything! I *definitely* tested this thoroughly (*wink* *wink*) so there may be a few bugs. I'm not going to fix them (unless they prevent the program from running then maybe I will), but feel free to do so yourself.
