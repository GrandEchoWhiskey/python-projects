# BMI Calculator
This is a simple BMI (Body Mass Index) calculator implemented in Python. It allows you to calculate your BMI based on your weight and height inputs, and provides an interpretation of the BMI value in terms of weight status.

### Prerequisites
- Python 3.x

### Usage
To use the BMI calculator, follow the instructions below:

1. Open a terminal or command prompt.
2. Navigate to the directory where the `bmi.py` file is located.
3. Run the script with the following command:

```shell
python bmi.py <weight> <height>
```
Replace `<weight>` with your weight in kilograms (kg) and `<height>` with your height in centimeters (cm). For example:

```shell
python bmi.py 70 170
```
This will calculate the BMI and display the result.
> Note: Make sure to provide valid numeric inputs for weight and height.

### Class Details
`bmi` Class
This class represents a BMI calculator and provides the following methods:

- `__init__(self, weight: float, height: float)`: Initializes a `bmi` object with the specified weight and height inputs.
- `height`: This property returns the weight in kilograms.
- `weight`: This property returns the height in centimeters
- `value`: This property calculates and returns the BMI value based on the weight and height inputs.
- `interpretation`: This property determines the weight status interpretation based on the BMI value.
- `__str__()`: This method overrides the string representation of the `bmi` object and provides a formatted result string with weight, height, BMI, and interpretation.

### BMI Calculation
$$
bmi = \left({weight (kg)\over{height (cm) \div 100}}\right)^2
$$

### BMI Interpretation
The BMI interpretation is based on the following weight status categories:

BMI	| Weight Status
--- | ---
15.9 or less | Emaciation II
16 - 16.9 | Emaciation I
17 - 18.5 | Underweight
18.5 - 24.9 | Normal
25 - 29.9 | Overweight
30 - 34.9 | Obesity I
35 - 39.9 | Obesity II
40 or greater | Obesity III

### Example
Here's an example of running the script:

```shell
$ python bmi.py 70 170
---------- BMI RESULT ----------
Weight:             70.0kg
Height:             170.0cm
BMI:                24.22
Interpretation:     Normal
-------------------------------
```
In this example, a weight of 70.0 kg and a height of 170.0 cm were provided. The calculated BMI is 24.22, which falls within the "Normal" weight status category.

### Contributing
Contributions to this BMI calculator are welcome. If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request on the GitHub repository.
