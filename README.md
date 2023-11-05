# Genetic Algorithm for Investment Optimization

This Python code implements a Genetic Algorithm for optimizing investments in a given problem domain. The algorithm aims to find the best combination of investments that meet certain constraints.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Description](#description)
- [Results](#results)
- [License](#license)

## Prerequisites

Before you can run this code, make sure you have the following dependencies installed:

- Python 3.x

You can install dependencies manually or using the following command:
```bash
pip install -r requirements.txt
```

## Description

This code uses a Genetic Algorithm to optimize investments. Here's an overview of how it works:

1. It defines a set of parameters in the `cons.py` file, such as the initial population size, the number of iterations, and the selection size.

2. It generates an initial population of individuals.

3. For a specified number of iterations, it generates new individuals (children) and adds them to the population.

4. It evaluates each individual's fitness based on certain criteria and selects a subset of the population based on their fitness.

5. The best individuals, as well as the average and worst fitness values, are recorded over generations.

6. The algorithm outputs the best investment combination found.

## Results

The code provides insights into the best investment combination that meets specific constraints. It also visualizes the evolution of fitness values over generations using Matplotlib. You can run the code and examine the results to see how the algorithm performs for your specific problem.

![Example](/imgs/Example.png)

## License

This code is provided under the [MIT License](LICENSE). You are free to use and modify it as needed for your own projects.