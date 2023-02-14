from django.test import TestCase
from app import models as m

# Create your tests here.


class TaxiTestCase(TestCase):
    def test_can_create_taxi(self):
        taxi = m.create_taxi(False, 4, 1.5, 0)
        taxi2 = m.create_taxi(False, 4, 2.5, 0)
        taxi3 = m.create_taxi(False, 6, 3, 0)

        self.assertEqual(taxi.id, 1)
        self.assertEqual(taxi.occupied, False)
        self.assertEqual(taxi.capacity, 4)
        self.assertEqual(taxi.fare, 1.5)
        self.assertEqual(taxi.passengers, 0)
        self.assertEqual(taxi.notes, "")
        self.assertEqual(taxi.taxi_number, 111)

        self.assertEqual(taxi2.id, 2)
        self.assertEqual(taxi2.occupied, False)
        self.assertEqual(taxi2.capacity, 4)
        self.assertEqual(taxi2.fare, 2.5)
        self.assertEqual(taxi2.passengers, 0)
        self.assertEqual(taxi2.notes, "")
        self.assertEqual(taxi2.taxi_number, 122)

        self.assertEqual(taxi3.id, 3)
        self.assertEqual(taxi3.occupied, False)
        self.assertEqual(taxi3.taxi_number, 133)

    def test_remove_taxi(self):
        taxi = m.create_taxi(False, 4, 1.5, 0)
        taxi2 = m.create_taxi(False, 4, 2.5, 0)
        taxi3 = m.create_taxi(False, 6, 3, 0)

        self.assertEqual(taxi.taxi_number, 111)
        self.assertEqual(taxi2.taxi_number, 122)
        self.assertEqual(taxi3.taxi_number, 133)

        taxis_before = m.all_taxis()

        self.assertEqual(len(taxis_before), 3)

        m.remove_taxi(111)

        taxis_after = m.all_taxis()

        self.assertNotEqual(len(taxis_before), len(taxis_after))
        self.assertEqual(len(taxis_after), 2)

    def test_remove_taxi_not_exist(self):
        with self.assertRaises(ValueError):
            m.remove_taxi(111)

    def test_filter_free_taxis(self):
        taxi = m.create_taxi(True, 4, 1.5, 0)
        taxi2 = m.create_taxi(False, 4, 2.5, 0)
        taxi3 = m.create_taxi(False, 6, 3, 0)

        self.assertEqual(len(m.filter_free_taxis()), 2)

    def test_filter_free_taxis_and_capacity(self):
        taxi = m.create_taxi(True, 6, 1.5, 0)
        taxi2 = m.create_taxi(False, 4, 2.5, 0)
        taxi3 = m.create_taxi(False, 6, 3, 0)

        self.assertEqual(len(m.filter_free_capacity_taxis(5)), 1)

    def test_finish_fare(self):
        taxi = m.create_taxi(True, 4, 2, 3)
        taxi2 = m.create_taxi(False, 4, 2.5, 0)
        taxi3 = m.create_taxi(False, 6, 3, 0)

        self.assertEqual(m.finish_fare(111, 10), 20)

    def test_finish_fare_not_occupied(self):
        taxi2 = m.create_taxi(False, 4, 2.5, 0)

        with self.assertRaises(ValueError):
            cost = m.finish_fare(111, 10)

    def test_send_taxi_out(self):
        taxi = m.create_taxi(True, 4, 2, 3)
        taxi2 = m.create_taxi(False, 4, 2.5, 0)
        taxi3 = m.create_taxi(False, 6, 3, 0)

        self.assertEqual(taxi2.occupied, False)
        self.assertEqual(taxi2.passengers, 0)

        taxi2 = m.send_taxi_out(122, 3)

        self.assertEqual(taxi2.occupied, True)
        self.assertEqual(taxi2.passengers, 3)

    def test_send_taxi_out_too_many_passengers(self):
        taxi = m.create_taxi(True, 4, 2, 3)
        taxi2 = m.create_taxi(False, 4, 2.5, 0)
        taxi3 = m.create_taxi(False, 6, 3, 0)

        self.assertEqual(taxi2.occupied, False)
        self.assertEqual(taxi2.passengers, 0)

        with self.assertRaises(ValueError):
            taxi2 = m.send_taxi_out(122, 7)
