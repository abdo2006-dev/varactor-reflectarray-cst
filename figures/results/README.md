# Simulated results

Reflection response of the current diagnostic geometry, exported from CST
Studio Suite 2023.

Naming follows the run identifiers in
[`../../docs/experiment_log.md`](../../docs/experiment_log.md).

| File | Content |
|---|---|
| `g04_reflection_magnitude.png` | Reflection magnitude, both capacitance endpoints, wide sweep |
| `g04_reflection_phase.png` | Reflection phase, both capacitance endpoints, wide sweep |

In both plots red is `varC = 0.19 pF` and green is `varC = 0.025 pF`.

The phase plots are CST screen output and wrap at plus or minus 180 degrees. No
tuning range in degrees may be read from them. Quantifying the tuning requires
the numerical complex S-parameter export and phase unwrapping recorded as the
next step in `../../docs/project_state.md`.
