class Customer(object):
    def __init__(self, name, address, phone_no):
        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.id = None
        self.restaurant = None
        self.orderedItems = {}
        self.total_cost = 0
        self.waiter = None
        self.table = None
        self.paymentStatus = False

    def OrderFood(self, food_menu, quantity):
        if self.restaurant != None:
            self.orderedItems[food_menu.name] = quantity
            if self.waiter == None:
                self.restaurant.assignWaiter(self)
            if self.table == None:
                self.restaurant.reserveTable(self)
            self.total_cost += food_menu.price*quantity


    def MakePayment(self):
        choice = int(input("\nEnter: \n\t1. Cash Payment \n\t2. Card Payment\n\t"))
        print(choice)
        while choice != 1 and choice !=2:
            choice = int(input("\nEnter: \n\t1. Cash Payment \n\t2. Card Payment\n\t"))
            print(choice)
        if choice == 1:
            cash_pay= CashPayment(self)
            cash_pay.paid(self)
            self.restaurant.payments.append(cash_pay)
        if choice == 2:
            card_number = input("\nEnter Card Number: ")
            bank_name = input("\nEnter Bank name: ")
            card_pay = CardPayment(self, card_number, bank_name)
            card_pay.paid(self)
            self.restaurant.payments.append(card_pay)
    
    def checkIn(self, res):
        res.setCustomer(self)
        self.restaurant = res

    def checkOut(self, res):
        if self.paymentStatus == False and self.total_cost > 0:
            print("Customer: {1} => Please Pay: {0} Then CheckOut!".format(self.total_cost, self.name))
        else:
            self.restaurant = None
            if self.waiter != None:
                self.waiter.getFreed()
                self.waiter = None
            if self.table !=None:
                self.table.getFreed()
                self.table = None
            if self in res.customer:
                res.removeCustomer(self)

class Payment(object):
    def __init__(self, cus):
        self.customer_name = cus.name
        self.total_cost = cus.total_cost

    def paid(self, cus):
        cus.paymentStatus = True

class CardPayment(Payment):
    def __init__(self, cus, card_number, bank_name):
        self.card_number = card_number
        self.bank_name = bank_name
        self.payment_type = "Card"
        super(CardPayment, self).__init__(cus)

class CashPayment(Payment):
    def __init__(self, cus):
        self.payment_type = "Cash"
        super(CashPayment, self).__init__(cus)


class Order(object):
    def __init__(self, order_id, order_type, order_items):
        self.order_id = order_id
        self.order_type = order_type
        self.order_items = order_items
        self.order_status = None

    
    def makeOrder(self):
        pass

class OnlineDelivery(Order):
    def __init__(self, address, order_id, order_type, order_items):
        self.deliveryAddress = address
        self.deliveryStatus = None
        super(OnlineDelivery, self).__init__(order_id, order_type, order_items)

    def Delivered(self):
        pass

class ServeOnTable(Order):
    def __init__(self, address, order_id, order_type, order_items):
        super(ServeOnTable, self).__init__(order_id, order_type, order_items)

    def Served(self):
        pass


class Restaurant(object):
    def __init__(self, name, location, city):
        self.name = name
        self.location = location
        self.city = city
        self.incID = 0
        self.customer = []
        self.menu = []
        self.waiterList = [Waiter(i,"Waiter "+ str(i)) for i in range(1, 11)]
        self.tableList = [Table(i) for i in range(1, 11)]
        self.payments = []

    def assignWaiter(self, cus):
        for w in self.waiterList:
            if w.isFreed():
                w.getAssigned()
                cus.waiter = w
                return
        print("No Waiter is Free Now")
            
            

    def reserveTable(self, cus):
        for t in self.tableList:
            if t.isFreed():
                t.assign()
                cus.table = t
                return
        print("No Table is Free Now")

    def receiveBill(self, cus):
        if cus.paymentStatus == False or cus.total_cost > 0:
            cus.MakePayment()
            print("Customer {0} paid: {1}.".format(cus.name, cus.total_cost))
        else:
            print("No Bill for Customer {0}".format(cus.name))
    
    def printBill(self, cus):
        print("Customer Bill:\n Name: {0}".format(cus.name))
        for item_key in cus.orderedItems:
            print("Item: {0} Q: {1}".format(item_key, cus.orderedItems[item_key]))
        print("Total Cost: ", cus.total_cost)

    def setCustomer(self, cus):
        cus.id = self.incID
        self.incID +=1
        self.customer.append(cus)

    def removeCustomer(self, cus):
        self.customer.remove(cus)

    def addMenu(self, menu):
        self.menu.append(menu)



class Waiter(object):
    def __init__(self,id, name):
        self.id = id
        self.name = name
        self.isFree = True

    def getAssigned(self):
        self.isFree = False

    def isFreed(self):
        if self.isFree == True:
            return True
        else:
            return False

    def getFreed(self):
        self.isFree = True

    def receiveOrder(self):
        pass

class DeliveryBoy(Waiter):
    def __init__(self, id, name):
        self.deliveryStatus = None
        super(DeliveryBoy, self).__init__(id, name)

    def getDeliveryAddress(self):
        pass

class OwnWaiter(Waiter):
     def __init__(self, id, name):
        self.orderStatus = None
        super(OwnWaiter, self).__init__(id, name)
    

class Table(object):
    def __init__(self, id):
        self.id = id
        self.isFree = True
    
    def isFreed(self):
        if self.isFree == True:
            return True
        else:
            return False

    def assign(self):
        self.isFree = False

    def getFreed(self):
        self.isFree = True
        
class FoodMenu(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Drinks(FoodMenu):
    def __init__(self, name, price):
        self.item_type = "Drinks"
        super(Drinks, self).__init__(name, price)

class Snacks(FoodMenu):
    def __init__(self, name, price):
        self.item_type = "Snacks"
        super(Snacks, self).__init__(name, price)

class Main_Food(FoodMenu):
    def __init__(self, name, price):
        self.item_type = "Main Food"
        super(Main_Food, self).__init__(name, price)

if __name__ == "__main__":
    cus = Customer("Khan", "Dhaka", '0181xxxxxxxxx')
    cus1 = Customer("Chowdury", "Noakhali", '0181xxxxxxxxx')
    cus2 = Customer("Hossain", "Kishorgonj", '0181xxxxxxxxx')
    cus3 = Customer("Kamal", "Rangpur", '0181xxxxxxxxx')
    res = Restaurant("Sonargoan", "Kawran Bazar", "Dhaka")
    cus.checkIn(res)
    cus1.checkIn(res)
    cus2.checkIn(res)
    cus3.checkIn(res)
    i = 0
    print("Restaurant", res.name, "has Customer:\n")
    for r in res.customer:
        print("Name: {0} \tAddress: {1}.".format (res.customer[i].name, res.customer[i].address))
        i += 1
    cus.checkOut(res)
    i = 0
    print("Restaurant", res.name, "has Customer:\n")
    for r in res.customer:
        print("Name: {0} \tAddress: {1}.".format (res.customer[i].name, res.customer[i].address))
        i += 1
    
    drinks_cocaCola = Drinks("Coca Cola", 50)
    drinks_mountain_due = Drinks("Mountain Due", 30)
    drinks_lachchi = Drinks("Lachchi", 70)

    snacks_burger = Snacks("Burgur", 350)
    snacks_sandwich = Snacks("Sandwich", 150)
    snacks_shworma = Snacks("Shworma", 250)

    main_food_kachchi = Main_Food("Kachchi", 450)
    main_food_Biriani = Main_Food("Haydrabadi Biriyani", 400)
    main_food_morog_polao = Main_Food("Morog Polao", 380)

    res.addMenu(drinks_cocaCola)
    res.addMenu(drinks_mountain_due)
    res.addMenu(drinks_lachchi)
    res.addMenu(snacks_burger)
    res.addMenu(snacks_sandwich)
    res.addMenu(snacks_shworma)
    res.addMenu(main_food_kachchi)
    res.addMenu(main_food_Biriani)
    res.addMenu(main_food_morog_polao)

    i = 0
    print("Resraurant has Menu: \n")
    for m in res.menu:
        print("NAME: {0} \t TYPE: {1} \t PRICE: {2}"
        .format(res.menu[i].name, res.menu[i].item_type,res.menu[i].price))
        i +=1

    for w in res.waiterList:
        print(w.name, w.id, w.isFree)
    for t in res.tableList:
        print( t.id, t.isFree)

    cus.OrderFood(drinks_cocaCola, 2)
    cus.OrderFood(snacks_sandwich, 2)
    cus.OrderFood(main_food_Biriani, 3)
    cus1.OrderFood(snacks_sandwich, 2)
    cus1.OrderFood(main_food_Biriani, 3)
    cus2.OrderFood(main_food_Biriani, 3)

    for w in res.waiterList:
        print(w.name, w.id, w.isFree)
    for t in res.tableList:
        print( t.id, t.isFree)
        
    res.printBill(cus1)
    res.receiveBill(cus1)
    cus1.checkOut(res)

    res.printBill(cus2)
    res.receiveBill(cus2)
    cus2.checkOut(res)

    res.printBill(cus3)
    res.receiveBill(cus3)
    cus3.checkOut(res)

    for c in res.customer:
        print("\nCustomer name: {0} has Total Cost: {1}.".format(c.name, c.total_cost))
        print("Ordered: ")
        for item_key in c.orderedItems.keys():
            print(item_key,"*", c.orderedItems[item_key])

    print("Total payments for restaurant:")
    for p in res.payments:
        if p.payment_type == "Cash":
            print("Customer Name: {0}, Paid: {1} by Cash".format(p.customer_name, p.total_cost))
        if p.payment_type == "Card":
            print("Customer Name: {0}, Paid: {1} by Card Number: {2} bank: {3}".format(p.customer_name, p.total_cost, p.card_number, p.bank_name))
        




    

    