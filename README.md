# Numerical Simulation of Three-Phase Flow

> **Research Paper | BITS Pilani | Jan–May 2025**
> Thilak S · Under Prof. Shyam Sunder Yadav
> Department of Mechanical Engineering, BITS Pilani
> `f20220771@pilani.bits-pilani.ac.in`

A numerical framework for dynamic modeling of three-phase bubble rise using the **Volume-of-Fluid (VOF)** method implemented in **Basilisk C**, with **Adaptive Mesh Refinement (AMR)** for high-resolution interface tracking at reduced computational cost.

---

## Abstract

Numerical simulation of three-phase flow presents challenges due to complex interfacial dynamics, phase interactions, and stability constraints. This work presents a framework for dynamic modeling of three-phase bubble rise using VOF in Basilisk C. Utilizing AMR, the simulation combines precise interface resolution with high computational efficiency. The Navier-Stokes solver incorporates surface tension forces to capture capillary pressure effects, bubble deformation, interface evolution, and bubble-induced vortices. The simulation produces a gas plume that rises as a buoyant jet through two stratified liquid layers, analyzing velocity, plume shape evolution, and interfacial properties.

**Index Terms:** Three-phase flow, Volume-of-Fluid (VOF), Basilisk C, Adaptive Mesh Refinement (AMR), Navier-Stokes equations, surface tension, bubble dynamics, CFD

---

## Motivation

Gas, liquid, and solid three-phase interactions play a critical role in chemical processing, oil recovery, and environmental fluid mechanics. These systems exhibit complex interfacial dynamics — bubble-particle collisions, phase separation, and interfacial instabilities — which directly affect process efficiency and stability.

**Why existing methods fall short:**
- **Level-set methods** — limited in handling triple-phase contact lines and large density ratios
- **Discrete Element Modeling (DEM)** — struggles with realistic interface evolution and correct interfacial tension parameters
- **Fixed-grid approaches** — cannot adaptively resolve sharp gradients at interfaces without prohibitive computational cost

This work addresses these challenges by combining VOF with AMR in Basilisk C, enabling dynamic mesh refinement precisely at phase boundaries and triple contact lines.

---

## Key Results

| Result | Detail |
|--------|--------|
| **Interface Evolution** | Dynamic tracking of f1, f2, f3 volume fractions over time |
| **Bubble Dynamics** | Deformation and trajectory through stratified liquid layers confirmed buoyancy-dominant behavior |
| **Surface Tension** | Vortex generation around bubbles quantified via pressure distribution |
| **Velocity Field** | u.x and u.y confirm upward plume and recirculation zones at interfaces |
| **AMR Advantage** | Higher interface resolution vs fixed-grid at comparable computational cost |

---

## Simulation Parameters

### Surface Tension Coefficients

| Parameter | Value (N/m) |
|-----------|-------------|
| σ₁ (Phase 1 – Phase 2) | 0.072 |
| σ₂ (Phase 2 – Phase 3) | 0.045 |
| σ₃ (Phase 1 – Phase 3) | 0.030 |

### Dynamic Viscosity Values

| Parameter | Value (Pa·s) |
|-----------|--------------|
| μ₁ (Phase 1) | 0.001 |
| μ₂ (Phase 2) | 0.002 |
| μ₃ (Phase 3) | 0.003 |

### Mesh & Solver Configuration

| Parameter | Value |
|-----------|-------|
| Base mesh resolution | 64 × 64 cells |
| Maximum AMR refinement level | 10 |
| Refinement criterion | \|∇F\| > C_threshold |
| Boundary — axis | Symmetry (cylindrical geometry) |
| Boundary — upper/lower | Outflow |
| Boundary — bottom wall | No-slip |
| Solver | Basilisk C (open-source CFD toolbox) |
| Post-processing | ParaView |
| OS | Ubuntu |

---

## Theoretical Background

### Three-Phase Flow Concepts

**1. Wettability Order**
The wettability order governs the relative arrangement of phases in porous media. It controls the range of pore sizes occupied by each fluid phase, which in turn determines flow conductance and trapping processes.

**2. Flow Patterns**
Three-phase flow can exhibit several configurations depending on how the liquid phases are distributed:
- **Stratified flow** — phases separated by gravity into distinct horizontal layers
- **Slug flow** — alternating plugs of gas and liquid
- **Annular flow** — gas core surrounded by liquid film on walls

---

## Governing Equations

### Three-Phase Continuity

Each phase $i$ satisfies mass conservation:

$$\frac{\partial \alpha_i \rho_i}{\partial t} + \nabla \cdot (\alpha_i \rho_i \mathbf{u}_i) = 0$$

with the volume fraction constraint ensuring the domain is fully occupied at all times:

$$\sum_{i=1}^{n} \alpha_i = 1$$

### Energy Conservation (Phase Change)

When accounting for heat during phase change:

$$\frac{\partial T}{\partial t} + \mathbf{u} \cdot \nabla T = \frac{1}{\rho C_p} \nabla \cdot (\kappa \nabla T) + \frac{Q}{\rho C_p}$$

where:
- $\mathbf{u}$ — fluid velocity field
- $C_p$ — specific heat capacity
- $\kappa$ — thermal conductivity
- $Q$ — latent heat release due to phase change

### VOF — Volume Fraction

The VOF method uses a scalar field $F \in [0,1]$ per phase:
- $F = 0$ — cell contains no tracked fluid
- $F = 1$ — cell fully occupied by tracked fluid
- $0 < F < 1$ — interface cell

### VOF Advection

$$\frac{\partial F}{\partial t} + \mathbf{u} \cdot \nabla F = 0$$

This guarantees conservation of volume fraction while advecting with the flow.

### Interface Representation — Mixture Properties

Properties such as density and viscosity are averaged over volume fractions in each cell:

$$\rho = \sum_{m=1}^{n} \alpha_m \rho_m$$

### Surface Tension (Continuum Surface Force)

$$\mathbf{F}_{st} = \sigma \kappa \mathbf{n} \delta_s$$

where the interface curvature $\kappa$ is computed as:

$$\kappa = \nabla \cdot \left( \frac{\nabla F}{|\nabla F|} \right)$$

### Continuity Equation

For incompressible flows ($\rho$ = constant):

$$\nabla \cdot \mathbf{u} = 0$$

ensuring the velocity field is divergence-free.

### Momentum Equation (Navier-Stokes)

$$\frac{\partial \rho \mathbf{u}}{\partial t} + \nabla \cdot (\rho \mathbf{u}\mathbf{u}) = -\nabla p + \nabla \cdot (\mu \nabla \mathbf{u}) + \mathbf{F}_{st} + \mathbf{F}_g$$

where:
- $\frac{\partial \rho \mathbf{u}}{\partial t}$ — transient momentum change
- $\nabla \cdot (\rho \mathbf{u}\mathbf{u})$ — convective momentum transport
- $-\nabla p$ — pressure gradient force
- $\nabla \cdot (\mu \nabla \mathbf{u})$ — viscous diffusion
- $\mathbf{F}_{st}$ — surface tension force
- $\mathbf{F}_g$ — gravitational body force

### AMR Refinement Criterion

Cells are refined where the volume fraction gradient exceeds a threshold:

$$\text{Refine if} \quad |\nabla F| > C_{\text{threshold}}$$

Regions away from interfaces remain coarse, optimising resource utilisation.

---

## Repository Structure

```
three-phase-flow-vof/
├── src/
│   └── three_phase_vof.c          # Basilisk C simulation code
├── outputs/
│   ├── f1_surface.png             # Fig 1a — Phase 1 surface
│   ├── f1_surface_edges.png       # Fig 1b — Phase 1 surface with edges
│   ├── f1_points.png              # Fig 1c — Phase 1 points
│   ├── f2_surface.png             # Fig 2a — Phase 2 surface
│   ├── f2_surface_edges.png       # Fig 2b — Phase 2 surface with edges
│   ├── f2_points.png              # Fig 2c — Phase 2 points
│   ├── f3_surface.png             # Fig 3a — Phase 3 surface
│   ├── f3_surface_edges.png       # Fig 3b — Phase 3 surface with edges
│   ├── f3_points.png              # Fig 3c — Phase 3 points
│   ├── pressure_surface.png       # Fig 4  — Pressure & vortex generation
│   ├── ux_surface.png             # Fig 5a — Velocity field u.x
│   └── uy_surface.png             # Fig 5b — Velocity field u.y
├── paper/
│   └── Numerical_Simulation_of_Three-Phase_Flow.pdf
└── README.md
```

---

## Code Structure (Basilisk C)

The simulation framework is structured into four modules:

**1. Domain Setup**
Initialises the simulation domain, boundary conditions, and time-stepping loop. Brings together all fluid dynamics modules.

**2. Material Properties**
Defines densities, viscosities, and surface tension coefficients for 3 immiscible fluids. Volume fraction variables (f1, f2, f3) track each phase throughout the simulation.

**3. Momentum Conservation**
A three-phase momentum-conserving VOF advection scheme prevents artificial mass transfer during interface transport via interphase momentum conservation.

**4. Interface Reconstruction**
Calculates volume fractions at phase contact regions and applies geometric PLIC (Piecewise Linear Interface Calculation) reconstruction to identify and track phase boundaries.

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

Load `.vtu` output files in ParaView. Three representation modes used:

| Mode | Purpose |
|------|---------|
| **Surface** | Smooth interface visualisation |
| **Surface with Edges** | Displays AMR mesh structure |
| **Points** | Discrete phase data at cell centres |

Visualise: `f1`, `f2`, `f3` (volume fractions), `p` (pressure), `u.x`, `u.y` (velocity components).

---

## Results

### Figure 1 — Interface Evolution Over Time (f1)

Phase 1 volume fraction tracked over time, showing interface deformation consistent with theoretical buoyancy-driven flow predictions.

<p align="center">
  <img src="outputs/f1_surface.png" width="280" alt="f1 surface"/>
  &nbsp;&nbsp;
  <img src="outputs/f1_surface_edges.png" width="280" alt="f1 surface with edges"/>
  &nbsp;&nbsp;
  <img src="outputs/f1_points.png" width="280" alt="f1 points"/>
</p>
<p align="center">
  <em>(a) f1 – surface &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (b) f1 – surface with edges &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (c) f1 – points</em>
</p>

---

### Figure 2 — Deformation and Trajectory of Bubble (f2)

Phase 2 bubble dynamics showing deformation and trajectory as the bubble ascends through stratified liquid layers. Buoyancy confirmed as the dominant driving force.

<p align="center">
  <img src="outputs/f2_surface.png" width="280" alt="f2 surface"/>
  &nbsp;&nbsp;
  <img src="outputs/f2_surface_edges.png" width="280" alt="f2 surface with edges"/>
  &nbsp;&nbsp;
  <img src="outputs/f2_points.png" width="280" alt="f2 points"/>
</p>
<p align="center">
  <em>(a) f2 – surface &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (b) f2 – surface with edges &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (c) f2 – points</em>
</p>

---

### Figure 3 — Deformation and Trajectory of Bubble (f3)

Phase 3 dynamics illustrating interaction between the third phase and surrounding liquid layers, demonstrating the framework's ability to handle complex triple-phase contact lines.

<p align="center">
  <img src="outputs/f3_surface.png" width="280" alt="f3 surface"/>
  &nbsp;&nbsp;
  <img src="outputs/f3_surface_edges.png" width="280" alt="f3 surface with edges"/>
  &nbsp;&nbsp;
  <img src="outputs/f3_points.png" width="280" alt="f3 points"/>
</p>
<p align="center">
  <em>(a) f3 – surface &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (b) f3 – surface with edges &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (c) f3 – points</em>
</p>

---

### Figure 4 — Pressure Distribution & Vortex Generation

Pressure distribution (p) around rising bubbles reveals vortex formation driven by surface tension. This directly influences flow patterns and mass transfer rates between phases.

<p align="center">
  <img src="outputs/pressure_surface.png" width="450" alt="Pressure distribution and vortex generation"/>
  <br>
  <em>Fig. 4: Pressure distribution & vortex generation around the bubbles (p-surface)</em>
</p>

---

### Figure 5 — Velocity Field Analysis (u.x and u.y)

Velocity components confirm expected flow patterns: upward plume in bubble wake, recirculation zones at phase interfaces, and surface-tension-driven lateral flows.

<p align="center">
  <img src="outputs/ux_surface.png" width="380" alt="u.x velocity surface"/>
  &nbsp;&nbsp;
  <img src="outputs/uy_surface.png" width="380" alt="u.y velocity surface"/>
</p>
<p align="center">
  <em>(a) u.x – surface &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (b) u.y – surface</em>
</p>

---

## Novel Contributions

1. **Higher Interface Resolution** — AMR achieves finer resolution at phase boundaries than fixed-grid approaches, crucial for complex interfacial dynamics without prohibitive computational cost.

2. **Robust Validation Against Theory** — Results closely match theoretical models for buoyancy-driven three-phase flows, lending confidence in the framework for real-world multiphase systems.

3. **Industrial Applicability** — Framework directly applicable to oil recovery, chemical processing, environmental engineering, and waste minimisation — any system dependent on robust phase interactions.

---

## References

1. G. Pozzetti and B. Peters, *International Journal of Multiphase Flow*, vol. 99, pp. 186–204, 2018.
2. C. Zhao et al., *arXiv:2310.12826*, 2023.
3. M. Bagheri et al., *The Canadian Journal of Chemical Engineering*, vol. 100, no. 9, pp. 2291–2308, 2022.
4. M. Shen and B. Q. Li, *RSC Advances*, vol. 13, no. 6, pp. 3561–3574, 2023.
5. J. Kim and J. Lowengrub, *Interfaces and Free Boundaries*, vol. 7, no. 4, pp. 435–466, 2005.
6. X. Yuan et al., *Physics of Fluids*, vol. 34, no. 2, 2022.
7. S. Mirjalili and A. Mani, *Journal of Computational Physics*, vol. 498, p. 112657, 2024.
8. L. Zeng et al., *Fluids*, vol. 6, no. 9, p. 317, 2021.
9. Z. Xie et al., *International Journal for Numerical Methods in Fluids*, vol. 92, no. 7, pp. 765–784, 2020.
10. Z. Wang et al., *Journal of Computational Physics*, vol. 516, p. 113297, 2024.
11. Y. F. Yap et al., *International Journal of Heat and Mass Transfer*, vol. 115, pp. 730–740, 2017.
12. S. Aihara et al., *Theoretical and Computational Fluid Dynamics*, vol. 37, no. 5, pp. 639–659, 2023.
13. C. Zhan et al., *Physica D: Nonlinear Phenomena*, vol. 460, p. 134087, 2024.

---

**Author:** Thilak S | Department of Mechanical Engineering, BITS Pilani \
**Supervisor:** Dr. Shyam Sunder Yadav | Associate Professor | Department of Mechanical Engineering, BITS Pilani \
**Period:** January–May 2025 \
**Contact:** f20220771@pilani.bits-pilani.ac.in
