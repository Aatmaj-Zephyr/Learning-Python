# [Learning Python- Intermediate course: Day 13, The Statistics Module](https://dev.to/aatmaj/learning-python-intermediate-course-day-13-the-statistics-module-2bb5)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-13-the-statistics-module-2bb5)

## Today we will cover the `statistics` module in python.

---

Python has the built-in module `statistics` that you can use to calculate mathematical statistics of numeric data. You do not require to install anything extra. This `statistics` module was introduced new in Python 3.4.

The below sample shows the various functions in the module. I have ordered the methods as per the level of usage.

```python
>>> import statistics as st
>>> a=[1,1,2,6,5,7,7,7,8,9]
>>> st.mean(a)
#Calculates the mean (average) of the given data
5.3
>>> st.mode(a)
#Calculates the mode (central tendency) of the given numeric or nominal data
7
>>> st.harmonic_mean(a)
#Calculates the harmonic mean of the given data
2.8317788515563547
>>> b=[-2,3,4]
>>> st.harmonic_mean(b)
#StatisticsError is raised if data is empty, or any element is less than zero.
#Harmonic mean doesn't support negative numbers
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python39\lib\statistics.py", line 406, in harmonic_mean
    T, total, count = _sum(1 / x for x in _fail_neg(data, errmsg))
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python39\lib\statistics.py", line 164, in _sum
    for typ, values in groupby(data, type):
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python39\lib\statistics.py", line 406, in <genexpr>
    T, total, count = _sum(1 / x for x in _fail_neg(data, errmsg))
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python39\lib\statistics.py", line 289, in _fail_neg
    raise StatisticsError(errmsg)
statistics.StatisticsError: harmonic mean does not support negative values
>>> st.median(a)
#Calculates the median (middle value) of the given data
6.5
>>> st.stdev(a)
#Calculates the standard deviation from a sample of data
2.94580681270476
>>> st.variance(a)
#Calculates the variance from a sample of data
8.677777777777777
>>> st.median_high(a)
#Calculates the high median of the given data
7
>>> st.median_low(a)
#Calculates the low median of the given data
6
>>> st.median_grouped(a)
#Calculates the median of grouped continuous data
6.5
>>> st.pvariance(a)
#Calculates the variance of an entire population(dataset)
7.81
>>> st.pstdev(a)
#Calculates the standard deviation from an entire population
2.794637722496424
>>> a=[]
>>> st.median(a)
# If data is empty, StatisticsError will be raised.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python39\lib\statistics.py", line 430, in median
    raise StatisticsError("no median for empty data")
statistics.StatisticsError: no median for empty data
```

You will find a more detailed and comprehensive explaination at the [official documentation](https://docs.python.org/3/library/statistics.html)
