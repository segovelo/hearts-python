# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:16:02 2022

@author: Sebastian
"""

def top_of_heart(x):
  counter = 1
  midpoint = x//2+1
  for i in range(x):
    print(" "*(midpoint-2)+"\u2764\uFE0F "*2*counter + " "*2*(midpoint - (counter-1)) + "\u2764\uFE0F "*2*counter)
    midpoint -= 2
    if midpoint <= 3:
      break
    counter += 1

def full_heart(num_rows):
  counter = 0
  num_columns = num_rows
  for i in range(num_rows):
    if num_rows == 2:
      print(" "*(num_columns-1) + "\u2764\uFE0F ")
      break
    if counter == 0:
      top_of_heart(num_rows)
    elif counter == 1:
      print(" "*i + "\u2764\uFE0F "*(num_rows-i))
    elif counter == 2 or counter == 3:
      print("\u2764\uFE0F "*num_rows)
    else:
      print(" "*(num_columns-(num_rows-2)) + "\u2764\uFE0F "*(num_rows-2))
      num_rows = num_rows-2
      if num_rows == 1:
        break
    counter += 1


full_heart(20)

  