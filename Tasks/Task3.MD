# Task 3: Unit Test

## Unit Test

- Put simply, a unit test is a software testing method whereby “units” — the individual components that make up software — are tested.
- Software Engineers write unit tests for their code in order to make sure the code works as expected. This helps to detect any errors and protect against bugs.
- Unit tests are necessary for any production system, and directly correlate with the quality of sleep everyone on the engineering team experiences.

## Purposes

1. Unit tests most obviously provide a means of assessing the correctness of a system. They describe the expected behavior of a piece of code, and allow you to check that it works with the click of a button. It’s easy to miss something with static analysis alone - unit tests give you instantaneous, quantitative feedback regarding whether the system works as expected.
2. Unit tests provide a sort of documentation for the code - describing expected inputs and outputs, as well as the correct way to use a component. By reading the unit tests for a codebase you are unfamiliar with, you can gain a clearer understanding of how each component should be used, and how they fit together.
3. Unit tests allow you to easily check if a change to the system breaks something. Suppose you modify part A of the system, which is tightly coupled with part B - by running the unit tests for part B, you can instantly ensure that your change did not break that component (provided the tests are written well).
4. Unit tests provide yet another way to assess the cleanliness of your codebase. If a piece of code is difficult to test, it is almost always a code smell. Clean code is easy to test; if you are struggling to write clean tests for a piece of code, chances are the code needs to be reorganized, not the tests.
5. Unit tests assist in development using workflows like TDD (test-driven development). By writing unit tests as you code, you are granted all of the above metrics and indications immediately. They can then respond to them as they crop up. We’ll circle back to this point in the next task.
6. Unit tests provide a sandbox for thoroughly considering every edge case. The art of writing a good test case is the art of coming up with clever ways to break your own code. By spending time considering all the ways your code could malfunction in a chaotic fashion and hardening your code against them, you will end up with a more robust codebase.

## Considerations

Some key points to consider when writing your unit tests are:

- In a real-world environment, you should always check that parameters are what you expect, especially in a loosely typed language like Python. Part of the point of unit testing is to ensure your system does not fail in the presence of edge cases, including ridiculous ones (users can’t be trusted with anything these days).
- That being said, this task is focused on unit testing as it applies to refactoring, so, for the sake of time, you may assume all inputs to the system are valid (i.e all parameters are the expected type and all values are within reasonable bounds).
- You’ll need to replace the old test suite in the tests folder with your own series of unit tests.
- The old test suite should be broken (since you replaced all the classes it tests in the last step), but it should still serve as a handy template to speed you on your way.
- Note that you need only test concrete implementations of the engine and battery classes for this task. You may ignore testing on everything else.
- If you run into problems with the code you wrote in the last task while drafting unit tests, fix it! The goal of testing in this instance is to refine the draft codebase you created in the last task into something that’s guaranteed to work.
