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
- Linegraph
---

## import methods:

```python
from PygameGraph import Bargraph
from PygameGraph import Linegraph
```

#### code example:

```python
from PygameGraph import Bargraph
from PygameGraph import Linegraph
import pygame

pygame.init

screen = pygame.display.set_mode()


graph=Linegraph.calc((50,50),(1000,500),[7,8,9,1,2,4,8,6,5,3,1,0,8,7,6,5,4,8,12],None,None,20,amountHorLines=9)
graph1=Bargraph.calc((50,600),(1000,500),[7,8,9,1,2,4,8,6,5,3,1,0,8,7,6,5,4,8,12],None,None,20,amountHorLines=9)

print(graph)

while True:
    screen.fill("white")
    
    #Bargraph.draw(screen,graph)
    #Bargraph.move(graph,1,1)
    Linegraph.draw(screen,graph)
    Bargraph.draw(screen,graph1)
    pygame.display.flip()
```

###  For mote info check the [wiki](https://github.com/Ninja-Pit05/Pygame-Graphs/wiki)