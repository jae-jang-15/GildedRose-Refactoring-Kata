# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        item1 = Item("Conjured", 0, 2)
        item2 = Item("Sulfuras", 3, 3)
        item3 = Item("Aged Brie", 10, 8)
        self.items = [item1, item2, item3]
        self.gilded_rose = GildedRose(self.items)
        print(f"setUp: {item1}, {item2}, {item3} created in {self.items}")

    def tearDown(self):
        self.items = None
        self.gilded_rose = None
        print("tearDown: resource cleaned")

    def test_gilded_rose_conjured(self):      
        self.assertEqual("Conjured", self.items[0].name)
        self.assertEqual(0,self.items[0].sell_in)
        self.assertEqual(2,self.items[0].quality)

        self.gilded_rose.update_quality()
        self.assertEqual("Conjured", self.items[0].name)
        self.assertEqual(-1,self.items[0].sell_in)
        self.assertEqual(0,self.items[0].quality)


    def test_gilded_rose_sulfuras(self):
        self.assertEqual("Sulfuras", self.items[1].name)
        self.assertEqual(3, self.items[1].sell_in)
        self.assertEqual(3, self.items[1].quality)

        self.gilded_rose.update_quality()
        self.assertEqual(3, self.items[1].sell_in)
        self.assertEqual(3, self.items[1].quality)

    def test_gilded_rose_aged_brie(self):
        self.assertEqual("Aged Brie", self.items[2].name)
        self.assertEqual(10,self.items[2].sell_in)
        self.assertEqual(8,self.items[2].quality)

        self.gilded_rose.update_quality()
        self.assertEqual("Aged Brie", self.items[2].name)
        self.assertEqual(9,self.items[2].sell_in)
        self.assertEqual(9,self.items[2].quality)


        
if __name__ == '__main__':
    unittest.main()
