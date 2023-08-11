import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Celestial:  # celestial class to create celestial objects
    def __init__(self, info):
        self.name = info[0]
        self.mass = float(info[1])
        self.pos = np.array([float(info[2]), float(info[3])])
        self.vel = np.array([float(info[4]), float(info[5])])

    # update function to update position of celestial at each interval
    def update(self, other_body, interval):
        # direction vector between mars and phobos
        direction = other_body.pos - self.pos
        self.vel += (6.67430e-11 * other_body.mass * direction * interval) / (np.linalg.norm(direction) ** 3)  # velocity calculation for next iteration
        self.pos += self.vel * interval  # position calculation for next iteration


class Simulation:  # simulation class to create simulation object
    def __init__(self, parameters):
        # setting number of frames
        self.niter = int(parameters[0].split(";")[0])
        # setting time interval for numerical integration
        self.time_interval = int(parameters[0].split(";")[1])
        self.total_time = 0.0  # initalising elasped time
        # removing first element in parameters list (containing simulation parameters)
        parameters.pop(0)
        self.celestials = []  # creating celestials object list
        for i in range(len(parameters)):
            # appending celestials object to list with given parameters
            self.celestials.append(Celestial(parameters[i].split(";")))

    def animate(self, i):  # animation function to produce and update plot at each frame
        # updating position of mars object
        self.celestials[0].update(self.celestials[1], self.time_interval)
        # updating position of phobos object
        self.celestials[1].update(self.celestials[0], self.time_interval)
        # uodating mars position on plot
        self.patches[0].center = self.celestials[0].pos
        # updating phobos position on plot
        self.patches[1].center = self.celestials[1].pos
        self.kinetic()  # calling function to output kinetic energy
        return self.patches

    def kinetic(self):  # function to output kinetic energy
        # percentage of simulation elapsed
        percentage = self.total_time/(self.time_interval * self.niter)
        if percentage == 0.0 or percentage == 0.25 or percentage == 0.50 or percentage == 0.75 or percentage == 1.0:  # condition to output kinetic energy
            total = 0.0  # initialising total kinetic energy
            for i in range(2):
                # adding kinetic energy of each celestial object
                total += 0.5 * self.celestials[i].mass * (np.linalg.norm(self.celestials[i].vel) ** 2)
            # outputting total kinetic energy
            print("Total KE: " + str(total) + " J")
        # updating total time elapsed in simulation
        self.total_time += self.time_interval

    def run(self):  # function to set initial plot and run animation
        fig = plt.figure()
        ax = plt.axes()
        self.patches = []  # creating patches list
        self.patches.append(plt.Circle(self.celestials[0].pos, 7e5, color='r', animated=True, label="Mars"))  # creating mars patch
        self.patches.append(plt.Circle(self.celestials[1].pos, 3e5, color='orange', animated=True, label="Phobos"))  # creating phobos patch

        for i in range(2):
            ax.add_patch(self.patches[i])  # adding patches to plot
            
        ax.axis('scaled')
        ax.set_xlim(-1e7, 1e7)
        ax.set_ylim(-1e7, 1e7)
        ax.set_xlabel('X-Coordinate')
        ax.set_ylabel('Y-Coordinate')
        ax.legend()

        self.anim = FuncAnimation(fig, self.animate, frames=self.niter,repeat=False, interval=1, blit=True)  # creating animation object

        plt.show()  # showing plot


def main():  # main function to run simulation
    f = open(input("Enter Filename: ") + ".txt")
    input_parameters = []  # creating input parameters list
    for i in f:
        input_parameters.append(i)  # appending each line of input file to list
    f.close()
    sim = Simulation(input_parameters)  # creating simulation object
    sim.run()  # running simulation


main()
