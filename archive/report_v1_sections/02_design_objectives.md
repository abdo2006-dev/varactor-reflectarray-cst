## 2. Design basis and engineering objectives

### 2.1 Reference unit-cell concept

The reference element is a six-layer printed circuit board. The published
description assigns the layers as follows: the first four layers form the
reflecting structure, and the last two route bias signals to the varactor diode
[CITATION REQUIRED, Harz and Kleine-Ostmann 2022]. The precursor paper labels the
individual copper layers as patch, slot, stripline with bias-T, ground,
bias-voltage supply, and varactor diode [CITATION REQUIRED, Harz et al. 2020].

Electrically the element works in three stages. An incident plane wave excites
the top patch. The patch couples through a slot in the second copper layer into
a stripline on the third layer, which is buried between the slot layer and the
ground plane. That stripline is the resonator. It is divided by a blind via into
two sections whose published dimensions are named `Ls` and `Lv`: the short
section supplies inductive reactance, and the longer section together with the
varactor supplies the capacitive load that sets the phase range. The blind via
passes through a clearance in the ground plane and carries the RF node to the
lower layers, where the varactor sits. Changing the varactor capacitance
therefore changes the loading on the resonator, which moves the resonance and
shifts the phase of the reflected wave.

The bias network is the part of the design that makes this practical in an
array. The published design uses a bias-T consisting of a quarter-wavelength
line and a radial-stub shunt, so that the DC path can reach the diode while the
stub-plus-transformer combination presents a high impedance at the RF junction.
The source reports a maximum simulated phase shift of about 337 degrees for its
optimised element. That figure is a property of the published design. It is not
a result of this work, and no part of this report claims to have reproduced it.

### 2.2 Engineering objectives

The project set out to do the following.

Build a parametric CST model of the element in which every published dimension
appears as a named parameter, so that geometry changes are controlled rather
than manual. Establish that the model is numerically trustworthy, by checking
the periodic boundary and Floquet mode configuration, the energy balance, and
the convergence of the adaptive mesh, before drawing any conclusion from its
output. Verify that the tuning element itself behaves as intended, separately
from whether the surrounding structure responds to it. Characterise the
reflection magnitude and phase against capacitance and frequency, and build a
phase-versus-capacitance relation from that characterisation.

The last objective is the one that has not been reached. It requires a usable
phase response to characterise, and the reconstructed element does not yet
provide one. The project's active objective is therefore narrower: identify
where the reconstruction and the published design diverge, using controlled
experiments rather than untracked parameter adjustment.

A secondary objective governs how the work is recorded. Every dimension in the
model is one of three things: a value published by the source, a value inferred
from a published figure, or a value chosen by this project because the source
does not give it. The report keeps those categories separate throughout. Section
3.3 and Appendix A identify which is which.

### 2.3 Target operating region

The model is evaluated at normal incidence over a narrow band around the design
frequency.

| Quantity | Value |
|---|---|
| Reference frequency `fRef` | 26.104 GHz |
| Simulated interval | approximately 25.6 to 26.6 GHz |
| Unit cell | 7 mm by 7 mm, periodic in x and y |
| Incidence | `theta = 0`, `phi = 0` |
| Capacitance endpoints | 0.025 pF and 0.19 pF |

The simulated interval is not an arbitrary choice. It is the frequency range
over which the substrate material model is fitted, so results outside it would
be extrapolations of the dielectric definition as well as of the geometry. This
becomes relevant in Section 10, where the next planned experiment requires a
wider sweep.

Normal incidence keeps the Floquet mode set small and the computational cost low
enough for the available hardware, which is a 16 GB laptop running CST inside a
Windows virtual machine with roughly 6 to 8 GB available to the solver. Oblique
incidence is a later study and is not covered here.
