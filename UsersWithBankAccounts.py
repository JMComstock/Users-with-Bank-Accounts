class User:
    def __init__(self, name, email):
        self.username = name
        self.email = email
        self.account = BankAccount (int_rate=0.02, balance = 0)
        self.balance = 0

    # def example_method(self):
    #     self.account.deposit(100)
    #     print(self.account.balance)

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("Insufficient funds to make a withdrawl")
        return self

    def transfer_money(self, other_user, amount):
        if self.balance < amount:
            print("insifficient funds to make transfer")
        else:
            self.balance -= amount
            other_user.balance += amount
        print("You have successfully transfered the funds")

    def display_user_balance(self):
        print(f"Username: {self.username}, Balance: {self.balance}")

class BankAccount:
	def __init__(self, int_rate, balance = 0):
		self.rate = int_rate
		self.account = balance

	# def deposit(self, amount):
	# 	self.account += amount
	# 	return self
	
	# def withdraw(self, amount):
	# 	self.account -= amount
	# 	if self.account < amount:
	# 		print("Insufficient funds: Charging a $5 fee")
	# 		self.account -= 5
	# 	return self

	# def display_account_info(self):
	# 	print(f"Balance: {self.balance}")
	# 	return self
	
	def yield_interest(self):
		if self.balance > 0:
			self.balance = self.balance * (self.rate)+self.balance
		return self




user1 = User("Ron" , "ron@email.com")
user2 = User("Missy", "missy@email.com")
user3 = User("Jason", "jason@email.com")

user1.make_deposit(100).make_withdrawl(20).display_user_balance()
# user2.make_deposit(600).make_deposit(100).make_withdrawl(50).make_withdrawl(50).display_user_balance()
# user3.make_deposit(1000).make_withdrawl(20).make_withdrawl(200).make_withdrawl(50).display_user_balance()


# user1.transfer_money(user3, 40)

# user1.display_user_balance()

# user1.display_user_balance()
# user2.display_user_balance()
# user3.display_user_balance()

