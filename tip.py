def main():
    dollars = dollars_to_float(input("How much wast the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
#def for dollar sign and .strip
def dollars_to_float(d):
    return float(d.strip('$'))
#def for percentege sign and percent,.strip
def percent_to_float(p):
    return float(p.strip('%')) / 100
main()