import calendar
import datetime

import pandas

# days range approximate
ONE_YEAR_DATA_RANGE = 250
TWO_YEAR_DATA_RANGE = 500
THREE_YEAR_DATA_RANGE = 750
FOUR_YEAR_DATA_RANGE = 1000
FIVE_YEAR_DATA_RANGE = 1250
SEVEN_YEAR_DATA_RANGE = 1750
TEN_YEAR_DATA_RANGE = 2500
FIFTEEN_YEAR_DATA_RANGE = 3750
TWENTY_YEAR_DATA_RANGE = 5000
TWENTY_FIVE_YEAR_DATA_RANGE = 7500
# csv column indexes
OPEN = 1
HIGH = 2
LOW = 3
CLOSE = 4
DATE = 0
THURSDAY = '4'
FRIDAY = '5'
MONDAY = '1'
TUESDAY = '2'
WEDNESDAY = '3'

formatted_data = pandas.read_csv("nifty.csv").to_numpy()

# daily counters
under_1 = 0
under_2 = 0
under_3 = 0
under_4 = 0
under_5 = 0
under_7point5 = 0
under_10 = 0
above_10 = 0
monday_total = 0
tuesday_total = 0
wednesday_total = 0
friday_total = 0

# weekly counters
weekly_thursday_under_1 = 0
weekly_thursday_under_2 = 0
weekly_thursday_under_3 = 0
weekly_thursday_under_4 = 0
weekly_thursday_under_5 = 0
weekly_thursday_under_6 = 0
weekly_thursday_under_7 = 0
weekly_thursday_under_8 = 0
weekly_thursday_under_10 = 0
weekly_thursday_under_15 = 0
weekly_thursday_above_15 = 0

weekly_friday_to_thursday_under_1 = 0
weekly_friday_to_thursday_under_2 = 0
weekly_friday_to_thursday_under_3 = 0
weekly_friday_to_thursday_under_4 = 0
weekly_friday_to_thursday_under_5 = 0
weekly_friday_to_thursday_under_6 = 0
weekly_friday_to_thursday_under_7 = 0
weekly_friday_to_thursday_under_8 = 0
weekly_friday_to_thursday_under_10 = 0
weekly_friday_to_thursday_under_15 = 0
weekly_friday_to_thursday_above_15 = 0

weekly_monday_to_thursday_under_1 = 0
weekly_monday_to_thursday_under_2 = 0
weekly_monday_to_thursday_under_3 = 0
weekly_monday_to_thursday_under_4 = 0
weekly_monday_to_thursday_under_5 = 0
weekly_monday_to_thursday_under_6 = 0
weekly_monday_to_thursday_under_7 = 0
weekly_monday_to_thursday_under_8 = 0
weekly_monday_to_thursday_under_10 = 0
weekly_monday_to_thursday_under_15 = 0
weekly_monday_to_thursday_above_15 = 0

weekly_wednesday_to_thursday_under_1 = 0
weekly_wednesday_to_thursday_under_2 = 0
weekly_wednesday_to_thursday_under_3 = 0
weekly_wednesday_to_thursday_under_4 = 0
weekly_wednesday_to_thursday_under_5 = 0
weekly_wednesday_to_thursday_under_6 = 0
weekly_wednesday_to_thursday_under_7 = 0
weekly_wednesday_to_thursday_under_8 = 0
weekly_wednesday_to_thursday_under_10 = 0
weekly_wednesday_to_thursday_under_15 = 0
weekly_wednesday_to_thursday_above_15 = 0

weekly_tuesday_to_thursday_under_1 = 0
weekly_tuesday_to_thursday_under_2 = 0
weekly_tuesday_to_thursday_under_3 = 0
weekly_tuesday_to_thursday_under_4 = 0
weekly_tuesday_to_thursday_under_5 = 0
weekly_tuesday_to_thursday_under_6 = 0
weekly_tuesday_to_thursday_under_7 = 0
weekly_tuesday_to_thursday_under_8 = 0
weekly_tuesday_to_thursday_under_10 = 0
weekly_tuesday_to_thursday_under_15 = 0
weekly_tuesday_to_thursday_above_15 = 0

weekly_open_to_low_under_1 = 0
weekly_open_to_low_under_2 = 0
weekly_open_to_low_under_3 = 0
weekly_open_to_low_under_4 = 0
weekly_open_to_low_under_5 = 0
weekly_open_to_low_under_6 = 0
weekly_open_to_low_under_7 = 0
weekly_open_to_low_under_8 = 0
weekly_open_to_low_under_10 = 0
weekly_open_to_low_under_15 = 0
weekly_open_to_low_above_15 = 0

weekly_open_to_high_under_1 = 0
weekly_open_to_high_under_2 = 0
weekly_open_to_high_under_3 = 0
weekly_open_to_high_under_4 = 0
weekly_open_to_high_under_5 = 0
weekly_open_to_high_under_6 = 0
weekly_open_to_high_under_7 = 0
weekly_open_to_high_under_8 = 0
weekly_open_to_high_under_10 = 0
weekly_open_to_high_under_15 = 0
weekly_open_to_high_above_15 = 0

# monthly counters
monthly_thursday_under_2 = 0
monthly_thursday_under_4 = 0
monthly_thursday_under_6 = 0
monthly_thursday_under_8 = 0
monthly_thursday_under_10 = 0
monthly_thursday_under_12 = 0
monthly_thursday_under_14 = 0
monthly_thursday_under_16 = 0
monthly_thursday_under_18 = 0
monthly_thursday_under_20 = 0
monthly_thursday_above_20 = 0

monthly_open_to_high_under_2 = 0
monthly_open_to_high_under_4 = 0
monthly_open_to_high_under_6 = 0
monthly_open_to_high_under_8 = 0
monthly_open_to_high_under_10 = 0
monthly_open_to_high_under_12 = 0
monthly_open_to_high_under_14 = 0
monthly_open_to_high_under_16 = 0
monthly_open_to_high_under_18 = 0
monthly_open_to_high_under_20 = 0
monthly_open_to_high_above_20 = 0

monthly_open_to_low_under_2 = 0
monthly_open_to_low_under_4 = 0
monthly_open_to_low_under_6 = 0
monthly_open_to_low_under_8 = 0
monthly_open_to_low_under_10 = 0
monthly_open_to_low_under_12 = 0
monthly_open_to_low_under_14 = 0
monthly_open_to_low_under_16 = 0
monthly_open_to_low_under_18 = 0
monthly_open_to_low_under_20 = 0
monthly_open_to_low_above_20 = 0

weekly_close = []
monthly_expiry_dates = []
monthly_close = []
weekly_highs = []
weekly_lows = []
monthly_highs = []
monthly_lows = []

daily_sum = 0
weekly_sum = 0
tuesday_sum = 0
wednesday_sum = 0
friday_sum = 0
monday_sum = 0
monthly_sum = 0


def increment_daily_counters(diff):
    global under_1, under_2, under_3, under_4, under_5, under_7point5, under_10, above_10, daily_sum
    daily_sum = daily_sum + abs(diff * 100)
    if abs(diff * 100) < 1:
        under_1 = under_1 + 1
    elif abs(diff * 100) < 2:
        under_2 = under_2 + 1
    elif abs(diff * 100) < 3:
        under_3 = under_3 + 1
    elif abs(diff * 100) < 4:
        under_4 = under_4 + 1
    elif abs(diff * 100) < 5:
        under_5 = under_5 + 1
    elif abs(diff * 100) < 7.5:
        under_7point5 = under_7point5 + 1
    elif abs(diff * 100) < 10:
        under_10 = under_10 + 1
    else:
        above_10 = above_10 + 1


def increment_weekly_counters(diff):
    global weekly_thursday_under_1, weekly_thursday_under_2, weekly_thursday_under_3, weekly_thursday_under_4, \
        weekly_thursday_under_5, weekly_thursday_under_6, weekly_thursday_under_7, weekly_sum, \
        weekly_thursday_under_8, weekly_thursday_under_10, weekly_thursday_under_15, weekly_thursday_above_15
    weekly_sum = weekly_sum + abs(diff * 100)
    if abs(diff * 100) < 1:
        weekly_thursday_under_1 = weekly_thursday_under_1 + 1
    elif abs(diff * 100) < 2:
        weekly_thursday_under_2 = weekly_thursday_under_2 + 1
    elif abs(diff * 100) < 3:
        weekly_thursday_under_3 = weekly_thursday_under_3 + 1
    elif abs(diff * 100) < 4:
        weekly_thursday_under_4 = weekly_thursday_under_4 + 1
    elif abs(diff * 100) < 5:
        weekly_thursday_under_5 = weekly_thursday_under_5 + 1
    elif abs(diff * 100) < 6:
        weekly_thursday_under_6 = weekly_thursday_under_6 + 1
    elif abs(diff * 100) < 7:
        weekly_thursday_under_7 = weekly_thursday_under_7 + 1
    elif abs(diff * 100) < 8:
        weekly_thursday_under_8 = weekly_thursday_under_8 + 1
    elif abs(diff * 100) < 10:
        weekly_thursday_under_10 = weekly_thursday_under_10 + 1
    elif abs(diff * 100) < 15:
        weekly_thursday_under_15 = weekly_thursday_under_15 + 1
    else:
        weekly_thursday_above_15 = weekly_thursday_above_15 + 1


def increment_tuesday_to_thursday_counters(diff):
    global weekly_tuesday_to_thursday_under_1, weekly_tuesday_to_thursday_under_2, weekly_tuesday_to_thursday_under_3, weekly_tuesday_to_thursday_under_4, \
        weekly_tuesday_to_thursday_under_5, weekly_tuesday_to_thursday_under_6, weekly_tuesday_to_thursday_under_7, tuesday_sum, \
        weekly_tuesday_to_thursday_under_8, weekly_tuesday_to_thursday_under_10, weekly_tuesday_to_thursday_under_15, weekly_tuesday_to_thursday_above_15
    tuesday_sum = tuesday_sum + abs(diff * 100)
    if abs(diff * 100) < 1:
        weekly_tuesday_to_thursday_under_1 = weekly_tuesday_to_thursday_under_1 + 1
    elif abs(diff * 100) < 2:
        weekly_tuesday_to_thursday_under_2 = weekly_tuesday_to_thursday_under_2 + 1
    elif abs(diff * 100) < 3:
        weekly_tuesday_to_thursday_under_3 = weekly_tuesday_to_thursday_under_3 + 1
    elif abs(diff * 100) < 4:
        weekly_tuesday_to_thursday_under_4 = weekly_tuesday_to_thursday_under_4 + 1
    elif abs(diff * 100) < 5:
        weekly_tuesday_to_thursday_under_5 = weekly_tuesday_to_thursday_under_5 + 1
    elif abs(diff * 100) < 6:
        weekly_tuesday_to_thursday_under_6 = weekly_tuesday_to_thursday_under_6 + 1
    elif abs(diff * 100) < 7:
        weekly_tuesday_to_thursday_under_7 = weekly_tuesday_to_thursday_under_7 + 1
    elif abs(diff * 100) < 8:
        weekly_tuesday_to_thursday_under_8 = weekly_tuesday_to_thursday_under_8 + 1
    elif abs(diff * 100) < 10:
        weekly_tuesday_to_thursday_under_10 = weekly_tuesday_to_thursday_under_10 + 1
    elif abs(diff * 100) < 15:
        weekly_tuesday_to_thursday_under_15 = weekly_tuesday_to_thursday_under_15 + 1
    else:
        weekly_tuesday_to_thursday_above_15 = weekly_tuesday_to_thursday_above_15 + 1


def increment_friday_to_thursday_counters(diff):
    global weekly_friday_to_thursday_under_1, weekly_friday_to_thursday_under_2, weekly_friday_to_thursday_under_3, weekly_friday_to_thursday_under_4, \
        weekly_friday_to_thursday_under_5, weekly_friday_to_thursday_under_6, weekly_friday_to_thursday_under_7, friday_sum, \
        weekly_friday_to_thursday_under_8, weekly_friday_to_thursday_under_10, weekly_friday_to_thursday_under_15, weekly_friday_to_thursday_above_15
    friday_sum = friday_sum + abs(diff * 100)
    if abs(diff * 100) < 1:
        weekly_friday_to_thursday_under_1 = weekly_friday_to_thursday_under_1 + 1
    elif abs(diff * 100) < 2:
        weekly_friday_to_thursday_under_2 = weekly_friday_to_thursday_under_2 + 1
    elif abs(diff * 100) < 3:
        weekly_friday_to_thursday_under_3 = weekly_friday_to_thursday_under_3 + 1
    elif abs(diff * 100) < 4:
        weekly_friday_to_thursday_under_4 = weekly_friday_to_thursday_under_4 + 1
    elif abs(diff * 100) < 5:
        weekly_friday_to_thursday_under_5 = weekly_friday_to_thursday_under_5 + 1
    elif abs(diff * 100) < 6:
        weekly_friday_to_thursday_under_6 = weekly_friday_to_thursday_under_6 + 1
    elif abs(diff * 100) < 7:
        weekly_friday_to_thursday_under_7 = weekly_friday_to_thursday_under_7 + 1
    elif abs(diff * 100) < 8:
        weekly_friday_to_thursday_under_8 = weekly_friday_to_thursday_under_8 + 1
    elif abs(diff * 100) < 10:
        weekly_friday_to_thursday_under_10 = weekly_friday_to_thursday_under_10 + 1
    elif abs(diff * 100) < 15:
        weekly_friday_to_thursday_under_15 = weekly_friday_to_thursday_under_15 + 1
    else:
        weekly_friday_to_thursday_above_15 = weekly_friday_to_thursday_above_15 + 1


def increment_wednesday_to_thursday_counters(diff):
    global weekly_wednesday_to_thursday_under_1, wednesday_sum, weekly_wednesday_to_thursday_under_2, weekly_wednesday_to_thursday_under_3, weekly_wednesday_to_thursday_under_4, \
        weekly_wednesday_to_thursday_under_5, weekly_wednesday_to_thursday_under_6, weekly_wednesday_to_thursday_under_7, \
        weekly_wednesday_to_thursday_under_8, weekly_wednesday_to_thursday_under_10, weekly_wednesday_to_thursday_under_15, weekly_wednesday_to_thursday_above_15
    wednesday_sum = wednesday_sum + abs(diff * 100)
    if abs(diff * 100) < 1:
        weekly_wednesday_to_thursday_under_1 = weekly_wednesday_to_thursday_under_1 + 1
    elif abs(diff * 100) < 2:
        weekly_wednesday_to_thursday_under_2 = weekly_wednesday_to_thursday_under_2 + 1
    elif abs(diff * 100) < 3:
        weekly_wednesday_to_thursday_under_3 = weekly_wednesday_to_thursday_under_3 + 1
    elif abs(diff * 100) < 4:
        weekly_wednesday_to_thursday_under_4 = weekly_wednesday_to_thursday_under_4 + 1
    elif abs(diff * 100) < 5:
        weekly_wednesday_to_thursday_under_5 = weekly_wednesday_to_thursday_under_5 + 1
    elif abs(diff * 100) < 6:
        weekly_wednesday_to_thursday_under_6 = weekly_wednesday_to_thursday_under_6 + 1
    elif abs(diff * 100) < 7:
        weekly_wednesday_to_thursday_under_7 = weekly_wednesday_to_thursday_under_7 + 1
    elif abs(diff * 100) < 8:
        weekly_wednesday_to_thursday_under_8 = weekly_wednesday_to_thursday_under_8 + 1
    elif abs(diff * 100) < 10:
        weekly_wednesday_to_thursday_under_10 = weekly_wednesday_to_thursday_under_10 + 1
    elif abs(diff * 100) < 15:
        weekly_wednesday_to_thursday_under_15 = weekly_wednesday_to_thursday_under_15 + 1
    else:
        weekly_wednesday_to_thursday_above_15 = weekly_wednesday_to_thursday_above_15 + 1


def increment_monday_to_thursday_counters(diff):
    global weekly_monday_to_thursday_under_1, monday_sum, weekly_monday_to_thursday_under_2, weekly_monday_to_thursday_under_3, weekly_monday_to_thursday_under_4, \
        weekly_monday_to_thursday_under_5, weekly_monday_to_thursday_under_6, weekly_monday_to_thursday_under_7, \
        weekly_monday_to_thursday_under_8, weekly_monday_to_thursday_under_10, weekly_monday_to_thursday_under_15, weekly_monday_to_thursday_above_15
    monday_sum = monday_sum + abs(diff * 100)
    if abs(diff * 100) < 1:
        weekly_monday_to_thursday_under_1 = weekly_monday_to_thursday_under_1 + 1
    elif abs(diff * 100) < 2:
        weekly_monday_to_thursday_under_2 = weekly_monday_to_thursday_under_2 + 1
    elif abs(diff * 100) < 3:
        weekly_monday_to_thursday_under_3 = weekly_monday_to_thursday_under_3 + 1
    elif abs(diff * 100) < 4:
        weekly_monday_to_thursday_under_4 = weekly_monday_to_thursday_under_4 + 1
    elif abs(diff * 100) < 5:
        weekly_monday_to_thursday_under_5 = weekly_monday_to_thursday_under_5 + 1
    elif abs(diff * 100) < 6:
        weekly_monday_to_thursday_under_6 = weekly_monday_to_thursday_under_6 + 1
    elif abs(diff * 100) < 7:
        weekly_monday_to_thursday_under_7 = weekly_monday_to_thursday_under_7 + 1
    elif abs(diff * 100) < 8:
        weekly_monday_to_thursday_under_8 = weekly_monday_to_thursday_under_8 + 1
    elif abs(diff * 100) < 10:
        weekly_monday_to_thursday_under_10 = weekly_monday_to_thursday_under_10 + 1
    elif abs(diff * 100) < 15:
        weekly_monday_to_thursday_under_15 = weekly_monday_to_thursday_under_15 + 1
    else:
        weekly_monday_to_thursday_above_15 = weekly_monday_to_thursday_above_15 + 1


def increment_weekly_open_to_low_counters(diff):
    global weekly_open_to_low_under_1, weekly_open_to_low_under_2, weekly_open_to_low_under_3, weekly_open_to_low_under_4, \
        weekly_open_to_low_under_5, weekly_open_to_low_under_6, weekly_open_to_low_under_7, \
        weekly_open_to_low_under_8, weekly_open_to_low_under_10, weekly_open_to_low_under_15, weekly_open_to_low_above_15
    if abs(diff * 100) < 1:
        weekly_open_to_low_under_1 = weekly_open_to_low_under_1 + 1
    elif abs(diff * 100) < 2:
        weekly_open_to_low_under_2 = weekly_open_to_low_under_2 + 1
    elif abs(diff * 100) < 3:
        weekly_open_to_low_under_3 = weekly_open_to_low_under_3 + 1
    elif abs(diff * 100) < 4:
        weekly_open_to_low_under_4 = weekly_open_to_low_under_4 + 1
    elif abs(diff * 100) < 5:
        weekly_open_to_low_under_5 = weekly_open_to_low_under_5 + 1
    elif abs(diff * 100) < 6:
        weekly_open_to_low_under_6 = weekly_open_to_low_under_6 + 1
    elif abs(diff * 100) < 7:
        weekly_open_to_low_under_7 = weekly_open_to_low_under_7 + 1
    elif abs(diff * 100) < 8:
        weekly_open_to_low_under_8 = weekly_open_to_low_under_8 + 1
    elif abs(diff * 100) < 10:
        weekly_open_to_low_under_10 = weekly_open_to_low_under_10 + 1
    elif abs(diff * 100) < 15:
        weekly_open_to_low_under_15 = weekly_open_to_low_under_15 + 1
    else:
        weekly_open_to_low_above_15 = weekly_open_to_low_above_15 + 1


def increment_weekly_open_to_high_counters(diff):
    global weekly_open_to_high_under_1, weekly_open_to_high_under_2, weekly_open_to_high_under_3, weekly_open_to_high_under_4, \
        weekly_open_to_high_under_5, weekly_open_to_high_under_6, weekly_open_to_high_under_7, \
        weekly_open_to_high_under_8, weekly_open_to_high_under_10, weekly_open_to_high_under_15, weekly_open_to_high_above_15
    if abs(diff * 100) < 1:
        weekly_open_to_high_under_1 = weekly_open_to_high_under_1 + 1
    elif abs(diff * 100) < 2:
        weekly_open_to_high_under_2 = weekly_open_to_high_under_2 + 1
    elif abs(diff * 100) < 3:
        weekly_open_to_high_under_3 = weekly_open_to_high_under_3 + 1
    elif abs(diff * 100) < 4:
        weekly_open_to_high_under_4 = weekly_open_to_high_under_4 + 1
    elif abs(diff * 100) < 5:
        weekly_open_to_high_under_5 = weekly_open_to_high_under_5 + 1
    elif abs(diff * 100) < 6:
        weekly_open_to_high_under_6 = weekly_open_to_high_under_6 + 1
    elif abs(diff * 100) < 7:
        weekly_open_to_high_under_7 = weekly_open_to_high_under_7 + 1
    elif abs(diff * 100) < 8:
        weekly_open_to_high_under_8 = weekly_open_to_high_under_8 + 1
    elif abs(diff * 100) < 10:
        weekly_open_to_high_under_10 = weekly_open_to_high_under_10 + 1
    elif abs(diff * 100) < 15:
        weekly_open_to_high_under_15 = weekly_open_to_high_under_15 + 1
    else:
        weekly_open_to_high_above_15 = weekly_open_to_high_above_15 + 1


def increment_monthly_counters(diff):
    global monthly_thursday_under_4, monthly_thursday_under_2, monthly_thursday_under_6, monthly_thursday_under_4, \
        monthly_thursday_under_8, monthly_thursday_under_12, monthly_thursday_under_10, monthly_thursday_under_18, \
        monthly_thursday_under_14, monthly_thursday_under_20, monthly_thursday_under_16, monthly_thursday_above_20, monthly_sum
    monthly_sum = monthly_sum + abs(diff * 100)
    if abs(diff * 100) < 2:
        monthly_thursday_under_2 = monthly_thursday_under_2 + 1
    elif abs(diff * 100) < 4:
        monthly_thursday_under_4 = monthly_thursday_under_4 + 1
    elif abs(diff * 100) < 6:
        monthly_thursday_under_6 = monthly_thursday_under_6 + 1
    elif abs(diff * 100) < 8:
        monthly_thursday_under_8 = monthly_thursday_under_8 + 1
    elif abs(diff * 100) < 10:
        monthly_thursday_under_10 = monthly_thursday_under_10 + 1
    elif abs(diff * 100) < 12:
        monthly_thursday_under_12 = monthly_thursday_under_12 + 1
    elif abs(diff * 100) < 14:
        monthly_thursday_under_14 = monthly_thursday_under_14 + 1
    elif abs(diff * 100) < 16:
        monthly_thursday_under_16 = monthly_thursday_under_16 + 1
    elif abs(diff * 100) < 18:
        monthly_thursday_under_18 = monthly_thursday_under_18 + 1
    elif abs(diff * 100) < 20:
        monthly_thursday_under_20 = monthly_thursday_under_20 + 1
    else:
        monthly_thursday_above_20 = monthly_thursday_above_20 + 1


def increment_monthly_open_to_high_counters(diff):
    global monthly_open_to_high_under_4, monthly_open_to_high_under_2, monthly_open_to_high_under_6, monthly_open_to_high_under_4, \
        monthly_open_to_high_under_8, monthly_open_to_high_under_12, monthly_open_to_high_under_10, monthly_open_to_high_under_18, \
        monthly_open_to_high_under_14, monthly_open_to_high_under_20, monthly_open_to_high_under_16, monthly_open_to_high_above_20

    if abs(diff * 100) < 2:
        monthly_open_to_high_under_2 = monthly_open_to_high_under_2 + 1
    elif abs(diff * 100) < 4:
        monthly_open_to_high_under_4 = monthly_open_to_high_under_4 + 1
    elif abs(diff * 100) < 6:
        monthly_open_to_high_under_6 = monthly_open_to_high_under_6 + 1
    elif abs(diff * 100) < 8:
        monthly_open_to_high_under_8 = monthly_open_to_high_under_8 + 1
    elif abs(diff * 100) < 10:
        monthly_open_to_high_under_10 = monthly_open_to_high_under_10 + 1
    elif abs(diff * 100) < 12:
        monthly_open_to_high_under_12 = monthly_open_to_high_under_12 + 1
    elif abs(diff * 100) < 14:
        monthly_open_to_high_under_14 = monthly_open_to_high_under_14 + 1
    elif abs(diff * 100) < 16:
        monthly_open_to_high_under_16 = monthly_open_to_high_under_16 + 1
    elif abs(diff * 100) < 18:
        monthly_open_to_high_under_18 = monthly_open_to_high_under_18 + 1
    elif abs(diff * 100) < 20:
        monthly_open_to_high_under_20 = monthly_open_to_high_under_20 + 1
    else:
        monthly_open_to_high_above_20 = monthly_open_to_high_above_20 + 1


def increment_monthly_open_to_low_counters(diff):
    global monthly_open_to_low_under_4, monthly_open_to_low_under_2, monthly_open_to_low_under_6, monthly_open_to_low_under_4, \
        monthly_open_to_low_under_8, monthly_open_to_low_under_12, monthly_open_to_low_under_10, monthly_open_to_low_under_18, \
        monthly_open_to_low_under_14, monthly_open_to_low_under_20, monthly_open_to_low_under_16, monthly_open_to_low_above_20

    if abs(diff * 100) < 2:
        monthly_open_to_low_under_2 = monthly_open_to_low_under_2 + 1
    elif abs(diff * 100) < 4:
        monthly_open_to_low_under_4 = monthly_open_to_low_under_4 + 1
    elif abs(diff * 100) < 6:
        monthly_open_to_low_under_6 = monthly_open_to_low_under_6 + 1
    elif abs(diff * 100) < 8:
        monthly_open_to_low_under_8 = monthly_open_to_low_under_8 + 1
    elif abs(diff * 100) < 10:
        monthly_open_to_low_under_10 = monthly_open_to_low_under_10 + 1
    elif abs(diff * 100) < 12:
        monthly_open_to_low_under_12 = monthly_open_to_low_under_12 + 1
    elif abs(diff * 100) < 14:
        monthly_open_to_low_under_14 = monthly_open_to_low_under_14 + 1
    elif abs(diff * 100) < 16:
        monthly_open_to_low_under_16 = monthly_open_to_low_under_16 + 1
    elif abs(diff * 100) < 18:
        monthly_open_to_low_under_18 = monthly_open_to_low_under_18 + 1
    elif abs(diff * 100) < 20:
        monthly_open_to_low_under_20 = monthly_open_to_low_under_20 + 1
    else:
        monthly_open_to_low_above_20 = monthly_open_to_low_above_20 + 1


def find_last_thursday_in_month(year, month):
    dt = datetime.date(year, month, calendar.monthrange(year, month)[1])
    offset = 4 - datetime.date(year, month, calendar.monthrange(year, month)[1]).isoweekday()
    if offset > 0:
        offset -= 7
    dt += datetime.timedelta(offset)
    return dt


# loop to initiate monthly expiry dates
for year in range(1980, 2022):
    for month in range(1, 13):
        monthly_expiry_dates.append(find_last_thursday_in_month(year, month).strftime('%d %b %Y'))

weekly_high = 0
weekly_low = 50000
monthly_high = 0
monthly_low = 50000
monday = 0
tuesday = 0
wednesday = 0
friday = 0

# loop to analyse complete data range
for i in range(0, TWENTY_YEAR_DATA_RANGE):
    # logic to calculate daily change %
    increment_daily_counters((formatted_data[i][CLOSE] - formatted_data[i + 1][CLOSE]) / formatted_data[i + 1][CLOSE])
    if formatted_data[i][LOW] < weekly_low:
        weekly_low = formatted_data[i][LOW]
    if formatted_data[i][HIGH] > weekly_high:
        weekly_high = formatted_data[i][HIGH]
    if formatted_data[i][LOW] < monthly_low:
        monthly_low = formatted_data[i][LOW]
    if formatted_data[i][HIGH] > monthly_high:
        monthly_high = formatted_data[i][HIGH]
    # setting weekday close values
    if (datetime.datetime.strptime(formatted_data[i][DATE], '%d %b %Y').strftime('%w')) == MONDAY:
        monday = formatted_data[i][CLOSE]
    if (datetime.datetime.strptime(formatted_data[i][DATE], '%d %b %Y').strftime('%w')) == TUESDAY:
        tuesday = formatted_data[i][CLOSE]
    if (datetime.datetime.strptime(formatted_data[i][DATE], '%d %b %Y').strftime('%w')) == WEDNESDAY:
        wednesday = formatted_data[i][CLOSE]
    if (datetime.datetime.strptime(formatted_data[i][DATE], '%d %b %Y').strftime('%w')) == FRIDAY:
        friday = formatted_data[i][CLOSE]

    # logic to calculate weekly change %
    if (datetime.datetime.strptime(formatted_data[i][DATE], '%d %b %Y').strftime('%w')) == THURSDAY:
        weekly_close.append(formatted_data[i][CLOSE])
        weekly_lows.append(weekly_low)
        weekly_highs.append(weekly_high)
        if len(weekly_close) > 1:
            if friday != 0:
                increment_friday_to_thursday_counters(
                    (weekly_close[len(weekly_close) - 2] - friday) / friday)
                friday = 0
                friday_total = friday_total + 1
            if monday != 0:
                increment_monday_to_thursday_counters((weekly_close[len(weekly_close) - 2] - monday) / monday)
                monday = 0
                monday_total = monday_total + 1
            if tuesday != 0:
                increment_tuesday_to_thursday_counters((weekly_close[len(weekly_close) - 2] - tuesday) / tuesday)
                tuesday = 0
                tuesday_total = tuesday_total + 1
            if wednesday != 0:
                increment_wednesday_to_thursday_counters((weekly_close[len(weekly_close) - 2] - wednesday) / wednesday)
                wednesday = 0
                wednesday_total = wednesday_total + 1
            increment_weekly_counters(
                (weekly_close[len(weekly_close) - 2] - weekly_close[len(weekly_close) - 1]) / \
                weekly_close[len(weekly_close) - 2])
            increment_weekly_open_to_low_counters(
                (weekly_close[len(weekly_close) - 2] - weekly_low) / weekly_close[len(weekly_close) - 2])
            increment_weekly_open_to_high_counters(
                (weekly_high - weekly_close[len(weekly_close) - 2]) / weekly_close[len(weekly_close) - 2])
        weekly_high = 0
        weekly_low = 50000
        # logic to calculate monthly change %
        if str(formatted_data[i][DATE]) in monthly_expiry_dates:
            monthly_close.append(formatted_data[i][CLOSE])
            monthly_lows.append(monthly_low)
            monthly_highs.append(monthly_high)
            if len(monthly_close) > 1:
                increment_monthly_counters(
                    (monthly_close[len(monthly_close) - 2] - monthly_close[len(monthly_close) - 1]) / \
                    monthly_close[len(monthly_close) - 2])
                increment_monthly_open_to_low_counters(
                    (monthly_close[len(monthly_close) - 2] - monthly_low) / monthly_close[len(monthly_close) - 2])
                increment_monthly_open_to_high_counters(
                    (monthly_high - monthly_close[len(monthly_close) - 2]) / monthly_close[len(monthly_close) - 2])
            monthly_high = 0
            monthly_low = 50000

total = TWENTY_YEAR_DATA_RANGE
print("------- DAILY CHANGE FOR PAST 20 YEARS-------- ")
print()
print("UNDER 1 = " + str("{:.2%}".format(under_1 / total)))
print("UNDER 2 = " + str("{:.2%}".format(under_2 / total)))
print("UNDER 3 = " + str("{:.2%}".format(under_3 / total)))
print("UNDER 4 = " + str("{:.2%}".format(under_4 / total)))
print("UNDER 5 = " + str("{:.2%}".format(under_5 / total)))
print("UNDER 7.5 = " + str("{:.2%}".format(under_7point5 / total)))
print("UNDER 10 = " + str("{:.2%}".format(under_10 / total)))
print("ABOVE 10 = " + str("{:.2%}".format(above_10 / total)))
print("SWEET SPOT UNDER 2 = " + str("{:.2%}".format(under_1 / total + under_2 / total)))
print("SWEET SPOT ABOVE 2 = " + str("{:.2%}".format(1 - (under_1 / total + under_2 / total))))
print()
print("------- WEEKLY CHANGE FOR PAST 20 YEARS-------- ")
print()
total = len(weekly_close)
print("UNDER 1 = " + str("{:.2%}".format(weekly_thursday_under_1 / total)))
print("UNDER 2 = " + str("{:.2%}".format(weekly_thursday_under_2 / total)))
print("UNDER 3 = " + str("{:.2%}".format(weekly_thursday_under_3 / total)))
print("UNDER 4 = " + str("{:.2%}".format(weekly_thursday_under_4 / total)))
print("UNDER 5 = " + str("{:.2%}".format(weekly_thursday_under_5 / total)))
print("UNDER 6 = " + str("{:.2%}".format(weekly_thursday_under_6 / total)))
print("UNDER 7 = " + str("{:.2%}".format(weekly_thursday_under_7 / total)))
print("UNDER 8 = " + str("{:.2%}".format(weekly_thursday_under_8 / total)))
print("UNDER 10 = " + str("{:.2%}".format(weekly_thursday_under_10 / total)))
print("UNDER 15 = " + str("{:.2%}".format(weekly_thursday_under_15 / total)))
print("ABOVE 15 = " + str("{:.2%}".format(weekly_thursday_above_15 / total)))
print("SWEET SPOT UNDER 5 = " + str("{:.2%}".format(weekly_thursday_under_1 / total + weekly_thursday_under_2 / total +
                                                    weekly_thursday_under_3 / total + weekly_thursday_under_4 / total +
                                                    weekly_thursday_under_5 / total)))
print("SWEET SPOT ABOVE 5 = " + str(
    "{:.2%}".format(1 - (weekly_thursday_under_1 / total + weekly_thursday_under_2 / total +
                         weekly_thursday_under_3 / total + weekly_thursday_under_4 / total +
                         weekly_thursday_under_5 / total))))
print()
print("------- MONDAY TO THURSDAY CHANGE FOR PAST 20 YEARS-------- ")
print()
total = monday_total
print("UNDER 1 = " + str("{:.2%}".format(weekly_monday_to_thursday_under_1 / total)))
print("UNDER 2 = " + str("{:.2%}".format(weekly_monday_to_thursday_under_2 / total)))
print("UNDER 3 = " + str("{:.2%}".format(weekly_monday_to_thursday_under_3 / total)))
print("UNDER 4 = " + str("{:.2%}".format(weekly_monday_to_thursday_under_4 / total)))
print("UNDER 5 = " + str("{:.2%}".format(weekly_monday_to_thursday_under_5 / total)))
print("UNDER 6 = " + str("{:.2%}".format(weekly_monday_to_thursday_under_6 / total)))
print("UNDER 7 = " + str("{:.2%}".format(weekly_monday_to_thursday_under_7 / total)))
print("UNDER 8 = " + str("{:.2%}".format(weekly_monday_to_thursday_under_8 / total)))
print("UNDER 10 = " + str("{:.2%}".format(weekly_monday_to_thursday_under_10 / total)))
print("UNDER 15 = " + str("{:.2%}".format(weekly_monday_to_thursday_under_15 / total)))
print("ABOVE 15 = " + str("{:.2%}".format(weekly_monday_to_thursday_above_15 / total)))
print("SWEET SPOT UNDER 4 = " + str(
    "{:.2%}".format(weekly_monday_to_thursday_under_1 / total + weekly_monday_to_thursday_under_2 / total +
                    weekly_monday_to_thursday_under_3 / total + weekly_monday_to_thursday_under_4 / total)))
print("SWEET SPOT ABOVE 4 = " + str(
    "{:.2%}".format(1 - (weekly_monday_to_thursday_under_1 / total + weekly_monday_to_thursday_under_2 / total +
                         weekly_monday_to_thursday_under_3 / total + weekly_monday_to_thursday_under_4 / total))))
print()
print("------- TUESDAY TO THURSDAY CHANGE FOR PAST 20 YEARS-------- ")
print()
total = tuesday_total
print("UNDER 1 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_under_1 / total)))
print("UNDER 2 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_under_2 / total)))
print("UNDER 3 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_under_3 / total)))
print("UNDER 4 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_under_4 / total)))
print("UNDER 5 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_under_5 / total)))
print("UNDER 6 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_under_6 / total)))
print("UNDER 7 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_under_7 / total)))
print("UNDER 8 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_under_8 / total)))
print("UNDER 10 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_under_10 / total)))
print("UNDER 15 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_under_15 / total)))
print("ABOVE 15 = " + str("{:.2%}".format(weekly_tuesday_to_thursday_above_15 / total)))
print("SWEET SPOT UNDER 3 = " + str(
    "{:.2%}".format(weekly_tuesday_to_thursday_under_1 / total + weekly_tuesday_to_thursday_under_2 / total +
                    weekly_tuesday_to_thursday_under_3 / total)))
print("SWEET SPOT ABOVE 3 = " + str(
    "{:.2%}".format(1 - (weekly_tuesday_to_thursday_under_1 / total + weekly_tuesday_to_thursday_under_2 / total +
                         weekly_tuesday_to_thursday_under_3 / total))))
print()
print("------- WEDNESDAY TO THURSDAY CHANGE FOR PAST 20 YEARS-------- ")
print()
total = wednesday_total
print("UNDER 1 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_under_1 / total)))
print("UNDER 2 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_under_2 / total)))
print("UNDER 3 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_under_3 / total)))
print("UNDER 4 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_under_4 / total)))
print("UNDER 5 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_under_5 / total)))
print("UNDER 6 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_under_6 / total)))
print("UNDER 7 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_under_7 / total)))
print("UNDER 8 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_under_8 / total)))
print("UNDER 10 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_under_10 / total)))
print("UNDER 15 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_under_15 / total)))
print("ABOVE 15 = " + str("{:.2%}".format(weekly_wednesday_to_thursday_above_15 / total)))
print("SWEET SPOT UNDER 3 = " + str(
    "{:.2%}".format(weekly_wednesday_to_thursday_under_1 / total + weekly_wednesday_to_thursday_under_2 / total +
                    weekly_wednesday_to_thursday_under_3 / total)))
print("SWEET SPOT ABOVE 3 = " + str(
    "{:.2%}".format(1 - (weekly_wednesday_to_thursday_under_1 / total + weekly_wednesday_to_thursday_under_2 / total +
                         weekly_wednesday_to_thursday_under_3 / total))))
print()
print("------- FRIDAY TO THURSDAY CHANGE FOR PAST 20 YEARS-------- ")
print()
total = friday_total
print("UNDER 1 = " + str("{:.2%}".format(weekly_friday_to_thursday_under_1 / total)))
print("UNDER 2 = " + str("{:.2%}".format(weekly_friday_to_thursday_under_2 / total)))
print("UNDER 3 = " + str("{:.2%}".format(weekly_friday_to_thursday_under_3 / total)))
print("UNDER 4 = " + str("{:.2%}".format(weekly_friday_to_thursday_under_4 / total)))
print("UNDER 5 = " + str("{:.2%}".format(weekly_friday_to_thursday_under_5 / total)))
print("UNDER 6 = " + str("{:.2%}".format(weekly_friday_to_thursday_under_6 / total)))
print("UNDER 7 = " + str("{:.2%}".format(weekly_friday_to_thursday_under_7 / total)))
print("UNDER 8 = " + str("{:.2%}".format(weekly_friday_to_thursday_under_8 / total)))
print("UNDER 10 = " + str("{:.2%}".format(weekly_friday_to_thursday_under_10 / total)))
print("UNDER 15 = " + str("{:.2%}".format(weekly_friday_to_thursday_under_15 / total)))
print("ABOVE 15 = " + str("{:.2%}".format(weekly_friday_to_thursday_above_15 / total)))
print("SWEET SPOT UNDER 5 = " + str(
    "{:.2%}".format(weekly_friday_to_thursday_under_1 / total + weekly_friday_to_thursday_under_2 / total +
                    weekly_friday_to_thursday_under_3 / total + weekly_friday_to_thursday_under_4 / total +
                    weekly_friday_to_thursday_under_5 / total)))
print("SWEET SPOT ABOVE 5 = " + str(
    "{:.2%}".format(1 - (weekly_friday_to_thursday_under_1 / total + weekly_friday_to_thursday_under_2 / total +
                         weekly_friday_to_thursday_under_3 / total + weekly_friday_to_thursday_under_4 / total +
                         weekly_friday_to_thursday_under_5 / total))))
print()
print("------- WEEKLY OPEN TO LOW CHANGE FOR PAST 20 YEARS-------- ")
print()
total = len(weekly_lows)
print("UNDER 1 = " + str("{:.2%}".format(weekly_open_to_low_under_1 / total)))
print("UNDER 2 = " + str("{:.2%}".format(weekly_open_to_low_under_2 / total)))
print("UNDER 3 = " + str("{:.2%}".format(weekly_open_to_low_under_3 / total)))
print("UNDER 4 = " + str("{:.2%}".format(weekly_open_to_low_under_4 / total)))
print("UNDER 5 = " + str("{:.2%}".format(weekly_open_to_low_under_5 / total)))
print("UNDER 6 = " + str("{:.2%}".format(weekly_open_to_low_under_6 / total)))
print("UNDER 7 = " + str("{:.2%}".format(weekly_open_to_low_under_7 / total)))
print("UNDER 8 = " + str("{:.2%}".format(weekly_open_to_low_under_8 / total)))
print("UNDER 10 = " + str("{:.2%}".format(weekly_open_to_low_under_10 / total)))
print("UNDER 15 = " + str("{:.2%}".format(weekly_open_to_low_under_15 / total)))
print("ABOVE 15 = " + str("{:.2%}".format(weekly_open_to_low_above_15 / total)))
print("SWEET SPOT UNDER 5 = " + str(
    "{:.2%}".format(weekly_open_to_low_under_1 / total + weekly_open_to_low_under_2 / total +
                    weekly_open_to_low_under_3 / total + weekly_open_to_low_under_4 / total +
                    weekly_open_to_low_under_5 / total)))
print("SWEET SPOT ABOVE 5 = " + str(
    "{:.2%}".format(1 - (weekly_open_to_low_under_1 / total + weekly_open_to_low_under_2 / total +
                         weekly_open_to_low_under_3 / total + weekly_open_to_low_under_4 / total +
                         weekly_open_to_low_under_5 / total))))

print()
print("------- WEEKLY OPEN TO HIGH CHANGE FOR PAST 20 YEARS-------- ")
print()
total = len(weekly_highs)
print("UNDER 1 = " + str("{:.2%}".format(weekly_open_to_high_under_1 / total)))
print("UNDER 2 = " + str("{:.2%}".format(weekly_open_to_high_under_2 / total)))
print("UNDER 3 = " + str("{:.2%}".format(weekly_open_to_high_under_3 / total)))
print("UNDER 4 = " + str("{:.2%}".format(weekly_open_to_high_under_4 / total)))
print("UNDER 5 = " + str("{:.2%}".format(weekly_open_to_high_under_5 / total)))
print("UNDER 6 = " + str("{:.2%}".format(weekly_open_to_high_under_6 / total)))
print("UNDER 7 = " + str("{:.2%}".format(weekly_open_to_high_under_7 / total)))
print("UNDER 8 = " + str("{:.2%}".format(weekly_open_to_high_under_8 / total)))
print("UNDER 10 = " + str("{:.2%}".format(weekly_open_to_high_under_10 / total)))
print("UNDER 15 = " + str("{:.2%}".format(weekly_open_to_high_under_15 / total)))
print("ABOVE 15 = " + str("{:.2%}".format(weekly_open_to_high_above_15 / total)))
print("SWEET SPOT UNDER 5 = " + str(
    "{:.2%}".format(weekly_open_to_high_under_1 / total + weekly_open_to_high_under_2 / total +
                    weekly_open_to_high_under_3 / total + weekly_open_to_high_under_4 / total +
                    weekly_open_to_high_under_5 / total)))
print("SWEET SPOT ABOVE 5 = " + str(
    "{:.2%}".format(1 - (weekly_open_to_high_under_1 / total + weekly_open_to_high_under_2 / total +
                         weekly_open_to_high_under_3 / total + weekly_open_to_high_under_4 / total +
                         weekly_open_to_high_under_5 / total))))

print()
print("------- MONTHLY CHANGE FOR PAST 20 YEARS-------- ")
print()
total = len(monthly_close)
print("UNDER 2 = " + str("{:.2%}".format(monthly_thursday_under_2 / total)))
print("UNDER 4 = " + str("{:.2%}".format(monthly_thursday_under_4 / total)))
print("UNDER 6 = " + str("{:.2%}".format(monthly_thursday_under_6 / total)))
print("UNDER 8 = " + str("{:.2%}".format(monthly_thursday_under_8 / total)))
print("UNDER 10 = " + str("{:.2%}".format(monthly_thursday_under_10 / total)))
print("UNDER 12 = " + str("{:.2%}".format(monthly_thursday_under_12 / total)))
print("UNDER 14 = " + str("{:.2%}".format(monthly_thursday_under_14 / total)))
print("UNDER 16 = " + str("{:.2%}".format(monthly_thursday_under_16 / total)))
print("UNDER 18 = " + str("{:.2%}".format(monthly_thursday_under_18 / total)))
print("UNDER 20 = " + str("{:.2%}".format(monthly_thursday_under_20 / total)))
print("ABOVE 20 = " + str("{:.2%}".format(monthly_thursday_above_20 / total)))
print(
    "SWEET SPOT UNDER 10 = " + str("{:.2%}".format(monthly_thursday_under_2 / total + monthly_thursday_under_4 / total +
                                                   monthly_thursday_under_6 / total + monthly_thursday_under_8 / total +
                                                   monthly_thursday_under_10 / total)))
print("SWEET SPOT ABOVE 10 = " + str(
    "{:.2%}".format(1 - (monthly_thursday_under_2 / total + monthly_thursday_under_4 / total +
                         monthly_thursday_under_6 / total + monthly_thursday_under_8 / total +
                         monthly_thursday_under_10 / total))))
print("------- MONTHLY OPEN TO LOW CHANGE FOR PAST 20 YEARS-------- ")
print()
total = len(monthly_lows)
print("UNDER 2 = " + str("{:.2%}".format(monthly_open_to_low_under_2 / total)))
print("UNDER 4 = " + str("{:.2%}".format(monthly_open_to_low_under_4 / total)))
print("UNDER 6 = " + str("{:.2%}".format(monthly_open_to_low_under_6 / total)))
print("UNDER 8 = " + str("{:.2%}".format(monthly_open_to_low_under_8 / total)))
print("UNDER 10 = " + str("{:.2%}".format(monthly_open_to_low_under_10 / total)))
print("UNDER 12 = " + str("{:.2%}".format(monthly_open_to_low_under_12 / total)))
print("UNDER 14 = " + str("{:.2%}".format(monthly_open_to_low_under_14 / total)))
print("UNDER 16 = " + str("{:.2%}".format(monthly_open_to_low_under_16 / total)))
print("UNDER 18 = " + str("{:.2%}".format(monthly_open_to_low_under_18 / total)))
print("UNDER 20 = " + str("{:.2%}".format(monthly_open_to_low_under_20 / total)))
print("ABOVE 20 = " + str("{:.2%}".format(monthly_open_to_low_above_20 / total)))
print(
    "SWEET SPOT UNDER 10 = " + str(
        "{:.2%}".format(monthly_open_to_low_under_2 / total + monthly_open_to_low_under_4 / total +
                        monthly_open_to_low_under_6 / total + monthly_open_to_low_under_8 / total +
                        monthly_open_to_low_under_10 / total)))
print("SWEET SPOT ABOVE 10 = " + str(
    "{:.2%}".format(1 - (monthly_open_to_low_under_2 / total + monthly_open_to_low_under_4 / total +
                         monthly_open_to_low_under_6 / total + monthly_open_to_low_under_8 / total +
                         monthly_open_to_low_under_10 / total))))
print("------- MONTHLY OPEN TO HIGH CHANGE FOR PAST 20 YEARS-------- ")
print()
total = len(monthly_highs)
print("UNDER 2 = " + str("{:.2%}".format(monthly_open_to_high_under_2 / total)))
print("UNDER 4 = " + str("{:.2%}".format(monthly_open_to_high_under_4 / total)))
print("UNDER 6 = " + str("{:.2%}".format(monthly_open_to_high_under_6 / total)))
print("UNDER 8 = " + str("{:.2%}".format(monthly_open_to_high_under_8 / total)))
print("UNDER 10 = " + str("{:.2%}".format(monthly_open_to_high_under_10 / total)))
print("UNDER 12 = " + str("{:.2%}".format(monthly_open_to_high_under_12 / total)))
print("UNDER 14 = " + str("{:.2%}".format(monthly_open_to_high_under_14 / total)))
print("UNDER 16 = " + str("{:.2%}".format(monthly_open_to_high_under_16 / total)))
print("UNDER 18 = " + str("{:.2%}".format(monthly_open_to_high_under_18 / total)))
print("UNDER 20 = " + str("{:.2%}".format(monthly_open_to_high_under_20 / total)))
print("ABOVE 20 = " + str("{:.2%}".format(monthly_open_to_high_above_20 / total)))
print(
    "SWEET SPOT UNDER 10 = " + str(
        "{:.2%}".format(monthly_open_to_high_under_2 / total + monthly_open_to_high_under_4 / total +
                        monthly_open_to_high_under_6 / total + monthly_open_to_high_under_8 / total +
                        monthly_open_to_high_under_10 / total)))
print("SWEET SPOT ABOVE 10 = " + str(
    "{:.2%}".format(1 - (monthly_open_to_high_under_2 / total + monthly_open_to_high_under_4 / total +
                         monthly_open_to_high_under_6 / total + monthly_open_to_high_under_8 / total +
                         monthly_open_to_high_under_10 / total))))

print("------- AVERAGE CHANGES IN 20 YEARS-------- ")
print()
total = monday_total
print("WEEKLY = " + str("{:.2%}".format(weekly_sum / 100 / total)))
print("FRI TO THU = " + str("{:.2%}".format(friday_sum / 100 / total)))
print("MON TO THU = " + str("{:.2%}".format(monday_sum / 100 / total)))
print("TUE TO THU = " + str("{:.2%}".format(tuesday_sum / 100 / total)))
print("WED TO THU = " + str("{:.2%}".format(wednesday_sum / 100 / total)))
total = len(monthly_highs)
print("MONTHLY = " + str("{:.2%}".format(monthly_sum/ 100 / total)))
