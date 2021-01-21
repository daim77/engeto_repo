from datetime import datetime as dt


def day_today():
    ts1 = dt.now()
    return ts1.strftime('%Y-%b-%d %H:%M:%S')


if __name__ == '__main__':
    print(day_today())
    print(__name__)
