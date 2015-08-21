from timeclock import Clock
import time
clock = Clock('EST')

# print clock.now()
#
# print clock.now(tz='GMT', format='%H')
#
# print clock.now()
format = "%Y %m %d %H %M %S"

print clock.now()
# print "Time until the 21th: "
# print clock.elTime(clock.now(format), "2015 08 21 16 01 01", format=format)

# print "Time since the 20th: "
# print clock.elTime("2016 08 15 01 01 01", clock.now(format), format=format)
# then = clock.now(format)
# time.sleep(10)
# now = clock.now(format)
#
# print clock.elTime(then, now, format=format)
format = "%H %M %S"
print clock.elTime(clock.now(format), "22 18 00", format=format)
