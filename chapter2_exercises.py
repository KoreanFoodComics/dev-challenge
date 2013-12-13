#!/usr/bin/python

# Exercises for chapter 2:

# Name: Bailey Solomon Johnson

import math
from datetime import datetime, timedelta

print "Chapter 1: N/A"

## 2.1 

print "Exercise 2.1"
print "this exercise taught us about errors btwn octal math (in the computer) and base 10 math that we use"

zipcode="02942"
## print as integer
print int(zipcode)

value = "0100"
print int(value)

## 2.2
print "Exercise 2.2"

x = 5
y = x+1
print y

##2.3
print "Exercise 2.3"

width = 17
height = 12.0
delimiter = ' . '

print width/2
print width/2.0
print height/3
print 1+2*5
print delimiter *5

##2.4

##2.4.1
print "Exercise 2.4.1"

r = 5
pi = 3.14

#vol = (float(4)/float(3)*float(pi)*(float(r**3)) ## ugly

vol = float(4)/float(3)*math.pi*5**3

print vol

##2.4.2
print "Exercise 2.4.2"

cover=24.95
discount= cover * (float(40)/float(100))
first_cost=3
additional_cost=0.75
copies=60


book_cost = (cover - discount)

shipping = first_cost + (additional_cost * (copies-1))

total_cost = book_cost + shipping

print total_cost

##2.4.3
print "Exercise 2.4.3"


def getSeconds(time_str):
	t = time_str.split(':')
	return int(t[0]) *3600 + int(t[1]) * 60 + int(t[2])

start_time = datetime.strptime('6:52:00', '%H:%M:%S')

## Easy pace seconds

easy_pace_sec = getSeconds ("0:8:15") * 2

## brisk pace Seconds

brisk_pace_sec = getSeconds("0:7:12") * 3

## total Seconds
tot_sec = easy_pace_sec + brisk_pace_sec

print "Total Seconds ", tot_sec

final_time = start_time + timedelta(seconds=tot_sec)
print "Final Time:", final_time.strftime('%H:%M%S')