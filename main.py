class Category:
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.ledger = []

    def __str__(self):
        x = 0
        string = self.name
        output = string.center(30, '*')
        total = f"\nTotal: {self.get_balance():.2f}"
        while x < len(self.ledger):
            item = self.ledger[x]
            output += f"\n{item['description']:<23.23}{item['amount']:>7.2f}"
            x += 1

        return output + total

    def deposit(self, amount, description=""):
        self.amount += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.amount -= amount
            #print("withdraw sucess")
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            #print("withdraw failed")
            return False

    def get_balance(self):
        return self.amount

    def transfer(self, amount, target):
        if self.check_funds(amount):
            description = f"Transfer to {target.name}"
            target.deposit(amount, f"Transfer from {self.name}")
            self.amount -= amount
            self.ledger.append({"amount": -amount, "description": description})
            #print("Transfer sucessful")
            return True
        else:
            #print("Transfer failed")
            return False

    def check_funds(self, amount):
        if self.amount >= amount:
            return True
        else:
            return False

    def get_total(self):
        lista = []
        total = 0
        for i in self.ledger:
            if i['amount'] < 0:
                total += i['amount']
        lista.append({f"{self.name}": total})

        return lista


def create_spend_chart(categories):
    totals = 0
    percent = []
    percent_rounded = []
    for item in categories:
        for i in item.get_total():
            totals += i[f'{item.name}']

    for item in categories:
        for i in item.get_total():
            percent.append({'item': item.name, 'percent': (i[f'{item.name}'] / totals) * 100})

    for i in percent:
        num = round(i['percent'], 2)
        percent_rounded.append({'item': i['item'], 'percent': num})
        print(num)

    for i in percent_rounded:
        aux = int(i['percent'] / 10)
        # print("o" * aux + f"==={i['item']}")

    header = "Percentage spent by category\n"
    chart = ""

    for num in reversed(range(0, 101, 10)):
        chart += str(num).rjust(3) + '|'
        for percent in percent_rounded:
            if percent['percent'] >= num:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    category_names = list(map(lambda category: category.name, categories))
    max_length = max(map(lambda description: len(description), category_names))
    names_vertical = list(map(lambda description: description.ljust(max_length), category_names))
    for x in zip(*names_vertical):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"
    return (header + chart + footer).rstrip("\n")





food = Category("food")
entertainment = Category("entertainment")
business = Category("business")
categories = [entertainment, food, business]
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart(categories))





