#!/bin/sh
export PYTHONPATH=$PYTHONPATH:$PWD/hsa
cd hsa
./setup.sh

cd ../cs219_toy_example
python generate_tf.py
