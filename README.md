# NanoSciTracker Image Converter

This module is part of the NanoSciTracker suite, sponsored by CNR-IOM for
the ARES Project.

## Installation

Install the dependencies:

* Numpy
* OpenCV
* LibGL

You can install them by:

```bash
sudo apt-get update
sudo apt-get python3 python3-pip
sudo apt-get -y install libgl1-mesa-glx
pip3 install numpy opencv-python
```

## Usage

### Task farming

For task-farming, take the following script file as a reference:

```bash
#!/bin/bash

let MY_ID=${OMPI_COMM_WORLD_RANK}+1
let SIZE=${OMPI_COMM_WORLD_SIZE}

# Change the following by your own
INPUT_FOLDER=input
OUTPUT_FOLDER=output
PREFIX=${INPUT_FOLDER}/img_
SUFFIX=.tif
let NUM_SAMPLES=20

for i in $(seq $MY_ID $SIZE $NUM_SAMPLES);
do
  python3 -m nsc.img.tiff2png --input ${PREFIX}${i}${SUFFIX}
done
```

Execute it:

```
mpirun <myscript>
```

### Bash

```bash
export IMAGE=./tests/Image2_10_2.tif
python3 -m nsc.img.tiff2png --input ${IMAGE}
```

### Testing

```bash
python3 -m pytest .
```

### Building the docs

```bash
cd docs && make docs
```

## MISC

Version: 0.1.2

Luis G. Leon-Vega
