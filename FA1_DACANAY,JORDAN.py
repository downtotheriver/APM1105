#!/usr/bin/env python
# coding: utf-8

# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a
# mile.

# In[5]:


print("Enter the number in kilometers")
kilometers = float(input("Kilometers: "))
print()
print("Kilometers: ", kilometers)
print("Miles: ", kilometers * 1.61)


# If  you  run  a  10  kilometer  race  in  42  minutes  42  seconds,  what  is  your  average
# pace  (time  per  mile  in  minutes  and  seconds)?  What  is  your  average  speed  in
# miles per hour?

# In[49]:


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

print("Enter their value")
kilometers = float(input("Kilometers: "))
minutes = 4
seconds = 16.2

estimated_kilometers = truncate(kilometers)

miles = kilometers * 1.61
minutes_converted = seconds / 60

total_minutes = minutes_converted + minutes

time_converted = kilometers * total_minutes

estimated_time = truncate(time_converted, 2)

print()

hours = estimated_time / 60

speed = miles/hours
estimated_speed = truncate(speed, 2)

converted_minutes = estimated_time // 1
second = estimated_time - (estimated_time // 1)
estimated_second = truncate(second, 3)
converted_seconds = estimated_second * 60

print("Average Pace (time per mile in minutes and seconds): ", miles, "miles in", converted_minutes, "minutes and", converted_seconds, "seconds")
print("Average Speed (miles per hour): ", estimated_speed, "miles per hour")


# In[ ]:




