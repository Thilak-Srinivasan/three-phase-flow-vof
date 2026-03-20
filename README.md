# Numerical Simulation of Three-Phase Flow

> **Research Paper | BITS Pilani | Jan–May 2025**
> Thilak S · Under Prof. Shyam Sunder Yadav
> Department of Mechanical Engineering, BITS Pilani

A numerical framework for dynamic modeling of three-phase bubble rise using the **Volume-of-Fluid (VOF)** method implemented in **Basilisk C**, with **Adaptive Mesh Refinement (AMR)** for high-resolution interface tracking at reduced computational cost.

---

## Abstract

Numerical simulation of three-phase flow presents challenges due to complex interfacial dynamics, phase interactions, and stability constraints. This work presents a framework for dynamic modeling of three-phase bubble rise using VOF in Basilisk C. The Navier-Stokes solver incorporates surface tension forces to capture capillary pressure effects, bubble deformation, interface evolution, and bubble-induced vortices. A gas plume rising as a buoyant jet through two stratified liquid layers is simulated, with analysis of velocity, plume shape evolution, and interfacial properties.

---

## Key Results

| Result | Detail |
|--------|--------|
| **Interface Evolution** | Dynamic tracking of f1, f2, f3 volume fractions over time |
| **Bubble Dynamics** | Deformation and trajectory through stratified liquid layers |
| **Surface Tension** | Vortex generation around bubbles quantified |
| **Velocity Field** | u.x and u.y components analyzed for flow pattern characterization |
| **AMR Advantage** | Higher interface resolution vs fixed-grid at comparable cost |

---

## Simulation Parameters

### Surface Tension Coefficients

| Parameter | Value (N/m) |
|-----------|-------------|
| σ₁ (Phase 1 – Phase 2) | 0.072 |
| σ₂ (Phase 2 – Phase 3) | 0.045 |
| σ₃ (Phase 1 – Phase 3) | 0.030 |

### Viscosity Values

| Parameter | Value (Pa·s) |
|-----------|--------------|
| μ₁ (Phase 1) | 0.001 |
| μ₂ (Phase 2) | 0.002 |
| μ₃ (Phase 3) | 0.003 |

### Mesh & Solver

| Parameter | Value |
|-----------|-------|
| Base mesh resolution | 64 × 64 cells |
| Maximum AMR refinement level | 10 |
| Refinement criterion | \|∇F\| > C_threshold |
| Boundary (axis) | Symmetry |
| Boundary (upper/lower) | Outflow |
| Boundary (bottom wall) | No-slip |
| Solver | Basilisk C (open-source) |
| Post-processing | ParaView |

---

## Governing Equations

### Three-Phase Continuity

Each phase $i$ satisfies:

$$\frac{\partial \alpha_i \rho_i}{\partial t} + \nabla \cdot (\alpha_i \rho_i \mathbf{u}_i) = 0$$

with the volume fraction constraint:

$$\sum_{i=1}^{n} \alpha_i = 1$$

### VOF Advection

$$\frac{\partial F}{\partial t} + \mathbf{u} \cdot \nabla F = 0$$

where $F \in [0,1]$ is the volume fraction field:
- $F = 0$: cell contains no tracked fluid
- $F = 1$: cell fully occupied by tracked fluid
- $0 < F < 1$: interface cell

### Mixture Density

$$\rho = \sum_{m=1}^{n} \alpha_m \rho_m$$

### Surface Tension (Continuum Surface Force)

$$\mathbf{F}_{st} = \sigma \kappa \mathbf{n} \delta_s, \qquad \kappa = \nabla \cdot \left( \frac{\nabla F}{|\nabla F|} \right)$$

### Momentum Equation (Navier-Stokes)

$$\frac{\partial \rho \mathbf{u}}{\partial t} + \nabla \cdot (\rho \mathbf{u}\mathbf{u}) = -\nabla p + \nabla \cdot (\mu \nabla \mathbf{u}) + \mathbf{F}_{st} + \mathbf{F}_g$$

### AMR Refinement Criterion

$$\text{Refine if} \quad |\nabla F| > C_{\text{threshold}}$$

---

## Repository Structure

```
three-phase-flow-vof/
├── src/
│   └── three_phase_vof.c          # Basilisk C simulation code
├── outputs/
│   ├── f1_surface.png             # Phase 1 interface evolution
│   ├── f1_surface_edges.png
│   ├── f1_points.png
│   ├── f2_surface.png             # Phase 2 bubble dynamics
│   ├── f2_surface_edges.png
│   ├── f2_points.png
│   ├── f3_surface.png             # Phase 3 bubble dynamics
│   ├── f3_surface_edges.png
│   ├── f3_points.png
│   ├── pressure_surface.png       # Pressure distribution & vortex
│   ├── ux_surface.png             # Velocity field u.x
│   └── uy_surface.png             # Velocity field u.y
├── paper/
│   └── Numerical_Simulation_of_Three-Phase_Flow.pdf
└── README.md
```

---

## Code Structure (Basilisk C)

The simulation is structured into four modules:

**1. Domain Setup**
Initialises the simulation domain, boundary conditions, and time-stepping loop.

**2. Material Properties**
Defines densities, viscosities, and surface tension coefficients for 3 immiscible fluids. Volume fraction variables (f1, f2, f3) track each phase.

**3. Momentum Conservation**
Three-phase momentum-conserving VOF advection scheme prevents artificial mass transfer during interface transport.

**4. Interface Reconstruction**
Geometric PLIC (Piecewise Linear Interface Calculation) reconstruction of phase boundaries from volume fraction fields.

---

## Running the Simulation

### Install Basilisk C
```bash
darcs get http://basilisk.fr/basilisk
cd basilisk/src
make
export BASILISK=$PWD
export PATH=$PATH:$BASILISK
```

### Compile and Run
```bash
cd src/
qcc -O2 -Wall three_phase_vof.c -o three_phase_vof -lm
./three_phase_vof
```

### Post-Processing (ParaView)
Load the `.vtu` output files in ParaView. Use the following representations:
- **Surface** — smooth interface visualisation
- **Surface with Edges** — displays mesh refinement structure
- **Points** — discrete phase data

Visualise: `f1`, `f2`, `f3` (volume fractions), `p` (pressure), `u.x`, `u.y` (velocity).

---

## Results Summary

### Interface Evolution (f1)
Phase 1 volume fraction tracked over time showing bubble nucleation and interface deformation consistent with theoretical buoyancy-driven flow predictions.

### Bubble Dynamics (f2, f3)
Deformation and trajectory of bubbles ascending through stratified liquid layers. Buoyancy confirmed as the dominant force in bubble rise behavior.

### Surface Tension & Vortex Generation
Pressure distribution (p) reveals vortex formation around rising bubbles. Surface tension quantified via vortex intensity, showing direct influence on mass transfer rates between phases.

### Velocity Field (u.x, u.y)
Velocity components confirm expected flow patterns: upward plume in bubble wake, recirculation zones at phase interfaces.

---

## Novel Contributions

1. **Higher Interface Resolution** — AMR achieves finer resolution at phase boundaries than fixed-grid approaches, crucial for complex interfacial dynamics without prohibitive computational cost.

2. **Robust Validation** — Results closely match theoretical models for buoyancy-driven three-phase flows.

3. **Industrial Applicability** — Framework directly applicable to oil recovery, chemical processing, and waste minimisation systems involving multiphase transport.

---

## References

1. Pozzetti & Peters, *International Journal of Multiphase Flow*, 2018.
2. Zhao et al., *arXiv:2310.12826*, 2023.
3. Bagheri et al., *The Canadian Journal of Chemical Engineering*, 2022.
4. Shen & Li, *RSC Advances*, 2023.
5. Kim & Lowengrub, *Interfaces and Free Boundaries*, 2005.

Full reference list available in `paper/Numerical_Simulation_of_Three-Phase_Flow.pdf`.

---

**Author:** Thilak S | Department of Mechanical Engineering, BITS Pilani
**Supervisor:** Dr. Shyam Sunder Yadav
**Period:** January–May 2025
**Contact:** f20220771@pilani.bits-pilani.ac.in
