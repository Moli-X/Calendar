import holidays
from ics import Calendar, Event
from datetime import datetime, timedelta

# 生成中国节假日的 .ics 文件
def generate_china_holiday_ics(year):
    # 获取中国的节假日
    ch_holidays = holidays.China(years=year)

    # 创建 ICS 文件
    calendar = Calendar()

    for date, name in ch_holidays.items():
        event = Event()
        event.name = name
        event.begin = date
        event.end = date
        event.make_all_day()

        # 添加到日历
        calendar.events.add(event)

    # 保存到 .ics 文件
    with open(f"china_holidays_{year}.ics", "w", encoding="utf-8") as f:
        f.writelines(calendar)

    print(f"Generated china_holidays_{year}.ics successfully.")

if __name__ == "__main__":
    # 生成当前年份的节假日
    current_year = datetime.now().year
    generate_china_holiday_ics(current_year)
