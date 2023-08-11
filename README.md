# Orbital Motion

## Aim

The aim of this checkpoint is to simulate the path of the moon Phobos orbiting the planet Mars using numerical integration.

## Numerical integration

Newton’s second law $\vec{F}(t)=m\vec{a}(t)$ can be written as two first order differential equations:

$\vec{v}(t)=\dfrac{d\vec{r}(t)}{dt}$ and $\vec{a}(t)=\dfrac{d\vec{v}(t)}{dt}=\dfrac{1}{m}\vec{F}(t)$

If we know the position and velocity of a body at some initial time and the form of the force acting on it, we can use numerical integration to simulate the body’s future motion.

There are a variety of numerical integration schemes (such as the Euler and Runge Kutta methods), but we will use one of the simplest techniques known as the Euler-Cromer method.

The Euler-Cromer algorithm is:

$\vec{v}(t+Δt)=\vec{v}(t)+\vec{a}(t)Δt$ 

$\vec{r}(t+Δt)=\vec{r}(t)+\vec{v}(t+Δt)Δt$

where $t$ is the current time and $Δt$ is the small time-step.

This is a symplectic integrator, meaning that the total energy is preserved (although there are oscillations around the average value).

## Gravitational Force Law

The gravitational force law determines the acceleration of heavenly bodies and so determines the motion of the planets and their moons (as well as the sun and its planets). Consider a 2-body system consisting of the planet Mars, of mass $m_1$ located at position $\vec{r_1}(t)$, and its moon Phobos, of mass $m_2$ located at $\vec{r_2}(t)$.

The gravitational force $\vec{F_2}(t)$ exerted on Phobos by Mars by is:

$\vec{F_2}(t)=G\dfrac{m_1m_2}{|\vec{r}_{21}(t)|^2}\hat{r}_{21}(t)$

where $\vec{r}_{21}=\vec{r}_1(t)−\vec{r}_2(t)$ is the position of Phobos relative to Mars, $\hat{r}_{21}(t)$ is the unit vector from the moon to the planet and $G$ is the gravitational constant.

The acceleration $\vec{a}_2(t)$ of Phobos due this force is:

$\vec{a}_2(t)=\dfrac{\vec{F}_2(t)}{m_2}$.

Similarly, the force $\vec{F}_1(t)$ exerted on Mars by Phobos is:

$\vec{F}_1(t)=G\dfrac{m_2m_1}{∣\vec{r}_{12}(t)∣^2}\hat{r}_{12}(t)$

and the acceleration $\vec{a}_1(t)$ of Mars is:

$\vec{a}_1(t)=\dfrac{\vec{F}_1(t)}{m_1}$.
  
### Many-body problems

Systems such as the solar system, or the orbit of both of the moons of Mars (Phobos and Deimos), are examples of “many body problems”. Here, the total force $\vec{F}_j$ acting on a given body $mj$ is the sum of the gravitational forces exerted by all the other bodies in the system:

$\vec{F}_j(t)=G∑_{i≠j}\dfrac{m_im_j}{∣\vec{r}_{ij}(t)∣^2}\hat{r}_{ij}(t)$

Such systems cannot in general be solved analytically, so a numerical integration scheme must be used to calculate the path of the motion of the bodies.
 
## Checkpoint task

Write an object-oriented Python program to simulate the orbit of Phobos (one of the moons of Mars) around the planet Mars using the numerical integration scheme given above.

You should treat this as a “two body problem”, i.e. consider the force exerted by Phobos on Mars as well as the force exerted by Mars on Phobos, and update the position of both Mars and Phobos at each timestep.

A simpler approach is to treat it as a “central potential” problem, i.e. take Mars as fixed so that you only need consider the force exerted by Mars on Phobos. This is a reasonable assumption as the mass of Phobos is much smaller than that of Mars. However, this approach will only be taken as a partial solution for this checkpoint.


### Central potential or two body problem?

You will see from the checkpoint marking scheme that if you treat the checkpoint as a central potential problem, i.e. take the position of Mars to be fixed and only consider the gravitational force exerted on Phobos by Mars, it is possible to get a pass mark - although not full marks - provided that you have done well in the remainder of the checkpoint tasks.

However, this checkpoint serves as a warm-up exercise for the Solar project, which is a simulation of the orbital motion of the inner planets of the solar system. For the project you will need to treat the solar system as a many body problem and, although the project uses a different numerical integration scheme, you will find it helpful to have looked at a two body problem beforehand. This is why you are recommended to attempt the checkpoint as a two body problem.

If you wish, you can treat the checkpoint as a many body problem, so that adding another moon would not involve changing the design of your code, but this is not required as part of the checkpoint code.

###
Your code should read in the simulation parameters (including the number of time steps and the length of the time step) and details of Mars and Phobos (including the mass and orbital radius) from file.


### Initial positions and velocities: the physics

To determine the initial velocity of Phobos you can assume uniform circular motion around a stationary planet located at the origin.

The centripetal force on Phobos is the gravitational pull of Mars, directed towards the centre of Mars, so we can write Newton’s second law as

$G\dfrac{m_1m_2}{r^2_{12}}=\dfrac{m_2v^2_2}{r_{12}}$

where $m_1$ is the mass of Mars, $m_2$ the mass of Phobis, $v_2$ the speed of Phobos and $r_{12}$ its separation from Mars (i.e. its orbital radius).

Rearranging this we obtain $v_2$, the magnitude of the velocity of Phobos:

$v_2=\sqrt{\dfrac{Gm_1}{r_{12}}}$

For uniform circular motion we know that the velocity of Phobos $\vec{v}_2(t)$ is perpendicular to its orbital radius $\vec{r}_{12}(t)$, so if we set the initial position of Phobos (relative to Mars) at time $t=0$ to be:

$\vec{r}_{12}(0)=(r_{12},0)$

then its initial velocity must be

$\vec{v}_2(0)=(0,v_2)$

where $r_{12}$ is its orbital radius and $v_2$ is given by the equation above (we have also assumed rotation in an anticlockwise direction).

 

### Input parameters: Mars and Phobos

#### Mars

- mass $m_1=6.4185×10^{23}\ kg$
- initial position $\vec{r}_1=(0,0)$
- initial velocity $\vec{v}_1=(0,0)$
#### Phobos

- mass $m_2=1.06×10^{16}\ kg$
- orbital radius $r_{12}=9.3773×10^6\ m$
- initial position $\vec{r}_2=(r_{12},0)$
- initial velocity $\vec{v}_2=(0,v_2)$, where $v_2=\sqrt{\dfrac{Gm_1}{r_{12}}}$.

The orbital period of Phobos is $0.319$ days. You will need to ensure that the timestep $Δt$ is small compared to this.

###
Your code should graphically represent the motion of Phobos as it orbits around Mars, using animation to show this motion. At suitable intervals, it should print out the total kinetic energy of the system to check whether it is conserved in your simulation.

### Total kinetic energy

The total kinetic energy $K(t)$ of the system is simply the sum of the kinetic energies of Mars and Phobos:

$K(t)=\dfrac{1}{2}m_1v_1(t)^2+\dfrac{1}{2}m_2v_2(t)^2$

For a many body system this becomes:

$K(t)=∑_i\dfrac{1}{2}m_iv_i(t)^2$
 
## Code design

You will need to think very carefully about the structure of your code. There is no single correct design, but one suggestion is to use two classes; one to represent the celestial bodies (in this case, Mars and Phobos) and one for the simulation. You are, of course, free to use other designs, but whatever you choose try not to overcomplicate your code and in particular think very carefully about what each of your classes is responsible for, i.e. what data it should hold (variables) and what it should do (methods). Also think carefully about what data you need to keep, e.g. in lists or numpy arrays, in order to implement the checkpoint and don’t keep unnecessary data “just in case” - this will almost certainly result in ovecomplicated code that is hard to read and debug.