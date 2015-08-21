Timeclock
---------
Simpler Date/Time Wrapper for Python

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

Timezone specification (This is be a temporary assignment):

```python
print clock.now(tz='EST')
```

Measuring time elapsed (past time first):

```python
format = "%H %M %S"
print clock.elTime(clock.now(format), "22 18 00", format=format)
> {'Sec': 20501, 'Hour': 5, 'Min': 41}
```
