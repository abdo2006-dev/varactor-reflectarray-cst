## 9. Limitations

This section states what the model cannot establish. It is not a list of
observed results, which are in Section 6, nor of proposed explanations, which
are in Section 8.

### 9.1 Undetermined dimensions

Five quantities in the model are project choices rather than published values.

| Quantity | Value used | Basis |
|---|---|---|
| Blind-via diameter `viaD` | 0.20 mm | chosen. Not published in the reviewed material |
| Ground-clearance diameter `viaClearD` | 0.50 mm | chosen. Not published in the reviewed material |
| Layer-5 and Layer-6 copper thickness | 0.035 mm | carried over from the upper-layer interpretation, not confirmed |
| Varactor terminal pads | 0.2155 by 0.1905 mm, 0.4185 mm separation | MACOM MAVR-011020-1411 package outline used in place of an unpublished PCB land pattern |
| Local Layer-5 to Layer-6 DC via and route | 0.20 mm diameter, negative-y trace | chosen for routing convenience |

None has been sensitivity-tested. The model therefore cannot distinguish a
result that follows from the published design from one that follows from these
choices, and no statement in this report may be read as validating any of them.

The bias-branch direction is a sixth choice, but a benign one: the +x and -x
branches are mirror images in a structure that is otherwise symmetric about that
axis, so it is a CAD convention rather than an electrical assumption.

### 9.2 Idealisations in the varactor model

The tuning element is an ideal series capacitance with zero resistance and zero
inductance. A physical varactor at 26 GHz has series resistance that sets the
element Q, package and interconnect inductance that can produce a self-resonance
within or near the band of interest, and a capacitance that follows a bias
characteristic rather than being set directly. The package body itself is also
absent from the electromagnetic problem.

The consequence runs in one direction and is worth being precise about. These
omissions would degrade a real element's performance relative to the model, so
they cannot explain a model that under-performs. They do mean that the model
cannot predict achievable phase range, insertion loss, or tuning linearity for a
physical device, and that any future phase-versus-capacitance relation derived
from it describes the ideal case only.

### 9.3 Idealisations in the electromagnetic model

Every conductor is PEC, so the model contains no ohmic loss. The near-unity
reflection magnitude reported in Section 6.1 is therefore partly a property of
the idealisation and is not comparable to a measured magnitude.

The substrate uses a single dielectric definition with a fit range of 25.6 to
26.6 GHz. Results outside that interval would extrapolate the material model as
well as the geometry, which constrains the design of the wider sweep in
Section 10.

The structure is infinitely periodic at normal incidence. Edge effects, mutual
coupling variation across a finite array, and the response at oblique incidence
are all outside what this model represents.

### 9.4 Precision of the recorded evidence

Most phase and impedance values in this report were read from CST plots rather
than exported as data. They are stated as approximate throughout and should not
be treated as publication-quality numbers.

Three specific gaps affect what can be claimed. The two adaptive-mesh delta
values for the current geometry's endpoint pair are not individually recorded,
only the statement that both meet the criterion. The additional endpoint
separation near 26.5 to 26.6 GHz has not been quantified in degrees. And the
per-variant numerical records for the slot-width and `lineV` sensitivity runs
are missing, which is why Section 6.4 quotes no values for them and why Figure 7
cannot yet be produced.

Building the phase-versus-capacitance relation the project needs will require
exported S-parameter data rather than screenshots, and that export has not been
set up.

### 9.5 Scope of the sensitivity study

The geometry study in Section 6.4 tested one value of each of three parameters,
applied cumulatively, with changes small relative to the dimensions themselves.
It establishes that those three points do not tune. It does not bound the
parameter space, does not isolate the effect of any single dimension, and cannot
show that the resonator dimensions are irrelevant to the problem.

### 9.6 Frequency coverage

No simulation has been run outside approximately 25.6 to 26.6 GHz. The model
therefore cannot say whether a capacitance-dependent resonance exists above
26.6 GHz. The hypothesis in Section 8.3 is a reading of behaviour at the edge of
the simulated window, and the window itself is the limitation.

### 9.7 No hardware

Nothing in this project was fabricated or measured. Every result is a simulation
result, and no statement here can be read as an experimental confirmation of
either the reconstructed model or the published design.
