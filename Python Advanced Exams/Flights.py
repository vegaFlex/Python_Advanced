def flights(*args):
    params = list(args)

    destinations = {}

    while True:

        destination = params.pop(0)
        if destination == 'Finish':
            return destinations

        passengers = params.pop(0) if args else ''

        if destination not in destinations:
            destinations[destination] = 0
        destinations[destination] += passengers


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))