import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
<<<<<<< HEAD
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quotes['stock'], quotes['top_bid']['price'], quotes['top_ask']['price'], (quotes['top_bid']['price'] + quotes['top_ask']['price']) / 2))
=======

>>>>>>> origin/main
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
<<<<<<< HEAD
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quotes['stock'], quotes['top_bid']['price'], quotes['top_ask']['price'], (quotes['top_bid']['price'] + quotes['top_ask']['price']) / 2))
=======

>>>>>>> origin/main

  """ ------------ Add more unit tests ------------ """


<<<<<<< HEAD
=======

>>>>>>> origin/main
if __name__ == '__main__':
    unittest.main()
