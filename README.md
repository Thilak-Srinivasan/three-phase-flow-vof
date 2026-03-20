# Numerical Simulation of Three-Phase Flow

> **Research Project | BITS Pilani | Jan–May 2025**
> Under Prof. Shyam Sunder Yadav

High-resolution CFD simulation of three-phase flow (gas-liquid-solid) using Volume of Fluid (VOF) method with Adaptive Mesh Refinement (AMR). Models gas plume rise and bubble dynamics with industrial applications in oil recovery and chemical processing.

---

## Key Results

| Parameter | Value |
|-----------|-------|
| **Method** | VOF (Volume of Fluid) + AMR |
| **Solver** | Basilisk C |
| **Applications** | Oil recovery, chemical processing |
| **Validation** | Against multiphase flow literature |

---

## Repository Structure

```
three-phase-flow-vof/
├── src/
│   ├── three_phase_vof.c          # Basilisk C main simulation
│   ├── bubble_dynamics.c          # Bubble rise analysis
│   └── amr_settings.h             # Adaptive mesh refinement config
├── outputs/
│   ├── volume_fraction_t*.png     # Time-series snapshots
│   └── bubble_rise_velocity.png
├── postprocessing/
│   └── plot_results.py            # Python post-processing
└── README.md
```

---

## Numerical Methods

### Volume of Fluid (VOF)
Tracks phase interface via volume fraction field `f ∈ [0,1]`:
```
∂f/∂t + ∇·(uf) = 0
```
Interface reconstructed using PLIC (Piecewise Linear Interface Calculation).

### Adaptive Mesh Refinement (AMR)
Dynamic grid refinement near phase interfaces:
- Coarse mesh in bulk phases
- Refined mesh at gas-liquid and liquid-solid interfaces
- Reduces computational cost by ~60% vs uniform fine mesh

### Governing Equations (One-fluid formulation)
```
∇·u = 0
ρ(∂u/∂t + u·∇u) = -∇p + ∇·(μ(∇u + ∇u^T)) + ρg + σκδₛn
```

---

## Running the Simulation (Basilisk C)

```bash
# Install Basilisk
darcs get http://basilisk.fr/basilisk
cd basilisk/src && make

# Run simulation
qcc -O2 -Wall three_phase_vof.c -o three_phase_vof -lm
./three_phase_vof
```

---

**Author:** Thilak S | BITS Pilani | January–May 2025
