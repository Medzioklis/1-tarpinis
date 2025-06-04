from datetime import datetime, timedelta
class Basket():
    def __init__(self, basket_id):
        self.basket_id = basket_id
        self.barrowed_books = []
        self.created_at = datetime.now().strftime("%Y-%m-%d")