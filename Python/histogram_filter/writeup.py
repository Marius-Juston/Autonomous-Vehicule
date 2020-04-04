from __future__ import division, print_function

from histogram_filter import localizer
from histogram_filter import simulate as sim

R = 'r'
G = 'g'
grid = [
    [R, G, G, G, R],
    [G, G, R, G, R],
    [G, R, G, G, G],
    [R, R, G, R, G],
    [R, G, R, G, R],
]
blur = 0.05
p_hit = 200.0
simulation = sim.Simulation(grid, blur, p_hit)
simulation.show_beliefs()

simulation.run(1)
simulation.show_beliefs()


def show_rounded_beliefs(beliefs):
    for row in beliefs:
        for belief in row:
            print("{:0.3f}".format(belief), end="  ")
        print()


show_rounded_beliefs(simulation.beliefs)


def test_sense():
    R = 'r'
    _ = 'g'

    simple_grid = [
        [_, _, _],
        [_, R, _],
        [_, _, _]
    ]

    p = 1.0 / 9
    initial_beliefs = [
        [p, p, p],
        [p, p, p],
        [p, p, p]
    ]

    observation = R

    expected_beliefs_after = [
        [1 / 11, 1 / 11, 1 / 11],
        [1 / 11, 3 / 11, 1 / 11],
        [1 / 11, 1 / 11, 1 / 11]
    ]

    p_hit = 3.0
    p_miss = 1.0
    beliefs_after_sensing = localizer.sense(
        observation, simple_grid, initial_beliefs, p_hit, p_miss)

    if helpers.close_enough(beliefs_after_sensing, expected_beliefs_after):
        print("Tests pass! Your sense function is working as expected")
        return

    elif not isinstance(beliefs_after_sensing, list):
        print("Your sense function doesn't return a list!")
        return

    elif len(beliefs_after_sensing) != len(expected_beliefs_after):
        print("Dimensionality error! Incorrect height")
        return

    elif len(beliefs_after_sensing[0]) != len(expected_beliefs_after[0]):
        print("Dimensionality Error! Incorrect width")
        return

    elif beliefs_after_sensing == initial_beliefs:
        print("Your code returns the initial beliefs.")
        return

    total_probability = 0.0
    for row in beliefs_after_sensing:
        for p in row:
            total_probability += p
    if abs(total_probability - 1.0) > 0.001:
        print("Your beliefs appear to not be normalized")
        return

    print("Something isn't quite right with your sense function")


test_sense()

from histogram_filter import simulate as sim
from histogram_filter import helpers

R = 'r'
G = 'g'
grid = [
    [R, G, G, G, R, R, R],
    [G, G, R, G, R, G, R],
    [G, R, G, G, G, G, R],
    [R, R, G, R, G, G, G],
    [R, G, R, G, R, R, R],
    [G, R, R, R, G, R, G],
    [R, R, R, G, R, G, G],
]

blur = 0.1
p_hit = 100.0
simulation = sim.Simulation(grid, blur, p_hit)

simulation.run(1)
simulation.show_beliefs()

R = 'r'
G = 'g'

grid = [
    [R, G, G, G, R, R, R],
    [G, G, R, G, R, G, R],
    [G, R, G, G, G, G, R],
    [R, R, G, R, G, G, G],
]

blur = 0.001
p_hit = 100.0
simulation = sim.Simulation(grid, blur, p_hit)

simulation.run(1)
simulation.show_beliefs()

simulation.run(1)


def test_robot_works_in_rectangle_world():
    R = 'r'
    G = 'g'

    grid = [
        [R, G, G, G, R, R, R],
        [G, G, R, G, R, G, R],
        [G, R, G, G, G, G, R],
        [R, R, G, R, G, G, G],
        [R, R, G, R, G, G, G],
        [R, R, G, R, G, G, G],
        # [R,R,G,R,G,G,G],
    ]

    blur = 0.001
    p_hit = 100.0
    for i in range(1000):
        simulation = sim.Simulation(grid, blur, p_hit)
        simulation.run(1)


test_robot_works_in_rectangle_world()
