
from itertools import islice
import random
import numpy as np
import argparse
from flask import Flask
from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__)


def get_tickets():

    # Create a 2D array [3x9] of 0s
    ticket_array = np.zeros((3, 9), dtype=int)

    # Create an a list of numbers from 1 to 90.
    total_numbers = [num for num in range(1, 90)]
    it = iter(total_numbers)
    li = [9, 10, 10, 10, 10, 10, 10, 10, 10]
    total_numbers = [list(islice(it, elem)) for elem in li]

    # Create a list of tuple of all the indices of 3x9 ticket_array . i.e (0,0),(0,1),...,(2,8)
    total_indices = [(i, j) for i in range(3) for j in range(9)]

    first_row = random.sample(total_indices[:9], 5)
    second_row = random.sample(total_indices[9:18], 5)
    third_row = random.sample(total_indices[-9:], 5)

    cols = [[] for i in range(9)]
    for i in range(9):
        if (0, i) in first_row:
            cols[i].append(0)
        if (1, i) in second_row:
            cols[i].append(1)
        if (2, i) in third_row:
            cols[i].append(2)

    for i in range(9):
        data = sorted(random.sample(total_numbers[i],len(cols[i])))
        for j in range(len(cols[i])):
            ticket_array[cols[i][j]][i] = data[j]

    return ticket_array


@app.route('/')
def ticket_server():
    template = env.get_template('ticket_template.html')
    no_of_tickets = args.quantity
    tickets = []
    for i in range(no_of_tickets):
        ticket = get_tickets()
        tickets.append(ticket)
    ll = [i for i in range(1, len(tickets)+1)]
    tickets = tuple(zip(tickets, ll))
    final_output = template.render(tickets=tickets, header=args.header)
    return final_output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=" arguments for tambola ticket-generator")
    parser.add_argument('--quantity', type=int, help="quanity of tickets")
    parser.add_argument('--header', type=str, help="this text will be printed on top of tickets", default="Ticket")
    args = parser.parse_args()
    app.run(debug=True)

