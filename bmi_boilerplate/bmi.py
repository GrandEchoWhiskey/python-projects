from math import inf as infinity

class bmi:

    def __init__(self, weight: float, height: float):
        """
        Weight in kilograms (kg), height in centimeters (cm).
        """
        self.__weight = float(weight)
        self.__height = float(height)

    @property
    def weight(self):
        """
        Weight in kilograms (kg).
        """
        return self.__weight
    
    @property
    def height(self):
        """
        Height in centimeters (cm).
        """
        return self.__height

    @property
    def value(self):
        """
        BMI = weight (kg) / (height (cm) / 100) ^ 2
        """
        return self.weight / ((self.height/100) ** 2)
    
    @property
    def interpretation(self):
        """
        BMI	Weight Status
        """
        __bmi_table = {
            "Emaciation II": 16,
            "Emaciation I": 17,
            "Underweight": 18.5,
            "Normal": 25,
            "Overweight": 30,
            "Obesity I": 35,
            "Obesity II": 40,
            "Obesity III": infinity
        }
        __bmi = self.value
        for key, value in __bmi_table.items():
            if __bmi < value:
                return key
        
    def __str__(self):
        __padding = 30
        __ljust = 19
        __result = " BMI RESULT ".center(__padding, "-") + "\n"
        __result += "Weight: ".ljust(__ljust, ' ') + f"{self.weight:.1f}kg \n"
        __result += "Height: ".ljust(__ljust, ' ') + f"{self.height:.1f}cm \n"
        __result += "BMI: ".ljust(__ljust, ' ') + f"{self.value:.2f} \n"
        __result += "Interpretation: ".ljust(__ljust, ' ') + f"{self.interpretation} \n"
        __result += "-" * __padding
        return __result

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python bmi.py <weight> <height>")
        sys.exit(1)
    try:
        my_bmi = bmi(sys.argv[1], sys.argv[2])
        print(my_bmi)
    except ValueError:
        print("Invalid input")
        print("Usage: python bmi.py <weight> <height>")
        sys.exit(1)
    