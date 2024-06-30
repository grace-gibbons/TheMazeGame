# TheMazeGame
Welcome to The Maze Game, a project that utilizes a raspberry pi and several external components to create a playable maze navigation game!

[Insert a picture here]

## The Maze Game How to Play
The goal of the game is simple. Navigate to the end of the maze and collect coins along the way.

### The Maze
The maze is represented using the 8x8 LED matrix. Your location is signified by the red dot, which starts at the bottom left corner of the maze. The goal is to reach to the top right corner, which signifies the end of the game.

<img src="https://github.com/grace-gibbons/TheMazeGame/assets/60190711/f827ea90-2a60-4212-b3fa-3ac8eacd9618" width="640" height="320">

The left is an example of an unlit 8x8 matrix. On the right, a sample maze has been overlayed onto the matrix. This represents a sample of what the player may have to navigate through, although the matrix LED will not display any of the walls of the maze. It is up to the player to navigate the maze blindly, slowly exploring the maze and determining the possible path to the end.

Of course, the player has some information. For their current position in the maze, the LCD display will show the player to optional directions they can go: left, right, up, or down. Using just the information of their current position and optional directions, the player must successfully navigate the maze.

### Navigating the Maze
The player can use the game controller to navigate the maze, either using the arrow pad on the left or the four buttons on the right. These buttons represent the up, down, left, and right motions possible to the player.

### Coins
Scattered randomly around the maze are three coins for the player to collect. The LCD displays the number of coins the player has collected, and will alert them when they stumble across a coin in the maze, denoted by the word "Coin!". The total number of coins collected will be displayed at the end of the game as well.

<img src="https://github.com/grace-gibbons/TheMazeGame/assets/60190711/5ab40a29-16ce-49ab-ad2d-927596e31bbc" width="640" height="480">

### Winning
The player begins at the bottom left corner of the maze and must reach the top right to win the game.

The number of coins they collected, as well as the number of total moves it took them to reach the end, are displayed. For a challenge, attempt to collect as many coins in as few moves as possible.

<img src="https://github.com/grace-gibbons/TheMazeGame/assets/60190711/d5212a5a-e33d-4da7-af51-3ad0601a3210" width="640" height="480">

The game can be restarted by pressing any button or arrow pad key on the game controller.

## Project Details

### Components Used
Raspberry Pi 4 Model B
8x8 LED Matrix Module
16x2 LCD display (Mine has an i2c interface)
Breadboard
8 1kohm resistors
Several jumper wires of varying types

### Assembly
The following is the complete diagram I created, to help assemble to components. Any GPIO configuration can be used, so long as it is properly reflected in the code.

<img src="https://github.com/grace-gibbons/TheMazeGame/assets/60190711/84d38c87-c1c7-4fc2-89aa-c39916d5bdfb" width="640" height="480">

For reference, here is a chart of my connections between the Matrix Pins and the Raspberry Pi's GPIO Pins:

| Matrix Pin Number | RPi GPIO Pin Number |
| ----------------- | ------------------- |
| 1                 | 19                  |
| 2                 | 6                   |
| 3                 | 22                  |
| 4                 | 27                  |
| 5                 | 5                   |
| 6                 | 17                  |
| 7                 | 13                  |
| 8                 | 26                  |
| 9                 | 21                  |
| 10                | 25                  |
| 11                | 24                  |
| 12                | 16                  |
| 13                | 12                  |
| 14                | 20                  |
| 15                | 23                  |
| 16                | 18                  |

### 8x8 Matrix
Talk about how it works and the method I decided to use in the code

### Maze Generation
Each time the game is played, a new maze is generated utilizing Prim's algorithm, a greedy algorithm, which expands outward from a single node. My version of the algorithm is loosely defined as follows:
  Setup:
    Create some set of cells M, which represent the entire graph, or Maze
    Let C be a random starting cell
    Add that cell C to the list of explored cells E
    Initialize an empty list F, of frontier cells, or cells adjacent to explored ones, to be traversed next
  While there are cells in list F (or this is iteration one):
    Select a random cell C from the list of explored cells
    Get all the neighbors of C that are not explored or in the frontier. Add them to the frontier list
    Select a random frontier cell R
    Select a cell adjacent A to R, that is in the explored list E
    Create a connection in the maze between R and A
    Get all the neighbors of R that are not explored or in the frontier. Add them to the frontier list
    Add R to the explored list E
    Remove R from the frontier list F

This algorithm was easy for me to understand and had a relatively simple implementation, which are the main reasons why I chose it for this project. It is also a fairly quick algorithm, in comparison to some of the others I have seen for maze generation, although given the maze is small the need for speed is not necessary. Compared to an algorithm like recursive backtracking (which I also have implemented in past projects) this algorithm seems to generate shorter corridors and many more dead ends. I think these features make the maze a little more exciting to navigate, since it seems to provide an average of more directions to go in a given location, especially since the player cannot actually see the bounds of the maze.

[This](https://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap.html) source has a lot of useful information regarding different algorithms for maze generation, and I have found it to be easy to understand, while still being detailed and helpful. There are also sample mazes that can be generated on the spot, which are very helpful in viewing th subtle differences provided by different algorithms.

## Lessons Learned and Problem Solving
This project initially spawned because I've always been interested in the interactions between hardware and software, and have spent many hours messing around with the Raspberry Pi, getting simple LEDs to light up, playing with 7-segment displays, and interacting with those components via code. I wanted to do a full project involving some hardware, instead of just writing simple scripts to turn lights on and off (which is fun, and educational, but not nearly as fulfilling).

In the past, I took an interest in creating maze generators and solvers, as the algorithms to do such things are simple, yet incredibly powerful. I found by coding them myself, I was able to teach myself a lot, and found the knowledge surrounding those algorithms to be applicable in other areas. That is where I got the idea for creating a simple maze game. I knew I needed some sort of output window, and had never worked with the LCD I had laying around, so I decided that would be another fun challenge to tackle. From there, I decided it would be best to make a small game about traversing a maze, and the rest of the pieces fell into place as I went.

As expected, not everything went so smoothly.

### Putting Pieces Together
Once I had a solid idea of the finished product I had in mind, there were several tasks I needed to tackle in order to achieve my goal. These included:
  Figuring out how to properly wire the LCD
  Understanding the libraries required to display text on the LCD
  Implementing a maze generator
  Learning how to wire an 8x8 Matrix Display
  Figuring out how to handle the Matrix in the code, getting the proper cell to light up
  Keeping track of game data, like player location, moves, and coins collected
  Accepting user input

None of these are small tasks, and looking at the list was a little overwhelming to me at first, especially because much of what I was working with was entirely new to me, meaning I would have to lean from scratch. I decided to start with getting the LCD up an running, because it is integral to the project, and I was excited to see how it would work. That work wasn't as complicated as I thought it was going to be, and soon after I was able to display simple messages.

Then, I moved onto wiring the 8x8 Matrix, and trying to understand how that worked, which was a whole lot tricker. Since I only needed one cell to be lit at any given moment, I was able to read through some work that others had done, and apply it for my own needs. Many people tackle trying to write full letters to the module, but I didn't need that sort of functionality.

With the two main hardware components out of the way, I started looking into maze generation algorithms. I wanted to try a different one so I could become familiar with a new algorithm, and settled on Prim's algorithm, which seemed to suit my needs just fine. Understanding the basic algorithm, writing pseudocode, and creating my own implementation, was one of the more time consuming parts of this project. I managed to get it working, and created a print function so I could see the maze on the screen, which was incredibly useful for debugging later down the line.

With those three main components done, I decided it was time to start the official project, and string the pieces I had created together, to create something a little closer to my end goal. As I worked on that, littler details like keeping track of game data, and writing a general flow for game progression fell into place. Had I attempted to tackle this project as one big thing, instead of splitting it into little parts, I probably would have struggled a lot more than I did. It was especially helpful to be able to understand how each unit was meant to work on it's own, so when it came to debugging, I could pinpoint where potential issues were coming from, and how to fix them.

### User Input
Initially, I wanted user input to be entered using four push buttons on the breadboard, connected to the Raspberry Pi. It was simple to get them wired up, and working in the code, but I quickly came across several problems.

The first, is that the buttons I had were small, and a little difficult to press. This made actually entering input challenging, especially since the breadboard was attached via wires to the Raspberry Pi, so I couldn't just pick it up and hold it like a game controller. The second issue was that the breadboard I own is small, and with all four buttons in close quarters, I had a lot of wires surrounding them, which made getting a finger anywhere near a button was also a challenge. It was so hard for me to test, that I figured the game wasn't going to be fun to play either, so I switched my input gathering method to use a game controller instead. This method makes it far easier for the player to actually play the game, and I'm glad I had the sense to make that switch, even though it involved a bit more extra work on my part.

### Frustrating limitations
The LCD I worked with has a 16x2 display, for a total of 32 characters. That is *not* a lot of character space to work with, given the previous sentence has 71 characters! I was challenged with the task of creating a fun, playable game, that displayed enough meaningful information on the screen, without it being too difficult to read.

Initially, I thought about using scrolling text, to display more characters than the limit provided. I quickly discovered that the scrolling made words hard to read and it was difficult to find necessary information quickly. I scraped this idea, because ultimately it added too much complexity, and at it's heart, I wanted to game to be simple. Displaying the direction the player had to go and if there was a coin in the room was non-negotiable. That data *had* to be there in order for the game to be playable. I also wanted to include a counter of how many coins they collected, so they wouldn't have to keep track themselves. With that information, I found I still had room to include the player's location, which isn't needed, but it ties the screen together.

With a bigger screen, I could have done more, but I enjoyed the challenge of having a limited amount of room. I was also pleasantly surprised at the amount of information I was able to display. Who knew one could build a functioning game with nothing but 32 characters, an 8x8 matrix display, and a game controller?


  
