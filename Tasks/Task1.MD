# Task One

## Description
- You are working as a Back-End Engineer at Lyft.
- As a Back-End Engineer you collaborate within a larger team made up of software engineering, product, data science, analytics and operations.
- Your team is responsible for Lyft Rentals. Lyft Rentals provides vehicles for riders who are looking to rent a vehicle for personal use such as a weekend vacation.
- Throughout the program your team will takeover an unfinished project to:
  1. Come up with a clean design for an existing, unfinished component
  2. Refactor a messy codebase
  3. Write unit tests for your newly refactored system
  4. Add new functionality to your system using Test-Driven Development
- You’ll receive guidance and support at each step of the journey. That being said, to complete this program, it’s advised that you have a baseline understanding of Python.

## Key Roles and Responsibilities of a Back-End Engineer at Lyft
A back-end engineer is responsible for creating the skeleton to ensure a website performs correctly. 

The focus for a back-end engineer is on:
  - Back-end logic
  - Database management
  - Application program interfaces (APIs)
  - Architecture
  - Servers

As a Back-End Engineer at Lyft in the Lyft Rentals team, you’ll get to work across a range of different problems to ensure that you deliver the world’s most delightful and easy to use car rental experience.


# The project at hand
Lyft is in the process of rolling out a new rental fleet in the hopes of encouraging more connected, sustainable cities across the US.

Your team has inherited an urgent project from a fellow colleague here at Lyft who had to make a pivot to a different project. The colleague was in the process of developing a component that is used by the rental fleet’s new logistics system. Unfortunately that component was only partially completed and your team’s responsibility is to now finalize that component and make it functional.

The component itself is responsible for determining whether cars in Lyft’s new rental fleet should be serviced when they are returned. The work you will do on this component will be carried through the each of the tasks within this program.

## Criteria for car servicing
Whether or not a Lyft rental car should be serviced depends on two factors at the moment:

The engine; and The battery.

Each of the three types of engines has its own criteria for determining when it should be serviced. The same applies to each type of battery.

The current service criteria are as follows:
|       Service       |             Service Criteria          |
|---------------------|---------------------------------------|
|   Capulet Engine   | once every 30,000 miles               |
|   Willoughby Engine | once every 60,000 miles               |
|   Sternman Engine   | only when the warning indicator is on |
|   Spindler Battery  | once every 2 years                    |
|   Nubbin Battery    | once every 4 years                    |

There are five car models in Lyft’s fleet, each with a different engine-battery combination. These are outlined below:

|   Car      |       Engine      |       Battery    |
|------------|-------------------|------------------|
|   Calliope | Capulet Engine    | Spindler Battery |
|   Glissade | Willoughby Engine | Spindler Battery |
| Palindrome | Sternman Engine   | Nubbin Batte     |
|  Rorschach | Willoughby Engine | Nubbin Batte     |
|   Thovex   | Capulet Engine    | Nubbin Battery   |

These service criteria will change somewhat frequently in the future, and new car models are bound to be added to the fleet. This is an important consideration throughout the program.

With this in mind, it’s very important that the component is extensible and easy to modify, so new service criteria can be added quickly and efficiently. Just today, you learned that the system must also take tires into account when determining if a car should be serviced in the future.

Tacking this functionality onto the current system would be difficult and messy - instead, you have been instructed to take the time to refactor the codebase prior to making the change. The first step of this process is to draft up a new (clean) system architecture that will allow for the seamless inclusion of the new functionality. Your task is to draft and submit a class diagram that maps out how the system will be reorganized.


## Software Architecture & Codebase

Clone the following repo to your machine: 
https://github.com/vagabond-systems/forage-lyft-starter-repo

A step-by-step instruction on how to do this is outlined here on GitHub: 
https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

The repo you just cloned contains the core functionality of the fleet service component referenced above.

In order to come up with a better design, you must first fully comprehend the current state of the codebase. Spend some time reading through each file and figuring out how things are organized.

It would be helpful to draw out how the classes currently relate to one another.
