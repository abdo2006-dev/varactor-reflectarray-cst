## 1. Introduction

Reconfigurable reflectarrays steer a beam by controlling the reflection phase of
each element in a periodic surface rather than by moving the antenna. At
millimetre-wave frequencies the usual way to make an element reconfigurable is
to load a resonant structure with a varactor diode, so that a DC bias voltage
shifts the element's resonance and therefore its reflected phase. An element of
this kind has to solve two problems at once. It must present a strong,
controllable resonance to the incident field, and it must carry a DC bias to
every diode without letting the bias network disturb the RF path.

This report documents a full-wave reconstruction of one such element in CST
Studio Suite 2023. The reference design is the varactor-loaded, six-layer
reflectarray unit cell reported by Harz et al. for K-band 5G metrology near
26 GHz [CITATION REQUIRED, Harz 2020; Harz and Kleine-Ostmann 2022]. The element
couples an incident field from a top patch, through a slot, into a buried
stripline resonator, and loads that resonator with a varactor placed on the far
side of the ground plane, reached through a blind via. A bias-T built from a
quarter-wavelength line and a radial stub feeds the diode.

The work has two purposes. The first is to build a numerically defensible model
of that element from the published dimensions, so that the reflection phase can
later be characterised against capacitance and exported for array-level study.
The second, which has become the dominant activity, is to explain why the
reconstructed model does not reproduce the capacitance-dependent phase response
that the source design reports.

The current state of that investigation is straightforward to state. The model
converges. The lumped varactor is electrically active and behaves like an ideal
capacitor of the specified value. Yet moving the capacitance across its full
range from 0.025 pF to 0.19 pF changes the reflected phase near 26.104 GHz by an
amount too small to be useful. Section 6 gives the simulated behaviour, Section 8
gives the current reading of what it means, and Section 9 states what this model
cannot establish either way.

This report therefore describes a reconstruction and discrepancy analysis, not a
successful reproduction. It is written so that a reader can tell, for every
statement, whether it comes from a published source, from a converged
simulation, from a screenshot read by eye, from a modelling assumption, or from
a hypothesis that has not been tested. Section 4.6 sets out that classification
and the repository keeps a claims ledger that records the evidence behind each
statement individually.

No hardware was fabricated and no measurement was made. Every result in this
report is a simulation result.
