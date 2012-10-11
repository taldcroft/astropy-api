#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import astropy.units as u

# ============
# Base Objects
# ============
"""
The Quantity class will represent a number + unit, and will understand how
to do operations between other quantity classes to convert the units automatically.
"""

# Creating quantities
# -------------------

# The preferred method for creating a quantity is through operations with units
q = 11.42 * u.meter # returns a Quantity object
q = 182.234 + u.meter # raises an error

# You could also use the Quantity constructor, but units must be supplied
q1 = u.Quantity(11.412, unit=u.meter)
q2 = u.Quantity(21.52, unit="cm")
q3 = u.Quantity(11.412) # raises an exception because no unit specified

# Operations
# ----------

"""
We have enough information to actually do this operation if the units are equivalent
but we don't know what unit to output -- how do we solve this? It would be very powerful
to have this kind of arithmetic.
"""

# Each of these operations would return a new Quantity object with the units of the quantity
#   object on the *left*
new_quantity = quantity1 + quantity2
new_quantity = quantity1 - quantity2
new_quantity = quantity1 * quantity2
new_quantity = quantity1 / quantity2
new_quantity = -quantity1

# Converting units
# ----------------
q = 11.412*u.meter

# to get a new quantity object in some new, equivalent units, you would use the to() method:
q.to(u.kilometer) # this returns a new quantity object with the supplied units
q.to(u.zettastokes) # Fails because not equivalent

# you may also just want the *value* of the quantity in some units. To do this, use the value_in() method:
quantity1.value_in(u.centimeter) # returns the *value* (just a number, not an object) of this quantity in the specified units

# Displaying
# ----------
# Printing the quantity should display the number and the units when converting to a string
str(quantity) # returns '11.412 m'
repr(quantity) # returns '<Quantity Value: 11.412 Units: meter>' or something