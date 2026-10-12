# Raychaudhuri equation: collapse of gas clouds and neutron stars

Theory and numerics of gravitational collapse via the Raychaudhuri equation

θ̇ = −θ²/3 − σ² + ω² − R_ab uᵃuᵇ + ∇ₐaᵃ

with a causal, neutron-star-like equation of state. Includes the acceleration-divergence (pressure-support) term, a derived parameter-free closure for it, a TOV comparison, and a Misner–Sharp GR code with adaptive mesh refinement.

## Contents

| Folder | What |
|---|---|
| `figures/derived_closure/` | **Current results** (derived closure `support = ρ/(1 − (2/3)ρR²)`, Buchdahl-capped) |
| `figures/old_closure/` | Earlier results with a cruder (k = 6) closure — **superseded**, kept for history |
| `figures/eos_and_gr/` | Realistic EoS (SLy crust + piecewise polytrope + causal cap), closure comparison, GR AMR collapse |
| `report/` | Summary report (HTML/PDF). **Describes the old closure; superseded** by `figures/derived_closure/` |
| `code/core_model.py` | Minimal reduced-ODE model (see note below) |

### Derived-closure figures
- `final_phase_diagram.png` — definitive outcome map in (M0, |θ0|), τmax up to 1800
- `careful_phase_diagram.png` — earlier τmax = 150 version
- `new_stability_diagram.png` — earlier 2D scan
- `new_phase_portraits.png`, `new_thetadot_vs_theta.png`, `new_theta_vs_tau.png`
- `new_terms_decomposition.png`, `new_gravity_support_vs_rho.png`
- `subcritical_supercritical.png`, `critical_scaling.png`, `critical_gravity_support_vs_rho.png`

## Model
Reduced 3-variable system (θ, ρ, R), 4πG = 1: θ̇ = −θ²/3 − (ρ+3p) + support, ρ̇ = −θ(ρ+p), Ṙ = θR/3. Inputs are (ρ0, R0, θ0) plus the EoS. Outcomes: stable, collapse, disperses, undetermined.

## Caveats
- **Original scripts are not included.** The analysis scripts that generated the figures were lost when the working session was reset; only the figures and report survived. `code/core_model.py` is a short reconstruction from notes (toy EoS, Euler stepping) and is not guaranteed to reproduce the figures exactly.
- The reduced-ODE and GR codes use the toy sigmoid EoS p = ρx/(1+x), x = (ρ/ρc)⁴, ρc = 0.8. The realistic EoS is validated only in the TOV solve.
- The closure is exact only for a uniform-density ansatz.
- Fixed-step Euler gives a numerical floor in the critical-scaling plateau.
- In the final phase diagram 165 of 11,050 cells remain undetermined (mainly M0 → 0).
- The GR AMR code agrees with the reduced ODE to ~15–20% (first order).
