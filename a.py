month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def total_days(year: int, month: int, day: int) -> int:
    """Считает общее количество дней с начала отчета."""
    days_from_years = (year - 1) * 365
    days_from_months = sum(month_days[m] for m in range(1, month))
    return days_from_years + days_from_months + day


def time_to_seconds(hour: int, minute: int, second: int) -> int:
    """Переводит время в секунды."""
    return hour * 3600 + minute * 60 + second


def lizard_duration(start_date: list[int], end_date: list[int]) -> tuple[int, int]:
    """Подсчитывает сколько дней и секунд жили ящерицы."""
    year1, month1, day1, hour1, min1, sec1 = start_date
    year2, month2, day2, hour2, min2, sec2 = end_date

    start_days = total_days(year1, month1, day1)
    end_days = total_days(year2, month2, day2)

    day_difference = end_days - start_days

    start_seconds = time_to_seconds(hour1, min1, sec1)
    end_seconds = time_to_seconds(hour2, min2, sec2)

    # если прошел не полный день
    if end_seconds < start_seconds:
        day_difference -= 1
        seconds_difference = (24 * 3600 - start_seconds) + end_seconds
    else:
        seconds_difference = end_seconds - start_seconds

    return day_difference, seconds_difference


if __name__ == "__main__":
    # start_date = [1001, 5, 20, 14, 15, 16]
    # end_date = [9009, 9, 11, 12, 21, 11]

    start_date = list(map(int, input().split()))
    end_date = list(map(int, input().split()))
    days, seconds = lizard_duration(start_date, end_date)
    print(days, seconds)
