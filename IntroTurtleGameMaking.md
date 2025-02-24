# Introduction to Turtle and Game Making

## What is Turtle?

Turtle is a **Python library** that lets you create drawings, animations, and even simple games! It’s often used to teach programming because it’s very visual and easy to understand.

Imagine you have a little "turtle" on the screen. This turtle can move around and draw lines as it goes. You give it commands, and it follows them to create shapes, patterns, or pictures. It’s a great way to learn how code works and see the result immediately.

## Basic Turtle Concepts:

- **Turtle**: The turtle is like a pen that moves on the screen. It can draw, change color, and make shapes.
- **Commands**: You give commands to the turtle to move it around. For example:
  - `forward(distance)` moves the turtle forward by the given distance.
  - `left(angle)` turns the turtle left by the specified angle.
  - `right(angle)` turns the turtle right by the specified angle.

### Example of Basic Code:

```python
import turtle

t = turtle.Turtle()  # Create a turtle object
t.forward(100)       # Move the turtle forward by 100 units
t.left(90)           # Turn the turtle 90 degrees to the left
t.forward(100)       # Move the turtle forward again
