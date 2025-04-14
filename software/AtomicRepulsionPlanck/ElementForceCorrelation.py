#!/usr/bin/python3

import math
import pandas as pd
import numpy as np

# Constants
ANGSTROM_TO_METER = 1e-10
AMU_TO_KG = 1.660539e-27

# Data
elements = [
    {"name": "Carbon (diamond)", "radius": 47.65, "mass": 12.01},
    {"name": "Silicon", "radius": 68.69, "mass": 28.09},
    {"name": "Germanium", "radius": 75.50, "mass": 72.64},
    {"name": "Aluminum", "radius": 74.88, "mass": 26.98},
    {"name": "Copper", "radius": 81.68, "mass": 63.55},
    {"name": "Iron", "radius": 81.68, "mass": 55.85},
    {"name": "Titanium", "radius": 89.73, "mass": 47.87},
    {"name": "Tin", "radius": 86.00, "mass": 118.71},
    {"name": "Zinc", "radius": 75.50, "mass": 65.38},
    {"name": "Nickel", "radius": 76.73, "mass": 58.69},
    {"name": "Carbon (amorphous)", "radius": 47.65, "mass": 12.01},
    {"name": "Silicon (amorphous)", "radius": 68.69, "mass": 28.09},
    {"name": "Germanium (amorphous)", "radius": 75.50, "mass": 72.64},
    {"name": "Boron", "radius": 52.60, "mass": 10.81},
    {"name": "Phosphorus", "radius": 66.21, "mass": 30.97},
    {"name": "Selenium", "radius": 74.26, "mass": 78.96},
    {"name": "Tellurium", "radius": 85.40, "mass": 127.60},
    {"name": "Arsenic", "radius": 73.64, "mass": 74.92},
    {"name": "Antimony", "radius": 86.00, "mass": 121.76},
    {"name": "Palladium (amorphous)", "radius": 84.78, "mass": 106.42},
]

df = pd.DataFrame(elements)

# Convert to base units
df['radius_m'] = df['radius'] * ANGSTROM_TO_METER
df['mass_kg'] = df['mass'] * AMU_TO_KG
df['volume_m3'] = (4/3) * math.pi * df['radius_m'] ** 3
df['density'] = df['mass_kg'] / df['volume_m3']

# Sweep Planck values
planck_nominal = 1.616e-35
sweep_range = np.linspace(0.1, 3.0, 500) * planck_nominal

best_corr = None
best_planck = None
best_df = None

for pl in sweep_range:
    metric = (df['radius_m'] * df['density']) / pl
    if np.std(metric) == 0:
        continue
    corr = np.corrcoef(metric, df['density'])[0, 1]
    if not np.isnan(corr) and (best_corr is None or abs(corr) > abs(best_corr)):
        best_corr = corr
        best_planck = pl
        best_df = df.copy()
        best_df['radius_density_planck'] = metric

# Final output
if best_df is None:
    print("ERROR: No usable correlation found.")
    exit(1)

# Linear prediction for visualization
fit = np.polyfit(best_df['radius_density_planck'], best_df['density'], 1)
best_df['predicted_density'] = np.polyval(fit, best_df['radius_density_planck'])
best_df['density_diff'] = best_df['density'] - best_df['predicted_density']

# Add permeability estimation based on absolute error scaled to 0..1
max_error = np.max(np.abs(best_df['density_diff']))
best_df['estimated_permeability'] = np.abs(best_df['density_diff']) / max_error if max_error != 0 else 0

# Output CSV
print("name,radius (Å),mass (amu),density (kg/m³),radius_density_planck,density_diff (kg/m³),estimated_permeability")
for _, row in best_df.iterrows():
    print(f"{row['name']},{row['radius']:.4f},{row['mass']:.4f},{row['density']:.4f},"
          f"{row['radius_density_planck']:.4f},{row['density_diff']:.10f},{row['estimated_permeability']:.4f}")

print(f"\nBest Planck length: {best_planck:.4e} m")
print(f"Correlation (radius × density vs. density): R = {best_corr:.4f}")
