class Train:
    amount_paid = False;

    def __init__(self,train_name,seats):
        self.train_name = train_name;
        self.seats = seats;

    def getFare(self):
        return 800 * self.seats;

    def bookTicket(self):
        self.amount_paid = True;

    def getStatus(self):
        if self.amount_paid:
            print(f"Your {self.seats} seats are successfully booked in train {self.train_name}.");
        else:
            print("You have not booked the ticket");


train_1 = Train("Rajdhani",2);
print(train_1.getFare());
train_1.bookTicket();
train_1.getStatus();


