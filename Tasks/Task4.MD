# Task 4: New Functionality

## Review

- In task 1, you drafted a newly designed architecture for your component;
- In task 2, you refactored the messy codebase; and
- In task 3, you introduced unit tests for your newly refactored system.
- In this final task, you’ll be asked to add some new functionality to the system. You will be using a test-driven development workflow - often abbreviated TDD - to make the changes.


## Test-driven development

TDD is a hybrid workflow that combines testing, coding and refactoring, where you constantly bounce back and forth between writing code and writing test cases for it. The workflow encourages good habits, helps you consider all possible edge cases, and leads to a robust, comprehensive test suite upon completion of the project.

**Is TDD the gold standard workflow for writing code?**

**The short-answer is no.**

TDD is not the best or the only coding workflow - every programmer develops (through much time and experience) their own processes, which work for them.

Some software engineers swear by it, some can’t stand it; neither is made a better developer for their view of the paradigm.

Figuring out what works for you requires years of practice and refinement, so as you take your first steps out of the syntax nursery and into the mystical world of theory, it’s important to expose yourself to the various competing schools of thought built around writing clean code.

TDD is a classic approach, and even if you don’t strictly adhere to the admittedly rigid testing cadence in the workflow you develop, there are still valuable lessons to be garnered from the doctrine. The most important thing to remember is to eschew dogma in favor of what actually works for you, provided you take the time to fully comprehend and play with the workflows you have available.

## Changes required

1. Upgrade Spindler batteries

- First, modify the Spindler battery so it requires service after three years instead of two.
- Notice how easy it is to make this change - you only need to touch one line of code instead of several, and the place where that line of code lives should be immediately obvious.
- Consider what steps would have been required to make this change to the original system architecture, and how much more difficult it would have been, especially if you were new to working on the codebase.

2. Add tire servicing criteria

- There are two types of tires currently in use by the Lyft fleet - Carrigan tires and Octoprime tires.

- The new tire wear sensors produce an array of four numbers between 0 and 1 inclusive, representing how worn each of the tires are.

- This array will be passed to each function in the car factory class, to be used by your tire implementation.

- Carrigan tires should be serviced only when one or more of the values in the tire wear array is greater than or equal to 0.9.

- Octoprime tires should be serviced only when the sum of all values in the tire wear array is greater than or equal to 3.

- hink carefully about the cleanest way to implement the new tire service criteria, then modify the system to complete the change.
