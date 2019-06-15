# dihedral
A dihedral group D<sub>n</sub> is a mathematical group structure representing the symmetries acting on the
vertices of a regular `n`-gon. For example, D<sub>3</sub> represents the symmetries of a triangle.

This python class generates the group structure of D<sub>n</sub> for any `n`, and contains methods for generating + verifying
subgroups as well as applying transformations to the vertices.

## Class structure
Rotation actions are stored in the class variable `r` as an array `r[0], ..., r[n / 2]` where the identity is `r[0]`. 
Reflections are stored in the same way in the class variable `s`. Vertices are stores as numpy arrays in `v`, but can be accessed
in a more readable integer format using the method `vertices`.

## Acting on the vertices

Vertices and actions of the group D<sub>3</sub> are shown below as an example. The dotted lines denote reflections, and the arrow denoting R<sub>1</sub> is a 120 degree turn. R<sub>2</sub> would then be a 240 degree turn.

<img src="https://i.imgur.com/SzLzRy9.png"/>

```python
from Dihedral import Dihedral

d3 = Dihedral(3)

# List the vertices in the group
d3.vertices()
# [0, 1, 2]

# Perform a rotation of 240 degrees on the vertices
d3.apply(d3.r[2], d3.vertices())
# [2, 0, 1]
```

## Composing symmetries
Symmetries can be combined using the `compose` method.

```python
# Compose a rotation with reflection (s_2(r_1))
composed_symmetry = d3.compose([d3.s[2], d3.r[1]])

# Apply the symmetry to vertex 1
d3.apply(composed_symmetry, [1])
# [2]
```

## Finding subgroups
The method `subgroups` returns all subgroups in the dihedral group by generating all possible subsets of the group and
verifying relevant group properties (identity, closure).

```python
d3.subgroups()
# [['r0'], ['r0', 's0'], ['r0', 's1'], ['r0', 's2'], ['r0', 'r1', 'r2'], ['r0', 'r1', 'r2', 's0', 's1', 's2']]
```

Specific subsets can also be verified as being a subgroup or not using the `has_subgroup` method.

# Reducing operations

While `compose` combines operations, they can be reduced to a readable format using `reduce_operations`. For example,

```python
# Reduce r_1(s_2)
d3.reduce_operations(([d3.r[1], d3.s[2]]))
# s0
```
