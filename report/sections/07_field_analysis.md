## 7. Field and surface-current diagnostics

S-parameters describe what leaves the structure. They do not say where the
energy went inside it. When an element converges, contains an electrically valid
tuning component, and still fails to tune, the next useful question is whether
the incident field is reaching the resonant path at all. Field monitors answer
that question directly.

### 7.1 Method

Two monitors were defined at the reference frequency of 26.104 GHz on the field
audit branch: electric field magnitude and surface current density. The geometry
was not modified for the audit, and the run used the same solver configuration
as the endpoint tests.

Reading these plots requires care with the colour scale, and the audit produced
one clear example of why. The electric-field plot saturates to a single colour
when the scale maximum is set far below the maximum in the data. A saturated
plot shows the scale, not the field, and no physical conclusion can be drawn
from it. The E-field capture from this run is unusable for that reason and is
excluded from the report until it is regenerated on a fixed non-saturating
range.

### 7.2 Surface-current distribution at 26.104 GHz

The surface-current result at `varC = 0.025 pF` is usable and gives the most
specific diagnostic evidence the project currently has.

CST reports the surface-current magnitude maximum as approximately 392.368 A/m,
located near `(x, y, z) = (1.138, -0.130, -0.254) mm`. The z coordinate places
that maximum at the Layer-2 top level, which is the slot layer.

On the default scale, the resonant path is invisible: everything except the
region around the maximum renders at the bottom of the range. Rescaling the plot
manually to a fixed 0 to 5 A/m range brings out a visible gradient along the
Layer-3 stripline and the lower routing. The rescaling is what makes the reading
quantitative rather than impressionistic. It shows that the current on the
resonant path is of the order of a few A/m while the global maximum is several
hundred A/m, a difference of roughly two orders of magnitude.

*[Figure 8 placeholder: surface-current magnitude at 26.104 GHz on a fixed
0 to 5 A/m scale. Field-audit branch, `varC = 0.025 pF`. Caption must state the
global maximum of approximately 392.368 A/m and its position at the Layer-2
level, so that the fixed scale is not mistaken for the full range of the data.]*

### 7.3 What the distribution does and does not establish

The confirmed observation is narrow: at 26.104 GHz and at the low-capacitance
endpoint, the surface current is concentrated at the slot layer, and the
Layer-3 resonant path carries current roughly two orders of magnitude smaller.

That is consistent with weak coupling from the patch and slot into the buried
stripline, which would explain the whole picture: an incident field that mostly
reflects off the upper structure, a resonator that is only lightly excited, and
a varactor that is electrically active on a branch with little influence over
the total reflected field.

It does not establish that explanation, for two reasons. A resonator can carry
modest current relative to a driven aperture and still dominate the reflected
phase, so a two-order-of-magnitude ratio is suggestive rather than decisive.
And the observation exists at one capacitance state only. The comparison that
would carry weight is between the two endpoints on identical geometry: if the
resonant-path current is essentially the same at 0.025 pF and 0.19 pF, the
varactor is not materially loading the excited resonator, and coupling becomes
the leading explanation. If the resonant-path current changes substantially
between the states while the reflected phase does not, the problem lies
somewhere between the resonator and the far field rather than in the coupling.

That comparison has not been run. Section 10 specifies it.
