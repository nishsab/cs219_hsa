#!/bin/sh
echo "░░░░░░░░"
echo "░░░░░░░░ Create Conda Environment <cs219_hsa>"
echo "░░░░░░░░"
conda create --name cs219_hsa python=2.7
echo "░░░░░░░░"
echo "░░░░░░░░ Swtich to Conda Environment <cs219_hsa>"
echo "░░░░░░░░"
eval "$(conda shell.bash hook)"L
conda activate cs219_hsa
echo "░░░░░░░░"
echo "░░░░░░░░ Install Python Package <hsa> in Conda Development Mode"
echo "░░░░░░░░"
conda develop $PWD/hsa
echo "░░░░░░░░"
echo "░░░░░░░░ Build <c-bytearray>"
echo "░░░░░░░░"
cd ./hsa
cd ./c-bytearray
python setup.py build
cp build/lib.*/c_wildcard.so ../utils/.
rm -rf build
cd ..
echo "░░░░░░░░"
echo "░░░░░░░░ Generate HSA Transfer Functions"
echo "░░░░░░░░"
cd ../cs219_toy_example
python generate_transfer_functions.py
echo "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
echo "░░░░░░░░ Done!                                          ░░░░░░░░"
echo "░░░░░░░░ Make sure you swtich to conda env <cs219_hsa>  ░░░░░░░░"
echo "░░░░░░░░ before running any examples.                   ░░░░░░░░"
echo "░░░░░░░░ Try this:                                      ░░░░░░░░"
echo "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
echo "░░░░░░░░        conda activate cs219_hsa                ░░░░░░░░"
echo "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
cd ..