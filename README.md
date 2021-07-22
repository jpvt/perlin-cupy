<div align="center"><img src="https://github.com/jpvt/perlin-cupy/blob/main/docs/image/Perlin-CuPy_logo_1000px.png" width="500"/></div>

# Perlin-CuPy: Perlin-NumPy for GPU


[![pypi](https://img.shields.io/badge/pypi-perlin--cupy-violet)](https://pypi.org/project/perlin-cupy/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blueviolet)](https://github.com/jpvt/perlin-cupy/blob/main/LICENSE)
[![Author](https://img.shields.io/badge/author-jpvt-blue)](https://www.jpvteixeira.com/)

[**Install**](https://github.com/jpvt/perlin-cupy#installation)
| [**Examples**](https://github.com/jpvt/perlin-cupy/tree/main/docs/examples)


Perlin-CuPy is a Perlin-NumPy compatible library for GPU-accelerated Perlin Noise generation.
Perlin-CuPy acts as a drop-in replacement to run [existing Perlin-NumPy code](https://github.com/pvigier/perlin-numpy) on NVIDIA CUDA platforms.

```py
from perlin_cupy import (
    generate_fractal_noise_2d, generate_fractal_noise_3d,
    generate_perlin_noise_2d, generate_perlin_noise_3d
)
```

## Installation

Wheel (precompiled binary package) is available for Linux (x86_64). We've currently tested only for CUDA 11.3 platform using CuPy v11.3, but it should work for any CuPy version installed in your environment.

| Platform      | Command                              |
| ------------- | ------------------------------------ |
| CUDA 11.3     | `pip install perlin-cupy`            |

### Requirements

* [NVIDIA CUDA GPU](https://developer.nvidia.com/cuda-gpus) with the Compute Capability 3.0 or larger.
* [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit): v10.0 / v10.1 / v10.2 / v11.0 / v11.1 / v11.2 / v11.3

### Python Dependencies

* [CuPy](https://pypi.org/project/cupy/): v10.0 / v10.1 / v10.2 / v11.0 / v11.1 / v11.2 / v11.3

## Usage

The usage is exactly the same as [Perlin-NumPy](https://github.com/pvigier/perlin-numpy).

### 2D noise

The function `generate_perlin_noise_2d` generates a 2D texture of perlin noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 2 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 2 ints)
* `tileable`: if the noise should be tileable along each axis (tuple of 2 bools)

Note: `shape` must be a multiple of `res`

The function `generate_fractal_noise_2d` combines several octaves of 2D perlin noise to make 2D fractal noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 2 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 2 ints)
* `octaves`: number of octaves in the noise (int)
* `persistence`: scaling factor between two octaves (float)
* `lacunarity`: frequency factor between two octaves (float)
* `tileable`: if the noise should be tileable along each axis (tuple of 2 bools)

Note: `shape` must be a multiple of `lacunarity^(octaves-1)*res`


### 3D noise

The function `generate_perlin_noise_3d` generates a 3D texture of perlin noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 3 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 3 ints)
* `tileable`: if the noise should be tileable along each axis (tuple of 3 bools)

Note: `shape` must be a multiple of `res`

The function `generate_fractal_noise_2d` combines several octaves of 3D perlin noise to make 3D fractal noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 3 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 3 ints)
* `octaves`: number of octaves in the noise (int)
* `persistence`: scaling factor between two octaves (float)
* `lacunarity`: frequency factor between two octaves (float)
* `tileable`: if the noise should be tileable along each axis (tuple of 3 bools)

Note: `shape` must be a multiple of `lacunarity^(octaves-1)*res`

## License

MIT License (See [LICENSE](https://github.com/jpvt/perlin-cupy/blob/main/LICENSE) file).

Perlin-CuPy is designed based on Perlin-NumPy's API (see [LICENSE_THIRD_PARTY](https://github.com/jpvt/perlin-cupy/blob/main/docs/LICENSE_THIRD_PARTY) file) by Pierre Vigier.

Perlin-CuPy is being maintained and developed by [João Pedro Vasconcelos](https://github.com/jpvt).

Icon logo made by [Eucalyp](https://creativemarket.com/eucalyp) from [Flaticon](https://www.flaticon.com/).
