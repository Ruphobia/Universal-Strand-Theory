# Universal Strand Theory

Universal Strand Theory is a developing model to redefine the fundamental nature of space, matter, and interactions, with the goal of eliminating superposition and uncertainty from physics. This repository contains mathematical explorations to test the theory, focusing on a new metric derived from atomic properties and a redefined Planck length.

## Core Principles

The theory proposes that space is a dynamic medium composed of strands that expand continuously. All physical phenomena—gravity, repulsion, light, and matter—emerge from the interactions of these strands.

- **Matter**: Matter is not a distinct entity but consists of strands knotted into stable configurations. An atom, such as carbon or silicon, is a localized tangle of strands, with its size (radius) and density (kg/m³) determined by the knot's structure.
- **Light**: Photons do not exist as particles. Electromagnetic radiation, observed as light, consists of perturbations propagating through the strand medium, analogous to vibrations in a network.
- **Forces**: Interactions like gravity and atomic repulsion result from strand dynamics. Expanding strands press against knotted regions, producing repulsion when knots are close (e.g., at 1.3 Å) or an apparent attraction (gravity) in less dense strand regions.
- **Superposition and Uncertainty**: The theory aims to replace quantum superposition and uncertainty with deterministic strand interactions. Quantum effects are hypothesized to arise from complex, predictable behaviors within the strand medium, not yet fully modeled.

By modeling space as a structured, active medium, the theory seeks a unified, deterministic framework for all physical phenomena, eliminating probabilistic interpretations.

## Current Exploration

The code in this repository, specifically `ElementForceCorrelation.py`, tests a central hypothesis: that a metric combining knot size, density, and a redefined Planck length correlates with material density, reflecting strand interactions. The script performs the following:

- Analyzes 20 materials (10 crystalline, 10 amorphous), including carbon (diamond) with radius 4.765e1 YottaPlanck (YP), silicon with radius 6.869e1 YP, and others, where 1 YP = 1e27 Planck lengths (1.616e-8 m).
- Computes material density (kg/m³) from mass (e.g., 1.201e1 amu for carbon, 2.809e1 amu for silicon, converted to kg via 1.660539e-27 kg/amu) and volume (m³, from radius in m).
- Calculates a metric: (radius × density) / Planck length, where radius (m) is converted from YP, density is in kg/m³, and Planck length (m) is swept from 1.616e-36 m to 4.848e-35 m to maximize correlation with density.
- Tests interactions at a reference distance of 1.3 Å, relevant for repulsive forces in the strand model, though the primary correlation is between the metric and density.
- Estimates **permeability** (dimensionless, 0.0 to 1.0) from the error in density predictions, where high permeability (e.g., carbon) indicates weaker strand interaction, and low permeability (e.g., tin) indicates stronger interaction.

Preliminary results show a Pearson correlation coefficient above 6.0e-1 at 1.3 Å, suggesting a relationship between the strand-based metric and density. Adjusting the Planck length improves this correlation, indicating the nominal Planck length (1.616e-35 m) may not fully capture strand dynamics.

## Permeability Hypothesis

Permeability is a critical concept, representing how much of the strand medium passes through a knotted structure without interacting. Knots with high permeability (e.g., carbon, radius 4.765e1 YP) produce weaker effects, while low permeability (e.g., tin, radius 8.6e1 YP) results in stronger interactions. Permeability is currently estimated indirectly from the difference between predicted and actual density values (kg/m³), scaled to 0.0–1.0. The goal is to derive permeability directly from knot properties, such as size, density (kg/m³), or strand arrangement.

## Objectives

This theory is driven by mathematical and computational exploration, with the following goals:

- Optimize the Planck length (m) to achieve a correlation of 1.0 between the radius-density-Planck metric and density (kg/m³).
- Model permeability as a function of knot structure to predict interaction strength.
- Extend the model to gravity, treating strand expansion as the source of attraction.
- Simulate strand perturbations to replicate electromagnetic wave behavior.
- Demonstrate that quantum effects, including superposition, emerge from deterministic strand interactions, eliminating uncertainty.

A perfect correlation (1.0) would support the strand model, but the ultimate aim is a complete, deterministic description of physics based on strand dynamics.

## Current Code

`ElementForceCorrelation.py` analyzes 20 materials, calculating the `(radius × density) / Planck length` metric (units: kg/m⁴) and correlating it with density (kg/m³). Key features:

- Uses radii in YottaPlanck (e.g., 4.765e1 YP, 6.869e1 YP), converted to meters (m) via 1 YP = 1.616e-8 m.
- Computes density from mass (amu to kg) and volume (m³), with a reference distance of 1.3 Å for context.
- Sweeps Planck lengths from 1.616e-36 m to 4.848e-35 m to find the optimal value.
- Outputs radii (Å), masses (amu), densities (kg/m³), metric values, density errors (kg/m³), and permeability (dimensionless) in a CSV format.

The script uses scientific notation (e.g., 1.3e-10 m for 1.3 Å) for precision and clarity.

## Invitation to Collaborate

This is an active research effort. The observed correlations (above 6.0e-1) suggest the strand model has potential, but it requires further development. We invite physicists, mathematicians, and computational scientists to:

- Improve the Planck length (m) optimization and metric formulation.
- Test the model with additional materials or properties (e.g., density in kg/m³, radii in YP).
- Explore direct calculations of permeability.
- Investigate strand perturbations to model light or quantum effects.

To contribute, clone the repository, review the code, and submit issues or pull requests. Feedback on the theory’s concepts, mathematical methods, or code implementation is encouraged. The aim is a deterministic model that unifies and simplifies physics.

## Future Directions

Future work includes refining the Planck length (m), developing a direct permeability model, and extending the theory to gravity and light. By eliminating superposition and uncertainty, Universal Strand Theory seeks a clearer, deterministic understanding of reality, where all phenomena arise from the dynamics of a single, structured medium.

Join us to explore whether strands can reshape physics.