# Perceptron

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)

## About <a name="about"></a>

In this section, I have implemented the perceptron algorithm with two examples.

### perceptron surgical

model accuracy sigmoid

![model accuracy sigmoid](output/model_accuracy_sigmoid.png)

model loss sigmoid

![model loss sigmoid](output/model_loss_sigmoid.png)

confusion matrix relu

![confusion matrix relu](output/confusion_matrix_relu.png)

model accuracy tanh

![model accuracy tanh](output/model_accuracy_tanh.png)

### perceptron forecast

data plot

![data plot](output/plot_data_temperature.png)

regression on the data

![regression on the data](output/temperature_regression.png)

## Getting Started <a name="getting-started"></a>

### Installation

To begin, install the required libraries by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

Once the requirements are installed, choose a project and run it.

### perceptron_surgical

``` terminal
jupyter nbconvert --to script perceptron_surgical.ipynb
```

### perceptron_forecast

``` terminal
jupyter nbconvert --to script perceptron_forecast.ipynb
```
