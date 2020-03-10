# CS219 HSA
Out of the box version of the hsa-python library with toy example. *We did not write any the HSA code*

| Group Members 			|			
| --------------------	| 
| Allen Huang 			   | 					
| Can Aygün 				| 					
| Daniel Achee 			|				
| Nishant Sabharwal		|			
| Zixuan Zhong			   | 


## 1. Configuration

You should use either Option 1 or Option 2 (not both) depending on your Python environment.

### 1.1. Option 1: Python 2

[Peyman Kazemian](http://yuba.stanford.edu/~peyman/) wrote this python library in Python 2. If the version of Python installed on your machine is 2.x (Execute the `python -V` command to check the Python version), please configure the hsa-python library by this command: 

```bash
source configure.sh
```

### 1.2. Option 2: Conda

If you want to manage multiple Python environments with Conda and already have Conda installed, try this command instead:

```bash
source configure_conda.sh
```

## 2. The Toy Example

Go to the example folder:

```bash
cd ./cs219_toy_example
```

### 2.1. Reachability Analysis

```bash
python run_reachability.py
```

### 2.2. Loop Detection

```bash
python run_loop_detection.py
```


      
