from dihedral import D

d6 = D(6)
d3 = D(3)

"""" Acting on the Vertices """
# Vertices are [0, n-1] for dn
assert d3.vertices() == [0, 1, 2]
assert d6.vertices() == [0, 1, 2, 3, 4, 5]
# A rotation by 240deg maps 0->2, 1->0, 2->1
assert d3.apply(d3.r[2]) == [2, 0, 1]
# A rotation by 120deg maps 0->1
assert d3.apply(d3.r[1], [0]) == [1]
# A flip through the centre switches 0<->1 and fixes 2
assert d3.apply(d3.s[0]) == [1, 0, 2]

"""" Subgroup Tests """
# d3 is a subgroup of d6
assert d6.has_subgroup(d3)
# The inverse doesn"t hold
assert not(d3.has_subgroup(d6))
# The identity (r0) is a subgroup
assert d3.has_subgroup([d3.r[0]])
# The rotations of d6 are a subgroup
assert d6.has_subgroup([r for r in d6.r])
# A single rotation with the identity is a subgroup
assert d3.has_subgroup([d3.r[0], d3.s[0]])
# Without the identity is not a subgroup
assert not(d3.has_subgroup([d3.s[0]]))

# d3"s subgroups are as we expect
assert d3.subgroups() == [["r0"], ["r0", "s0"], ["r0", "s1"], ["r0", "s2"], ["r0", "r1", "r2"], ["r0", "r1", "r2", "s0", "s1", "s2"]]

print("All tests passed!")
