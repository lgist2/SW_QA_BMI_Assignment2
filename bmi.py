

class BMI():
    def __init__(self, weight: int, height_feet: int, height_inches: int):
        self.weight = weight
        self.height_feet = height_feet
        self.height_inches = height_inches

    
    def bmi_calculate(self) -> float:
        feet_inch = self.height_feet * 12
        weight_kg = self.weight * 0.45 #weight from lbs to kg
        height_m = ((self.height_inches + feet_inch) * 0.025)**2 #height from ft/in to meters
        final_bmi = round(weight_kg / height_m, 1) #get bmi

        return final_bmi


    def bmi_category(self) -> str:
        category = ['Underweight','Normal Weight', 'Overweight', 'Obese' ]
        bmi = self.bmi_calculate()
        if bmi < 18.5:
            return category[0]
        elif bmi >= 18.5 and bmi <= 24.9:
            return category[1]
        elif bmi >= 25 and bmi <= 29.9:
            return category[2]
        elif bmi >= 30:
            return category[3]


    def display_bmi_info(self) -> str:
        bmi = self.bmi_calculate()
        category = self.bmi_category()
        return f'BMI: {bmi} Category: {category}'
                


def main():
   bmi = BMI(125, 5, 3)

   print(bmi.get_bmi_category())
   print(bmi.display_bmi_info())





if __name__ == '__main__':
    main()