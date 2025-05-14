## Benchmark Score Table 

| Model                   |   Avg MAE ↓ |   Rank |
|:------------------------|------------:|-------:|
| mace_omat_0_D3          |       5.335 |      1 |
| mace_matpes_r2scan_0_D3 |       5.391 |      2 |
| mace_mpa_0_D3           |       6.422 |      3 |
| mace_mp_0a_D3           |       9.446 |      4 |
| mace_matpes_PBE_0_D3    |       9.703 |      5 |
| mace_mp_0b3_D3          |      11.553 |      6 |


## Combined MAE Table 

| Model                   |   $K_{bulk}$ [GPa] |   $K_{shear}$ [GPa] |   Elasticity Score (avg) |   Rank |   Lat Const [Å] |   Rank |   $ω_{max}$ [THz] |   S [J/mol·K] |   F [kJ/mol] |   $C_{V}$ [J/mol·K] |   Phonon Score (avg) |   Rank |
|:------------------------|-------------------:|--------------------:|-------------------------:|-------:|----------------:|-------:|------------------:|--------------:|-------------:|--------------------:|---------------------:|-------:|
| mace_mp_0a_D3           |             48.032 |              13.867 |                   30.95  |      4 |           0.027 |      2 |             0.631 |         4.63  |        1.42  |               0.101 |                1.696 |      6 |
| mace_mp_0b3_D3          |             56.672 |              23.4   |                   40.036 |      6 |           0.027 |      2 |             0.38  |         3.637 |        1.113 |               0.073 |                1.301 |      4 |
| mace_mpa_0_D3           |             41.211 |               3.442 |                   22.326 |      3 |           0.019 |      1 |             0.025 |         2.44  |        0.745 |               0.041 |                0.813 |      2 |
| mace_omat_0_D3          |             22.798 |              11.507 |                   17.152 |      2 |           0.067 |      6 |             0.002 |         2.116 |        0.646 |               0.037 |                0.7   |      1 |
| mace_matpes_PBE_0_D3    |             47.555 |              16.274 |                   31.914 |      5 |           0.035 |      4 |             0.476 |         3.658 |        1.12  |               0.075 |                1.332 |      5 |
| mace_matpes_r2scan_0_D3 |             30.493 |               3.101 |                   16.797 |      1 |           0.044 |      5 |             0.008 |         3.169 |        0.97  |               0.063 |                1.052 |      3 |

\newpage


# Elasticity Report

## Bulk and Shear Moduli MAE Table

| Model                   |   K_bulk [GPa] |   K_shear [GPa] |   Elasticity Score (avg) |   Rank |
|:------------------------|---------------:|----------------:|-------------------------:|-------:|
| mace_mp_0a_D3           |         48.032 |          13.867 |                   30.95  |      4 |
| mace_mp_0b3_D3          |         56.672 |          23.4   |                   40.036 |      6 |
| mace_mpa_0_D3           |         41.211 |           3.442 |                   22.326 |      3 |
| mace_omat_0_D3          |         22.798 |          11.507 |                   17.152 |      2 |
| mace_matpes_PBE_0_D3    |         47.555 |          16.274 |                   31.914 |      5 |
| mace_matpes_r2scan_0_D3 |         30.493 |           3.101 |                   16.797 |      1 |


## Scatter and density Plots

### mace_mp_0a_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mp_0a_D3/scatter_plots/K_bulk_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mp_0a_D3/scatter_plots/K_bulk_scatter.png){ width=50% }

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mp_0a_D3/scatter_plots/K_shear_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mp_0a_D3/scatter_plots/K_shear_scatter.png){ width=50% }

### mace_mp_0b3_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mp_0b3_D3/scatter_plots/K_bulk_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mp_0b3_D3/scatter_plots/K_bulk_scatter.png){ width=50% }

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mp_0b3_D3/scatter_plots/K_shear_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mp_0b3_D3/scatter_plots/K_shear_scatter.png){ width=50% }

### mace_mpa_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mpa_0_D3/scatter_plots/K_bulk_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mpa_0_D3/scatter_plots/K_bulk_scatter.png){ width=50% }

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mpa_0_D3/scatter_plots/K_shear_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_mpa_0_D3/scatter_plots/K_shear_scatter.png){ width=50% }

### mace_omat_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_omat_0_D3/scatter_plots/K_bulk_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_omat_0_D3/scatter_plots/K_bulk_scatter.png){ width=50% }

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_omat_0_D3/scatter_plots/K_shear_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_omat_0_D3/scatter_plots/K_shear_scatter.png){ width=50% }

### mace_matpes_PBE_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_matpes_PBE_0_D3/scatter_plots/K_bulk_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_matpes_PBE_0_D3/scatter_plots/K_bulk_scatter.png){ width=50% }

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_matpes_PBE_0_D3/scatter_plots/K_shear_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_matpes_PBE_0_D3/scatter_plots/K_shear_scatter.png){ width=50% }

### mace_matpes_r2scan_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_matpes_r2scan_0_D3/scatter_plots/K_bulk_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_matpes_r2scan_0_D3/scatter_plots/K_bulk_scatter.png){ width=50% }

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_matpes_r2scan_0_D3/scatter_plots/K_shear_density.png){ width=50% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/elasticity/mace_matpes_r2scan_0_D3/scatter_plots/K_shear_scatter.png){ width=50% }


\newpage


# Lattice Constants Report

## Lattice Constants MAE Table

| Model                   |   Lat Const [Å] |   Rank |
|:------------------------|----------------:|-------:|
| mace_mp_0a_D3           |           0.027 |      2 |
| mace_mp_0b3_D3          |           0.027 |      2 |
| mace_mpa_0_D3           |           0.019 |      1 |
| mace_omat_0_D3          |           0.067 |      6 |
| mace_matpes_PBE_0_D3    |           0.035 |      4 |
| mace_matpes_r2scan_0_D3 |           0.044 |      5 |


## Per-Model Tables and Scatter Plots

### mace_mp_0a_D3

| Element   |   DFT (Å) |   mace_mp_0a_D3 (Å) |      Δ |   Δ/% |
|:----------|----------:|--------------------:|-------:|------:|
| Ag        |     4.082 |               4.093 |  0.011 |  0.27 |
| Pd        |     3.891 |               3.907 |  0.016 |  0.41 |
| Rh        |     3.76  |               3.813 |  0.053 |  1.41 |
| Li        |     3.352 |               3.3   | -0.052 | -1.55 |
| Na        |     4.107 |               4.069 | -0.038 | -0.93 |
| K         |     5.191 |               5.138 | -0.053 | -1.02 |
| Rb        |     5.572 |               5.461 | -0.111 | -1.99 |
| Cs        |     6.106 |               6.103 | -0.003 | -0.05 |
| Ca        |     5.463 |               5.42  | -0.043 | -0.79 |
| Sr        |     5.908 |               5.948 |  0.04  |  0.68 |
| Ba        |     4.976 |               4.938 | -0.038 | -0.76 |
| Al        |     4.002 |               3.993 | -0.009 | -0.22 |
| LiF       |     3.995 |               4.017 |  0.022 |  0.55 |
| NaF       |     4.619 |               4.619 |  0     |  0    |
| NaCl      |     5.585 |               5.585 |  0     |  0    |
| MgO       |     4.203 |               4.204 |  0.001 |  0.02 |
| Si        |     5.434 |               5.396 | -0.038 | -0.7  |
| Ge        |     5.719 |               5.702 | -0.017 | -0.3  |
| GaAs      |     5.69  |               5.659 | -0.031 | -0.54 |
| Cu        |     3.568 |               3.561 | -0.007 | -0.2  |
| C         |     3.562 |               3.556 | -0.006 | -0.17 |
| LiCl      |     5.056 |               5.018 | -0.038 | -0.75 |
| SiC(a)    |     3.072 |               3.076 |  0.004 |  0.13 |
| SiC(c)    |     5.029 |               5.024 | -0.005 | -0.1  |


![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/lattice_constants/mace_mp_0a_D3/scatter_plots/lattice_constants.png){ width=100% }

### mace_mp_0b3_D3

| Element   |   DFT (Å) |   mace_mp_0b3_D3 (Å) |      Δ |   Δ/% |
|:----------|----------:|---------------------:|-------:|------:|
| Ag        |     4.082 |                4.082 |  0     |  0    |
| Pd        |     3.891 |                3.911 |  0.02  |  0.51 |
| Rh        |     3.76  |                3.808 |  0.048 |  1.28 |
| Li        |     3.352 |                3.29  | -0.062 | -1.85 |
| Na        |     4.107 |                4.178 |  0.071 |  1.73 |
| K         |     5.191 |                5.191 |  0     |  0    |
| Rb        |     5.572 |                5.572 |  0     |  0    |
| Cs        |     6.106 |                5.928 | -0.178 | -2.92 |
| Ca        |     5.463 |                5.441 | -0.022 | -0.4  |
| Sr        |     5.908 |                5.958 |  0.05  |  0.85 |
| Ba        |     4.976 |                4.952 | -0.024 | -0.48 |
| Al        |     4.002 |                3.988 | -0.014 | -0.35 |
| LiF       |     3.995 |                4.02  |  0.025 |  0.63 |
| NaF       |     4.619 |                4.598 | -0.021 | -0.45 |
| NaCl      |     5.585 |                5.585 |  0     |  0    |
| MgO       |     4.203 |                4.203 |  0     |  0    |
| Si        |     5.434 |                5.417 | -0.017 | -0.31 |
| Ge        |     5.719 |                5.673 | -0.046 | -0.8  |
| GaAs      |     5.69  |                5.676 | -0.014 | -0.25 |
| Cu        |     3.568 |                3.547 | -0.021 | -0.59 |
| C         |     3.562 |                3.55  | -0.012 | -0.34 |
| LiCl      |     5.056 |                5.056 |  0     |  0    |
| SiC(a)    |     3.072 |                3.078 |  0.006 |  0.2  |
| SiC(c)    |     5.029 |                5.035 |  0.006 |  0.12 |


![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/lattice_constants/mace_mp_0b3_D3/scatter_plots/lattice_constants.png){ width=100% }

### mace_mpa_0_D3

| Element   |   DFT (Å) |   mace_mpa_0_D3 (Å) |      Δ |   Δ/% |
|:----------|----------:|--------------------:|-------:|------:|
| Ag        |     4.082 |               4.082 |  0     |  0    |
| Pd        |     3.891 |               3.899 |  0.008 |  0.21 |
| Rh        |     3.76  |               3.81  |  0.05  |  1.33 |
| Li        |     3.352 |               3.351 | -0.001 | -0.03 |
| Na        |     4.107 |               4.061 | -0.046 | -1.12 |
| K         |     5.191 |               5.191 |  0     |  0    |
| Rb        |     5.572 |               5.572 |  0     |  0    |
| Cs        |     6.106 |               6.106 |  0     |  0    |
| Ca        |     5.463 |               5.46  | -0.003 | -0.05 |
| Sr        |     5.908 |               5.948 |  0.04  |  0.68 |
| Ba        |     4.976 |               4.927 | -0.049 | -0.98 |
| Al        |     4.002 |               3.983 | -0.019 | -0.47 |
| LiF       |     3.995 |               4.032 |  0.037 |  0.93 |
| NaF       |     4.619 |               4.648 |  0.029 |  0.63 |
| NaCl      |     5.585 |               5.585 |  0     |  0    |
| MgO       |     4.203 |               4.211 |  0.008 |  0.19 |
| Si        |     5.434 |               5.417 | -0.017 | -0.31 |
| Ge        |     5.719 |               5.666 | -0.053 | -0.93 |
| GaAs      |     5.69  |               5.675 | -0.015 | -0.26 |
| Cu        |     3.568 |               3.568 |  0     |  0    |
| C         |     3.562 |               3.562 |  0     |  0    |
| LiCl      |     5.056 |               5.092 |  0.036 |  0.71 |
| SiC(a)    |     3.072 |               3.086 |  0.014 |  0.46 |
| SiC(c)    |     5.029 |               5.05  |  0.021 |  0.42 |


![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/lattice_constants/mace_mpa_0_D3/scatter_plots/lattice_constants.png){ width=100% }

### mace_omat_0_D3

| Element   |   DFT (Å) |   mace_omat_0_D3 (Å) |      Δ |   Δ/% |
|:----------|----------:|---------------------:|-------:|------:|
| Ag        |     4.082 |                4.073 | -0.009 | -0.22 |
| Pd        |     3.891 |                3.891 |  0     |  0    |
| Rh        |     3.76  |                3.782 |  0.022 |  0.59 |
| Li        |     3.352 |                3.328 | -0.024 | -0.72 |
| Na        |     4.107 |                4.107 |  0     |  0    |
| K         |     5.191 |                5.315 |  0.124 |  2.39 |
| Rb        |     5.572 |                5.978 |  0.406 |  7.29 |
| Cs        |     6.106 |                6.791 |  0.685 | 11.22 |
| Ca        |     5.463 |                5.441 | -0.022 | -0.4  |
| Sr        |     5.908 |                5.985 |  0.077 |  1.3  |
| Ba        |     4.976 |                4.976 |  0     |  0    |
| Al        |     4.002 |                3.969 | -0.033 | -0.82 |
| LiF       |     3.995 |                3.995 |  0     |  0    |
| NaF       |     4.619 |                4.619 |  0     |  0    |
| NaCl      |     5.585 |                5.566 | -0.019 | -0.34 |
| MgO       |     4.203 |                4.203 |  0     |  0    |
| Si        |     5.434 |                5.37  | -0.064 | -1.18 |
| Ge        |     5.719 |                5.658 | -0.061 | -1.07 |
| GaAs      |     5.69  |                5.682 | -0.008 | -0.14 |
| Cu        |     3.568 |                3.568 |  0     |  0    |
| C         |     3.562 |                3.548 | -0.014 | -0.39 |
| LiCl      |     5.056 |                5.041 | -0.015 | -0.3  |
| SiC(a)    |     3.072 |                3.068 | -0.004 | -0.13 |
| SiC(c)    |     5.029 |                5.011 | -0.018 | -0.36 |


![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/lattice_constants/mace_omat_0_D3/scatter_plots/lattice_constants.png){ width=100% }

### mace_matpes_PBE_0_D3

| Element   |   DFT (Å) |   mace_matpes_PBE_0_D3 (Å) |      Δ |   Δ/% |
|:----------|----------:|---------------------------:|-------:|------:|
| Ag        |     4.082 |                      4.051 | -0.031 | -0.76 |
| Pd        |     3.891 |                      3.884 | -0.007 | -0.18 |
| Rh        |     3.76  |                      3.779 |  0.019 |  0.51 |
| Li        |     3.352 |                      3.302 | -0.05  | -1.49 |
| Na        |     4.107 |                      4.107 |  0     |  0    |
| K         |     5.191 |                      5.191 |  0     |  0    |
| Rb        |     5.572 |                      5.572 |  0     |  0    |
| Cs        |     6.106 |                      5.924 | -0.182 | -2.98 |
| Ca        |     5.463 |                      5.438 | -0.025 | -0.46 |
| Sr        |     5.908 |                      5.999 |  0.091 |  1.54 |
| Ba        |     4.976 |                      4.974 | -0.002 | -0.04 |
| Al        |     4.002 |                      3.985 | -0.017 | -0.42 |
| LiF       |     3.995 |                      3.933 | -0.062 | -1.55 |
| NaF       |     4.619 |                      4.579 | -0.04  | -0.87 |
| NaCl      |     5.585 |                      5.544 | -0.041 | -0.73 |
| MgO       |     4.203 |                      4.101 | -0.102 | -2.43 |
| Si        |     5.434 |                      5.406 | -0.028 | -0.52 |
| Ge        |     5.719 |                      5.664 | -0.055 | -0.96 |
| GaAs      |     5.69  |                      5.704 |  0.014 |  0.25 |
| Cu        |     3.568 |                      3.556 | -0.012 | -0.34 |
| C         |     3.562 |                      3.533 | -0.029 | -0.81 |
| LiCl      |     5.056 |                      5.056 |  0     |  0    |
| SiC(a)    |     3.072 |                      3.069 | -0.003 | -0.1  |
| SiC(c)    |     5.029 |                      5.052 |  0.023 |  0.46 |


![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/lattice_constants/mace_matpes_PBE_0_D3/scatter_plots/lattice_constants.png){ width=100% }

### mace_matpes_r2scan_0_D3

| Element   |   DFT (Å) |   mace_matpes_r2scan_0_D3 (Å) |      Δ |   Δ/% |
|:----------|----------:|------------------------------:|-------:|------:|
| Ag        |     4.082 |                         4.067 | -0.015 | -0.37 |
| Pd        |     3.891 |                         3.895 |  0.004 |  0.1  |
| Rh        |     3.76  |                         3.812 |  0.052 |  1.38 |
| Li        |     3.352 |                         3.373 |  0.021 |  0.63 |
| Na        |     4.107 |                         4.107 |  0     |  0    |
| K         |     5.191 |                         5.248 |  0.057 |  1.1  |
| Rb        |     5.572 |                         5.572 |  0     |  0    |
| Cs        |     6.106 |                         6.053 | -0.053 | -0.87 |
| Ca        |     5.463 |                         5.557 |  0.094 |  1.72 |
| Sr        |     5.908 |                         6.096 |  0.188 |  3.18 |
| Ba        |     4.976 |                         4.976 |  0     |  0    |
| Al        |     4.002 |                         3.963 | -0.039 | -0.97 |
| LiF       |     3.995 |                         3.925 | -0.07  | -1.75 |
| NaF       |     4.619 |                         4.522 | -0.097 | -2.1  |
| NaCl      |     5.585 |                         5.479 | -0.106 | -1.9  |
| MgO       |     4.203 |                         4.164 | -0.039 | -0.93 |
| Si        |     5.434 |                         5.415 | -0.019 | -0.35 |
| Ge        |     5.719 |                         5.622 | -0.097 | -1.7  |
| GaAs      |     5.69  |                         5.671 | -0.019 | -0.33 |
| Cu        |     3.568 |                         3.547 | -0.021 | -0.59 |
| C         |     3.562 |                         3.575 |  0.013 |  0.36 |
| LiCl      |     5.056 |                         5.017 | -0.039 | -0.77 |
| SiC(a)    |     3.072 |                         3.074 |  0.002 |  0.07 |
| SiC(c)    |     5.029 |                         5.047 |  0.018 |  0.36 |


![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/lattice_constants/mace_matpes_r2scan_0_D3/scatter_plots/lattice_constants.png){ width=100% }


\newpage


# Phonon Dispersion Report

## Phonon MAE Summary Table (300K)

| Model                   |   $\omega_{max}$ [THz] |   S [J/mol·K] |   F [kJ/mol] |   C_V [J/mol·K] |   Phonon Score (avg) |   Rank |
|:------------------------|--------------:|--------------:|-------------:|----------------:|---------------------:|-------:|
| mace_mp_0a_D3           |         0.631 |         4.63  |        1.42  |           0.101 |                1.696 |      6 |
| mace_mp_0b3_D3          |         0.38  |         3.637 |        1.113 |           0.073 |                1.301 |      4 |
| mace_mpa_0_D3           |         0.025 |         2.44  |        0.745 |           0.041 |                0.813 |      2 |
| mace_omat_0_D3          |         0.002 |         2.116 |        0.646 |           0.037 |                0.7   |      1 |
| mace_matpes_PBE_0_D3    |         0.476 |         3.658 |        1.12  |           0.075 |                1.332 |      5 |
| mace_matpes_r2scan_0_D3 |         0.008 |         3.169 |        0.97  |           0.063 |                1.052 |      3 |


## Scatter Plots

### mace_mp_0a_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mp_0a_D3/scatter_plots/C_V.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mp_0a_D3/scatter_plots/F.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mp_0a_D3/scatter_plots/S.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mp_0a_D3/scatter_plots/max_freq.png){ width=25% }

### mace_mp_0b3_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mp_0b3_D3/scatter_plots/C_V.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mp_0b3_D3/scatter_plots/F.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mp_0b3_D3/scatter_plots/S.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mp_0b3_D3/scatter_plots/max_freq.png){ width=25% }

### mace_mpa_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mpa_0_D3/scatter_plots/C_V.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mpa_0_D3/scatter_plots/F.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mpa_0_D3/scatter_plots/S.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mpa_0_D3/scatter_plots/max_freq.png){ width=25% }

### mace_omat_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_omat_0_D3/scatter_plots/C_V.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_omat_0_D3/scatter_plots/F.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_omat_0_D3/scatter_plots/S.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_omat_0_D3/scatter_plots/max_freq.png){ width=25% }

### mace_matpes_PBE_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_matpes_PBE_0_D3/scatter_plots/C_V.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_matpes_PBE_0_D3/scatter_plots/F.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_matpes_PBE_0_D3/scatter_plots/S.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_matpes_PBE_0_D3/scatter_plots/max_freq.png){ width=25% }

### mace_matpes_r2scan_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_matpes_r2scan_0_D3/scatter_plots/C_V.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_matpes_r2scan_0_D3/scatter_plots/F.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_matpes_r2scan_0_D3/scatter_plots/S.png){ width=25% } ![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_matpes_r2scan_0_D3/scatter_plots/max_freq.png){ width=25% }

## Dispersion Plots

### mace_mp_0a_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mp_0a_D3/phonon_plots/dispersion_mace_mp_0a_D3_mp-1000.png){ width=25% }

### mace_mp_0b3_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mp_0b3_D3/phonon_plots/dispersion_mace_mp_0b3_D3_mp-1000.png){ width=25% }

### mace_mpa_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_mpa_0_D3/phonon_plots/dispersion_mace_mpa_0_D3_mp-1000.png){ width=25% }

### mace_omat_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_omat_0_D3/phonon_plots/dispersion_mace_omat_0_D3_mp-1000.png){ width=25% }

### mace_matpes_PBE_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_matpes_PBE_0_D3/phonon_plots/dispersion_mace_matpes_PBE_0_D3_mp-1000.png){ width=25% }

### mace_matpes_r2scan_0_D3

![](/Users/joehart/Desktop/0_Cambridge/0_MPhil_Scientific_Computing/MPhil_project/mlipx_testing/benchmark_app/benchmark_stats/bulk_crystal_benchmark/phonons/mace_matpes_r2scan_0_D3/phonon_plots/dispersion_mace_matpes_r2scan_0_D3_mp-1000.png){ width=25% }


\newpage

