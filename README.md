Timeclock
---------
Simpler Date/Time Wrapper for Python

Datetime [Format Directives](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior).

When initializing ```Clock()``` specify your current Timezone (Permanent assignment).
```python
from timeclock import Clock
clock = Clock('EST')
print clock.now()
> 16:19:36 - 08/21/2015 #Default Format
```
Format can be specified with ```format``` argument.

```python
print clock.now(format="%H:%M")
> 16:19
```

Timezone specification (This is a temporary assignment):

```python
print clock.now(tz='GMT')
> 21:19:36 - 08/21/2015
```

Measuring time elapsed (past time first):

```python
format = "%H %M %S"
print clock.elap(clock.now(format), "22 18 00", format=format)
> {'Sec': 20501, 'Hour': 5, 'Min': 341} #Total time for each value
```
