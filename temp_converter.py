while True:
    while True:
        try:
            temperature = float(input("Enter the desired temperature:\n"))
            break
        except ValueError:
            print("Please type a number for temperature.")
    temperature_unit = input("""\nPlease enter the temperature unit entered.
(Enter C for celisus.
Enter F for fahrenheit.
Enter K for kelvin.)
""")
    strip_of_temperature_unit = temperature_unit.strip()
    if strip_of_temperature_unit.upper() == "C" or strip_of_temperature_unit.upper() == "F" or strip_of_temperature_unit.upper() == "K":
        desired_temperature_unit = input("""\nPlease enter the desired temperature unit.
(Enter C for celisus.
Enter F for fahrenheit.
Enter K for kelvin.)
""")
        strip_of_desired_temperature_unit = desired_temperature_unit.strip()
        if strip_of_desired_temperature_unit.upper() == "C" or strip_of_desired_temperature_unit.upper() == "F" or strip_of_desired_temperature_unit.upper() == "K":
            if strip_of_temperature_unit.upper() == "C":
                if strip_of_desired_temperature_unit.upper() == "C":
                    answer_c_c = "\nAnswer: {}"
                    print(answer_c_c.format(temperature))
                    print("Its relation:\n'C' = 'C'")
                elif strip_of_desired_temperature_unit.upper() == "F":
                    answer_c_f = "\nAnswer: {}"
                    print(answer_c_f.format((temperature * 1.8) + 32))
                    print("Its relation:\n'F' = 'C' × 1.8 + 32")
                elif strip_of_desired_temperature_unit.upper() == "K":
                    answer_c_k = "\nAnswer: {}"
                    print(answer_c_k.format(temperature + 273.15))
                    print("Its relation:\n'K' = 'C' + 273.15")
            elif strip_of_temperature_unit.upper() == "F":
                if strip_of_desired_temperature_unit.upper() == "C":
                    answer_f_c = "\nAnswer: {}"
                    print(answer_f_c.format((temperature - 32) / 1.8))
                    print("Its relation:\n'C' = ('F' - 32) ÷ 1.8")
                elif strip_of_desired_temperature_unit.upper() == "F":
                    answer_f_f = "\nAnswer: {}"
                    print(answer_f_f.format(temperature))
                    print("Its relation:\n'F' = 'F'")
                elif strip_of_desired_temperature_unit.upper() == "K":
                    answer_f_k = "\nAnswer: {}"
                    print(answer_f_k.format((temperature + 459.67) / 1.8))
                    print("Its relation:\n'K' = ('F' + 459.67) ÷ 1.8")
            elif strip_of_temperature_unit.upper() == "K":
                if strip_of_desired_temperature_unit.upper() == "C":
                    answer_k_c = "\nAnswer: {}"
                    print(answer_k_c.format(temperature - 273.15))
                    print("Its relation:\n'C' = 'K' - 273.15")
                elif strip_of_desired_temperature_unit.upper() == "F":
                    answer_k_f = "\nAnswer: {}"
                    print(answer_k_f.format(temperature * 1.8 - 459.67))
                    print("Its relation:\n'F' = 'K' × 1.8 - 459.67")
                elif strip_of_desired_temperature_unit.upper() == "K":
                    answer_k_k = "\nAnswer: {}"
                    print(answer_k_k.format(temperature))
                    print("Its relation:\n'K' = 'K'")
        else:
            print(
                "\nYou have not typed a temperature unit, Please run the program again.")
    else:
        print("\nYou have not typed a temperature unit, Please run the program again.")
    run_again = input("\nDo you want to run the program again?(yes or no)")
    strip_of_run_again = run_again.strip()
    if strip_of_run_again.upper() == "YES":
        pass
    else:
        print("Thanks for use.")
        break
