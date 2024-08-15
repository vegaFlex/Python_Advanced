def accommodate(*guest_groups, **rooms):
    # Convert room keys to integers and sort rooms by capacity and room number
    sorted_rooms = sorted(
        ((int(k.split('_')[1]), v) for k, v in rooms.items()),
        key=lambda x: (x[1], x[0])
    )

    # Dictionary to hold which room accommodates which group
    accommodations = {}

    # Track the number of unaccommodated guests
    unaccommodated_guests = 0

    for guests in guest_groups:
        best_fit_room = None

        # Look for the best fit room
        for room_number, capacity in sorted_rooms:
            if capacity >= guests:
                best_fit_room = (room_number, capacity)
                break

        # Accommodate the group if a suitable room is found
        if best_fit_room:
            room_number, _ = best_fit_room
            accommodations[room_number] = guests
            sorted_rooms = [r for r in sorted_rooms if r[0] != room_number]
        else:
            unaccommodated_guests += guests

    # Prepare the output
    result = []

    if accommodations:
        result.append(f"A total of {len(accommodations)} accommodations were completed!")
        for room_number in sorted(accommodations.keys()):
            result.append(f"<Room {room_number} accommodates {accommodations[room_number]} guests>")
    else:
        result.append("No accommodations were completed!")

    if unaccommodated_guests > 0:
        result.append(f"Guests with no accommodation: {unaccommodated_guests}")

    if sorted_rooms:
        result.append(f"Empty rooms: {len(sorted_rooms)}")

    return '\n'.join(result)

