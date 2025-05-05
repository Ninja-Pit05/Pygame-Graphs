# Pygame-Graphs
A project designed to draw graphs on pygame in an easy and fast way. A hobby project made for fun.

### How to use it

For installing use this for now:
```python
pip install https://github.com/Ninja-Pit05/Pygame-Graphs/archive/refs/tags/v0.0.1.zip
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

###  For mote info check the [wiki](https://github.com/Ninja-Pit05/Pygame-Graphs/wiki)