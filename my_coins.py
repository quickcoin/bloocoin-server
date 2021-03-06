# -*- coding: utf-8 -*-
import mongo
import command


class MyCoins(command.Command):
    """ Allows users to check the amount of coins
        under their account.

        fingerprint: {"cmd": "my_coins", "addr": _, "pwd": _}
    """
    required = ['addr', 'pwd']

    def handle(self, *args, **kwargs):
        addr = self.data['addr']
        pwd = self.data['pwd']
        if mongo.db.addresses.find_one({"addr": addr, "pwd": pwd}):
            coins = coins = mongo.db.coins.find({"addr": addr}).count()
            self.success({"amount": coins})
            return
        else:
            self.error("Your address or password was invalid")
