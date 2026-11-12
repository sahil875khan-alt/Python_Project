def book_ticket(availabel_seats,seats_wanted):
    if seats_wanted > availabel_seats:
        raise ValueError(f"Sorry, Only {availabel_seats} seats is availabel , {seats_wanted} seats cann't buy!")
    if seats_wanted <=0:
        raise ValueError("At least 1 seats should be confirmed!")
    return
try:
    availabel_seats = 10
    seats_wanted = int(input("Enter the booking seat numbers:"))
    book_ticket(availabel_seats,seats_wanted)
except ValueError as i:
    print("Error:",i)
else:
    print("Ticket confirmed!")    
