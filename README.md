# Pygame-Graphs
A project designed to draw graphs on pygame in an easy and fast way. A hobby project made for fun.

### How to use it

For installing use this for now:
```python
pip install https://github.com/Ninja-Pit05/Pygame-Graphs/archive/refs/tags/v0.0.11.zip
```

To import it, use:
```python
import PygameGraphs
```
Or select a specific graph type to work with using:
```python
from PygameGraphs import "Graph Name"
```

So far, the graphs available are:
- Bargraph

---

## Bargraph
Displays data with bars.

import method:
```python
from PygameGraph import Bargraph
```

The Bargraph class comes with three functions:

> calc

Calculates the graphs contents position.

> draw

Draws the graph.

> move

Easly changes graph coordinates.


### calc

calc comes with the following arguments:
```python
calc(
    cords,
    size,
    verticalValue,
    verticalOverlayFunction=None,
    horizontalDisplay=None,
    fontSize=20,
    border=20,
    horPointy=10,
    verPointy=10,
    formatSeconds=False,
    amountHorLines=9
)
```

***cords*** - Coordinates of the position of the graph on the screen. Either a tuple (x,y) or a list [x,y].

***size*** - Width and Height of the graph. Either a tuple (w,h) or a list [x,y].

***verticalValue*** - Numeric value of each piece of data. Is also the internal value used to calculates each bar height, width, etc. For said reason, if your data is formatted, for instance, 30:23:12:0.34, it should be tranlated to an int value, let's say, seconds or hours.

***verticalOverlayFunction*** - Receives a function used to format the numerical data. Let's say, turning the 360 seconds internally, into """"""

***fontSize*** - The font size for labels. Either an integer or a tuple/list of two integers. If an integer is passed, both, vertical and horizontal labels, will have the passed value. If a tuple/list of two integers are passed, the first value will be the vertical label font size and the second value the horizontal label font size.

***border*** - The border of the graph, centering it's content.

***horPointy*** - The continuation of the horizontal lines before y 0.

***verPointy*** - The continuation of the horizontal lines before x 0.

***formatSeconds*** - (Discontinued, will disappear soon)

***amountHorLines*** - Amount of vertical division lines on the y coordinate.

#### code example:

```python
import pygame
from PygameGraph import Bargraph

pygame.init()
screen=pygame.display.set_mode((1200,700))


data=[1,2,7,4,1,3,12]
graph=Bargraph.calc((100,100),(1000,500),data)

while True:
    screen.fill('white')

    Bargraph.draw(screen,graph)

    pygame.display.flip()
```
---

### draw
Draws the graph to specified pygame.dislay pbject.

```python
draw(
    screen,
    dic,
    outline=5,
    style=0
)
```

***screen*** - Pygame.font object to draw graph on.

***dic*** - Python dictionary object which received the Bargraph.calc result.

***outline*** - Graph outline thickness

***style*** - (Discontinued, being deleted soon) Hide/show labels.

---

### move
Moves the graph coordinates given an value in pixels for both axis.

```python
move(
    dic,
    x,
    y
)
```

***dic*** - Python dictionary object which received the Bargraph.calc result.
***x*** - Number in pixels to move in the x axis.
***y*** - Number in pixels to move in the y axis.