#
# COMP 1701 Assign1.py
#
# Felipe Sarasti
#
# Assignemnt 1 - V02 Max Calculator
#
# References & Formulas
# [1]Formulas adapted from standard Cooper 12-Minute Run and Rockport Fitness Walking Tests from Wikipedia.
# VO2 max, Wikipedia: The Free Encyclopedia, Sep. 26, 2026.


def Kilometres2Metres(running_distance: float, ) -> float:
    """converts Kilometres to Metres"""
    return (running_distance * 1000)


def Seconds2Minutes(minutes: float, seconds: float, ) -> float:
    """converts the seconds into decimal minutes"""
    seconds = seconds / 60
    return (minutes + seconds)


def Kg2Lbs(weight: int, ) -> float:
    """converts kg into lbs"""
    return (weight * 2.205)


def Print_Results(Cooper_V02: str, name: str) -> None:
    """prints results from the Cooper test"""
    print(f"{name}, your V0₂ is {Cooper_V02}")


def Print_Results2(name1: str, Result: str, ) -> None:
    """prints results from the RockPort Test"""
    print(f"{name1}, your V0₂Max from the RockPort Fitness Test is {Result} ")


def Cooper_Formula(running_meters: float, ) -> str:
    """calculates V02Max using the Cooper Formula using the given variables"""
    V02Max = (running_meters - 504.9) / 44.73
    return f"{V02Max:.1f}ml/(kg*min)"


def Rock_Port_Formula(age1: int, sex: float, HR: int, new_weight: int, Total_Time: float, ) -> str:
    """calculates V02Max using the Rock_Port_Formula using the given variables"""
    V02Max1 = 132.853 - (0.0769 * new_weight) - (0.3877 * age1) - (3.2649 * Total_Time) - (0.1565 * HR) + 6.3150 * sex
    return f"{V02Max1:.1f}ml/(kg*min)"


def main() -> None:
    print("Welcome to the Cooper Test")
    name = input("Enter name: ")
    running_distance = float(input("Enter distance covered in 12 minutes of running(in km): "))
    running_metres = Kilometres2Metres(running_distance)
    Cooper_V02 = Cooper_Formula(running_metres)

    Print_Results(Cooper_V02, name)
    print("Welcome to the RockPort Test")
    name1 = input("Enter second name: ")
    age = int(input("What is your age: "))
    minutes = float(input("Enter minutes taken to walk 1 mile: "))
    seconds = float(input("Enter seconds taken to walk 1 mile: "))

    Total_Time = Seconds2Minutes(minutes, seconds)

    sex = float(input(f"Enter Sex of {name1} (1 for Male, 0 for Female)"))
    HR = int(input(f"What is {name1}'s final heart beats per minutes(bpm): "))
    weight = int(input("Enter weight(in kg): "))
    new_weight = Kg2Lbs(weight)

    Result = Rock_Port_Formula(age, sex, HR, new_weight, Total_Time)

    Print_Results2(name1, Result)




main()











