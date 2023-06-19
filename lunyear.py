import sxtwl
#日曆中文索引
# 從公曆年月日獲取一天的信息 （如果需要查公元前的，年份可以使用負號表示，1800年以前的都可以查）
day_solar = sxtwl.fromSolar(2023, 6, 17) 
print(day_solar.getLunarYear(),day_solar.getLunarMonth(),day_solar.getLunarDay())
# 從農曆年月日獲取一天的信息
day = sxtwl.fromLunar(2023, 4, 18)
# 公曆的年月日
s = "公曆:%d年%d月%d日" % (day.getSolarYear(), day.getSolarMonth(), day.getSolarDay())
print(s)