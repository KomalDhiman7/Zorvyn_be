class Record:
    def __init__(self, id, amount, type, category, date, notes, user_id):
        self.id = id
        self.amount = amount
        self.type = type
        self.category = category
        self.date = date
        self.notes = notes
        self.user_id = user_id