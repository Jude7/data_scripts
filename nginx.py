# -*- coding: utf-8 -*-
import datetime


dt_now = datetime.datetime.now()
str_now = dt_now.strftime("%d/%B/%Y:%H:%M:%S")
str_now = "28/Feb/2019:13:17:10"

d = "https://domain1.com"

req_count = 0
day_count = 0

with open("access.log") as e:
    for item in e.readlines():
        log_format_list = item.split()

        # Req count
        if log_format_list[10].strip(f'{log_format_list[6]}"') == d:
            req_count += 1

        # Day Count
        if log_format_list[10].strip(f'{log_format_list[6]}"') == d and \
            log_format_list[3].strip("[") == str_now and \
                log_format_list[8] == "200":
            day_count += 1


print(f"域名请求个数: {req_count}")
print(f"域名当前请求成功个数: {day_count}")
