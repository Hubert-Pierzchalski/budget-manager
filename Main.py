import database as db
import logic as lg
import matplotlib.pyplot as plt
import iban as ib


def commands():
    print(f'\n\nlist of commands:\n'
          f'income -- Write your income from given day.\n'
          f'expense -- Write your expense from given.\n'
          f'balance -- Check your current balance.\n'
          f'history transaction -- Check your history of incomes and expanses and change of total balance from given time period.\n'
          f'monthly balance -- Check your balance of income and expanses from the given month\n'
          f'monthly summary -- Check your history of incomes and expanses and change of total balance from given month\n'
          f'transfer -- Check validity of received IBAN number and/or add it to your history account\n'
          f'stop -- stops porgram.\n')


def main():
    db.create_history_balance()
    commands()
    while True:
        command = input('\n\nWhat would you like to do?: ').lower()
        command = command.strip()
        match command:
            case 'income':
                print("If you are done with entering your data instead of saying your income just type 'stop'")
                while True:
                    try:

                        income = input("Please enter your income: ")
                        if income == "stop":
                            break
                        else:
                            income = abs(float(income))
                            datestamp = input("Please enter date of your transaction (YYYY-MM-DD): ")
                            date = lg.repair_month(datestamp)
                            if lg.checkdate(date):
                                description = input("Please enter description of transaction: ")
                                db.insert(income, date, description)

                    except ValueError:
                        print("Please enter a rational number")

            case 'expense':
                print("If you are done with entering your data instead of saying your expanse just type 'stop'")
                while True:
                    try:

                        expense = input("Please enter your expense: ")
                        if expense == "stop":
                            break
                        else:
                            expense = abs(float(expense)) * -1
                            datestamp = input("Please enter date of your transaction (YYYY-MM-DD): ")
                            date = lg.repair_month(datestamp)
                            if lg.checkdate(date):
                                description = input("Please enter description of transaction: ")
                                db.insert(expense, date, description)
                            else:
                                print("Invalid date please try again\n")

                    except ValueError:
                        print("Please enter a rational number")

            case 'balance':
                value = (str(db.showbalance()).replace("[", "").replace("(", "").replace(",", "").replace(")", "").replace("]", ""))
                print(f"Your current balance is : {value}")

            case 'history transaction':
                while True:
                    date_from = str(input("Please enter date (YYYY-MM-DD) from which you want to check your history "
                                          "transaction: "))
                    if lg.checkdate(date_from):
                        date_to = str(input("Please enter date (YYYY-MM-DD) to which you want to check your history "
                                            "transaction: "))
                        if lg.checkdate(date_to):
                            date_from, date_to = lg.which_date_greater(date_from,date_to)
                            print(f"Your history of transactions looks as follow")
                            for item in db.showtimeperiod(date_from, date_to):
                                print(item)
                            print("Your total balance in given date range looks as follow")
                            lg.plot(date_from, date_to)
                            plt.show()
                            break

            case 'monthly balance':
                while True:
                    year = int(input("Please enter year from which you want to see transactions: "))
                    month = int(input("Please enter month from which you want to see transactions: "))
                    date_from, date_to = lg.monthperiod(month, year)
                    if date_from != 0:
                        break
                    else:
                        pass
                balance = (str(db.summaryofmonth(date_from, date_to)).replace("[", "").replace("(", "").replace(",", "").replace(")", "").replace("]", ""))
                print(f"Your balance in given month was : {balance}")

            case 'monthly summary': 
                while True:
                    year = int(input("Please enter year from which you want to see transactions: "))
                    month = int(input("Please enter month from which you want to see transactions: "))
                    date_from, date_to = lg.monthperiod(month, year)
                    if date_from != 0:
                        break
                    else:
                        pass
                print(f"Your history of transactions looks as follow")
                for item in db.showtimeperiod(date_from, date_to):
                    print(item)
                print("Your total balance in given date range looks as follow")
                lg.plot(date_from, date_to)
                plt.show()

            case 'stop':
                db.close()
                break

            case 'transfer':
                iban_number = str(input("Please enter iban number: "))
                if ib.check_iban(iban_number):
                    print("This IBAN is valid")

                    while True:

                        order = input(
                            "Would you like to enter this to your transaction history?\n Type in 'yes' or 'no'\n ").lower()
                        order = order.strip()

                        match order:
                            case "yes":

                                try:

                                    expense = input("Please enter your expense: ")
                                    if expense == "stop":
                                        break
                                    else:
                                        expense = abs(float(expense)) * -1
                                        datestamp = input("Please enter date of your transaction (YYYY-MM-DD): ")
                                        if lg.checkdate(datestamp):
                                            description = input("Please enter description of transaction: ")
                                            description = description + f" --> Transaction to account: {iban_number}"
                                            db.insert(expense, datestamp, description)
                                        else:
                                            print("Invalid date please try again\n")
                                        break

                                except ValueError:
                                    print("Please enter a rational number")

                            case "no":
                                break
                            case _:
                                print("Just type yes or no\n\n")
                else:
                    print("This IBAN is not valid")

            case 'help':
                commands()

            case _:
                print("Invalid input please check if you entered correct input\n If you forget what other commands are just type in 'help'")


if __name__ == '__main__':
    main()
