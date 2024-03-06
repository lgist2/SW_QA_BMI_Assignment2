

class BMI():
    def __init__(self, weight: int, height_feet: int, height_inches: int):
        self.weight = weight
        self.height_feet = height_feet
        self.height_inches = height_inches

    
    def calculate_bmi(self) -> float:
        feet_inch = self.height_feet * 12
        weight_kg = self.weight * 0.45 #weight from lbs to kg
        height_m = ((self.height_inches + feet_inch) * 0.025)**2 #height from ft/in to meters
        final_bmi = round(weight_kg / height_m, 1) #get bmi

        return final_bmi


    def get_bmi_category(self):
        category = ['Underweight','Normal Weight', 'Overweight', 'Obese' ]
        bmi = self.calculate()
        if bmi < 18.5:
            return f'BMI: {bmi} Category: {category[0]}'
        elif bmi >= 18.5 and bmi <= 24.9:
            return f'BMI: {bmi} Category: {category[1]}'
        elif bmi >= 25 and bmi <= 29.9:
            return f'BMI: {bmi} Category: {category[2]}'
        elif bmi >= 30:
            return f'BMI: {bmi} Category: {category[3]}'


                


def main():
   bmi = BMI(125, 5, 3)

   print(bmi.get_bmi_category())





if __name__ == '__main__':
    main()