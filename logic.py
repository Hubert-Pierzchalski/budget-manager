import database as db
import matplotlib.pyplot as plt
import datetime


def repair_month(time):   # This function is used just in case someone writes for example '6' instead of '06' as a month consequances of this problem are visible mcuh later

    try:
        time = time.split("-")
        time[1] = int(time[1])
        if time[1] < 10:
            time[1] = f"0{time[1]}"
        time = "-".join(time)
        return time
    except TypeError:
        print("Incorrect data format, should be YYYY-MM-DD, please check if u entered dash between the numbers")
        return False

def checkdate(date):

    date_format = '%Y-%m-%d'

    try:
        datetime.datetime.strptime(date, date_format)

        return True

    except ValueError or  TypeError:

        print("Incorrect data please check if u entered right numbers")
        return False


def monthperiod(month, year):
        
    if month >= 1 and month < 9:
        month_start = f"0{month}"
        month_end = f"0{month + 1}"
        date_start = f'{year}-{month_start}-01'
        date_end = f'{year}-{month_end}-01'
        return date_start, date_end
    elif month == 9:
        month_start = f"0{month}"
        month_end = f"{10}"
        date_start = f'{year}-{month_start}-01'
        date_end = f'{year}-{month_end}-01'
        return date_start, date_end
    elif month >= 10 and month < 12:
        month_start = f"{month}"
        month_end = f"{month + 1}"
        date_start = f'{year}-{month_start}-01'
        date_end = f'{year}-{month_end}-01'
        return date_start, date_end
    elif month == 12:
        month_start = f"12"
        month_end = f"01"
        date_start = f'{year}-{month_start}-01'
        date_end = f'{year+1}-{month_end}-01'
        return date_start, date_end
    else:
        print("Incorrect data please check if you entered everything correctly")
        return 0, 0


def plot(date_start, date_end):

    y, x_values = db.graphdata(date_start, date_end)
    y_values = []
    result = db.balance_until(date_start)

    for item in y:
        result += item
        y_values.append(result)

    fig = plt.figure().set_figwidth(14)
    plt.plot(x_values, y_values)
    plt.title(f"Total balance show in period between {date_start} and {date_end}")
    plt.xlabel("date")
    plt.ylabel(f"balance")
    return fig

def which_date_greater(date_start, date_end):

    date_format = '%Y-%m-%d'

    date_obj1 = datetime.datetime.strptime(date_start, date_format)
    date_obj2 = datetime.datetime.strptime(date_end, date_format)

    if date_obj1 > date_obj2:
        print(f"It is not possible to search for data from later date {date_obj2} to earlier date {date_obj1},so i changed their places. ")
        date_obj1 = date_end
        date_obj2 = date_start
        return date_obj2, date_obj1
    elif date_obj2 == date_obj1:
        date_obj2 = date_obj2 + datetime.timedelta(days=1)
        return date_obj1, date_obj2
    else:
        return date_obj1, date_obj2
    