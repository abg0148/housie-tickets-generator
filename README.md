## Housie(Tambola) Tickets Generator Using Python

### About

A housie ticket consists of a random distribution of 15 unique numbers between 1-90 in a 3x9 matrix.
Here is an example of a ticket.

**RULE #1** - Each row cannot has 5 numbers

**RULE #2** - Each column is assigned a range of numbers only: (ex. 1-10 can appear only in column 1)

**RULE #3** - In a specific column, numbers must be arranged in ascending order from top to bottom

### Requirements

* [Python](https://www.python.org)
* [Numpy](https://numpy.org/) (python package)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) (python package)

### Usage

* Clone this repository `git clone https://github.com/abg0148/housie-tickets-generator.git`
* Run code using  `python ticket-generator.py --quantity [number of tickets generated] --header [Text on ticket header]`
  
### Example

`python ticket-generator.py --quantity 2`

![Ticket Example](resources/ticket_example.png)


[References](https://github.com/jamesshah/housie-tickets-generator)
