class Movie:
    name: str
    description: str
    year: int
    tickets: int

    def __init__(self, name: str, year: int, description: str, tickets: int = 10):
        self.name = name
        self.year = year
        self.description = description
        self.tickets = tickets

    def  print_tickets(self):
        if self.tickets > 0:
            return ("Залишилось %d білетів" % self.tickets)
        else:
            return ("Білети закінчились")

