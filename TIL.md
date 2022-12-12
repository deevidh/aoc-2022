# Things I learned

This is primarily a reference for myself to try and help me to retain some of things I learn. I'm sure it will be useful to read through it when tackling next year's AOC!

----

## Day 5

### Unpacking args

When supplying a list (and presumably other iterables) as an argument to a function, we can prefix the list with `*` to unpack it into separate arguments. For example, I wanted to pass multiple strings to the zip function so that the strings would be zipped together. This required each string to be passed as a separate argument. However my multiple strings were in a list.

By passing a list of the strings directly, I didn't get the result I wanted:

```python
>>> list(zip(['abcdef','123456']))
[('abcdef',), ('123456',)]
```

However it worked when I unpacked the list into arguments:

```python
>>> list(zip(*['abcdef','123456']))
[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('e', '5'), ('f', '6')]
```

### FIXME: List slicing

```python
row[1::4]
```

----

## Day 8

### FIXME: Enumerators? Numpy arrays?

----

## Day 12

### Global Variables

At some point in my initial solution, I used a global variable. If I've used these in Python before, then I've forgotten about them. As a refresher: you can access global variables within functions, but if you want to write to them you must declare them within your function with something like `global varname`. Eventually I removed the global variables from my solution.

### Pathfinding Algorithms (BFS, Dijkstra's, A*)

When tackling this puzzle, I simply reasoned out the best way to tackle the problem and came up with a satisfactory algorithm. I started with the "E" node, and worked back to the "S" node. The algorithm evaluates the node(s) at the present depth to discover valid neighbours, which are then added to a set of nodes to visit in the next depth level. We then move on to the next depth level and iterate through the nodes in this set. Nodes which have been visited are tracked so that they are not revisited (these nodes are never relevant to re-visit at a later depth, as a shorter route would have found when they were visited at a lower depth). If the target node is found, then the path is complete and the algorithm is finished. Afterwards I did some reading, and found that I have implemented is called a **Breadth-First Search (BFS)**. This means that it evaluates all options at a certain depth before continuing - compare/contrast this with a **Depth-First Search (DFS)**.

I read that another possible algorithm is **Dijkstra's Algorithm**, which uses a prioritised queue instead of simply iterating through all of the unvisited nodes. However it seems that in this case of this puzzle, Dijkstra's algorithm isn't a useful improvement as the distance between each node is always 1, so there is no useful prioritization of the queue.

It has also been suggested that prioritizing the queue of unvisited nodes using some other heuristic such as the Manhattan distance to the target could yield an improvement. I believe this is known as the **A\* algorithm** (but I'm a little fuzzy on the details). If I understand correctly then using an A\* algorithm with no heuristic will essentially just do the same as a BFS. This is one to research in future, it could be very useful to have an A* algorithm in my toolbox.
