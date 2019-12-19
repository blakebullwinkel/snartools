#!/usr/bin/env python3
# (c) 2017 J. Blake Bullwinkel
"""
Snartools is a module that provides a collection of tools to help users optimize their snack bar orders.
Refer to the docstrings below for a descriptions of the functionality of each tool, and see 'usetools.py' 
for an example of an interface in which these tools are implemented. 
"""

import csv
import itertools


class Item(object):
    __slots__ = ["_canteen", "_submenu", "_dish", "_price"]

    def __init__(self, canteen, submenu, dish, price):
        self._canteen = canteen
        self._submenu = submenu
        self._dish = dish
        self._price = float(price)

    def getCanteen(self):
        return self._canteen

    def getSubmenu(self):
        return self._submenu

    def getDish(self):
        return self._dish

    def getPrice(self):
        return self._price

    def __len__(self):
        return 1

    def __eq__(self, other):
        return (self._dish == other._dish) and \
               (self._price == other._price)

    def __repr__(self):
        return "Item({0},{1},{2},{3})".format(self._canteen, self._submenu, self._dish, self._price)

    def __str__(self):
        return "<{0},{1},{2},{3}>".format(self._canteen, self._submenu, self._dish, self._price)


class Menu(object):
    __slots__ = ["_canteen", "_result"]

    def __init__(self, canteen=None):
        self._result = []
        if canteen != None:
            self._canteen = canteen
            with open(self._canteen + '.csv', 'r') as f:
                csvr = csv.reader(f)
                for row in csvr:
                    item = Item(row[0], row[1], row[2], row[3])
                    self._result.append(item)

    def getCanteen(self):
        return self._canteen

    def getSubmenus(self):
        submenus = []
        for item in self._result:
            if item._submenu not in submenus:
                submenus.append(item._submenu)
        return submenus

    def getDishes(self):
        dishes = []
        for item in self._result:
            dishes.append(item._dish)
        s = ', '
        return s.join(dishes)

    def getPrices(self):
        prices = []
        for item in self._result:
            if item._price not in prices:
                prices.append(item._price)
        return prices

    def specifySubmenus(self, submenus):
        items = []
        for item in self._result:
            if item._submenu in submenus:
                items.append(item)
        self._result = items

    def sortMenu(self):
        return sorted(self._result, key=lambda x: x._price)

    def longestOrder(self, price):
        sortedMenu = self.sortMenu()
        minPrice = sortedMenu[0]._price
        return int(price / minPrice)

    def shortestOrder(self, price):
        sortedMenu = self.sortMenu()
        maxPrice = sortedMenu[-1]._price
        return int(price / maxPrice)

    def longOrder(self, price, sortedMenu=None):
        if sortedMenu == None:
            sortedMenu = self.sortMenu()
        sum = 0
        order = []
        for item in sortedMenu:
            if sum + item._price <= price:
                order.append(item._dish)
                sum += item._price
        return order

    def lengthExact(self, length):
        orders = []
        maxLen = len(self.longOrder(7))
        assert length == int(length) and 0 < length <= maxLen
        sortedMenu = self.sortMenu()
        maxPrice = 7 - (length - 1) * sortedMenu[0]._price
        for item in sortedMenu:
            if item._price > maxPrice:
                sortedMenu.remove(item)
        allCombos = list(itertools.combinations_with_replacement(sortedMenu, length))
        for combo in allCombos:
            sum = 0
            for item in combo:
                sum += item._price
            if sum <= 7:
                orders.append(combo)
        return orders

    def lengthRange(self, lower, upper):
        allCombos = []
        orders = []
        maxLen = self.longestOrder(7)
        assert lower == int(lower) and upper == int(upper) and 0 < lower <= upper <= maxLen
        sortedMenu = self.sortMenu()
        for i in range(lower, upper + 1):
            maxPrice = 7 - (i - 1) * sortedMenu[0]._price
            for item in sortedMenu:
                if item._price > maxPrice:
                    sortedMenu.remove(item)
            allCombos += list(itertools.combinations_with_replacement(sortedMenu, i))
        for combo in allCombos:
            sum = 0
            for item in combo:
                sum += item._price
            if sum <= 7:
                orders.append(combo)
        return orders

    def priceExact(self, price):
        allCombos = []
        orders = []
        assert 0 < price <= 7
        sortedMenu = self.sortMenu()
        cheapestPrice = sortedMenu[0]._price
        maxLen = self.longestOrder(price)
        minLen = self.shortestOrder(price)
        for i in range(minLen, maxLen + 1):
            if i == 1:
                for item in self._result:
                    if item._price == price:
                        orders.append(item)
                        sortedMenu.remove(item)
            else:
                maxPrice = price - (i - 1) * cheapestPrice
                for item in sortedMenu:
                    if item._price > maxPrice:
                        sortedMenu.remove(item)
                allCombos += list(itertools.combinations_with_replacement(sortedMenu, i))
        for combo in allCombos:
            sum = 0
            for item in combo:
                sum += item._price
            if sum == price:
                orders.append(combo)
        return orders

    def priceRange(self, lower, upper):
        allCombos = []
        orders = []
        assert 0 < lower <= upper <= 7
        sortedMenu = self.sortMenu()
        cheapestPrice = sortedMenu[0]._price
        maxLen = self.longestOrder(upper)
        minLen = self.shortestOrder(upper)
        for i in range(minLen, maxLen + 1):
            if i == 1:
                for item in self._result:
                    if item._price >= lower and item._price <= upper:
                        orders.append(item)
            else:
                maxPrice = upper - (i - 1) * cheapestPrice
                for item in sortedMenu:
                    if item._price > maxPrice:
                        sortedMenu.remove(item)
                allCombos += list(itertools.combinations_with_replacement(sortedMenu, i))
        for combo in allCombos:
            sum = 0
            for item in combo:
                sum += item._price
            if sum >= lower and sum <= upper:
                orders.append(combo)
        return orders

    def moreExact(self, order, price):
        orderPrice = 0
        for item in self._result:
            if item in order:
                orderPrice += item._price
        assert orderPrice <= price <= 7
        remaining = price - orderPrice
        return self.priceExact(remaining)

    def moreRange(self, order, lower, upper):
        orderPrice = 0
        for item in self._result:
            if item in order:
                orderPrice += item._price
        assert lower <= upper <= 7 and orderPrice < upper
        low = lower - orderPrice
        high = upper - orderPrice
        return self.priceRange(low, high)

    def append(self, value):
        return self._result.append(value)

    def remove(self, value):
        return self._result.remove(value)

    def getCopy(self):
        return self._result.copy()

    def __iter__(self):
        return iter(self._result)

    def __len__(self):
        return len(self._result)

    def __repr__(self):
        return "Menu({})".format(self._result)

    def __str__(self):
        return "{}".format(self._result)