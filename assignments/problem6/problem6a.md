# Problem 6 "Writing a Function"
## Outcomes
- Use control statements to check input and output
- Parse input using character and string data types

## Problem 
You will be writing a **function** that calculates the range and time of flight of a projectile given the initial launch velocity and angle. You can ignore air resistance, for now. After learning how differential equations work in MATLAB/Python, we will return to this function to incorporate air resistance (and maybe the Coriolis effect).
## Procedure
1.  Review the kinematic equations for 2D projectile motion.
1.  Use the function `fsatellite.m` that I recently posted as a syntax template for a function, and use your projectile script as a starting point for the code. 
1.  Write a function that accepts the initial velocity, launch angle of a projectile, and a third argument for units, and returns the
horizontal distance traveled (aka the range) and the flight time of the projectile. Make sure to:
 * Accept velocities in mph and m/s (*I highly suggest getting it working before attempting any unit shenanigans*)
 * Check that the input is valid using control statements
 * Only accept launch angles between 0 and 90 degrees
 * Graph the trajectory of the projectile, maybe try to use an animated line
## Check your program
Inputting arguments into functions is a little different than with scripts. The arguments should be inputted when you call the function. Check that you can run your function using the following syntax:
```
[R,t] = fsatellite(30,30,"m/s")
R =
    79.5 
t =
    3.05
```
```
[R,t] = fsatellite(45,65,"mph")
R =
    103.7 
t =
    3.73
```


