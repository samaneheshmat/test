#Samaneh Heshmatzadeh Lab2


def get_retail_item_description():
    """This function gets the name of the item
    :return: item name
    """
    return input("Enter the retail item description: ")


def get_number_of_purchased_items():
    """This function gets the number of item purchased
    :return: number of item purchased
    """
    return float(input("Enter quantity purchased: "))


def get_price_usd_per_unit():
    """This function gets the price per item
     :return: price per unit
    """
    return float(input("Enter price per unit: "))


def get_tax_rate():
    """This function gets the tax rate
    :return: tax rate
    """
    return float(input("Enter tax: "))


def calculate_subtotal_usd(price, quantity):
    """This function calculates the subtotal price
    :param price: price of item
    :param quantity: quantity of items
    :return: subtotal
    """
    return price*quantity


def calculate_tax_usd(subtotal, tax):
    """This function calculates the total tax
    :param subtotal: subtotal in USD
    :param tax: tax rate
    :return: total tax
    """
    return subtotal*tax


def calculate_total_usd(subtotal, tax):
    """This function calculates the total price
    :param subtotal: subtotal in USD
    :param tax: tax rate
    :return: total price
     """
    return subtotal*(1.0+tax)


def main():
    item_description = get_retail_item_description()
    quantity_purchased = get_number_of_purchased_items()
    unit_price = get_price_usd_per_unit()
    tax_rate = get_tax_rate()
    subtotal_price = calculate_subtotal_usd(unit_price, quantity_purchased)
    tax_total = calculate_tax_usd(subtotal_price, tax_rate)
    total_price = calculate_total_usd(subtotal_price, tax_rate)

    print("Sales Receipt:")
    print("Item Description: ", item_description)
    print("Number of Purchased Items: ", int(quantity_purchased))
    print("Unit Price:", unit_price)
    print("Tax Rate: ", tax_rate)
    print("Subtotal:", subtotal_price)
    print("Tax:", tax_total)
    print("Total:", total_price)


if __name__ == "__main__":
    main()



