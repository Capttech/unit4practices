from django.test import TestCase
from app import models as m

# Create your tests here.
class Test_Airline(TestCase):
    def test_create_ticket(self):
        ticket = m.create_ticket("2023-02-11", "Philadelphia", "Tom")
        ticket2 = m.create_ticket("2023-02-12", "Philadelphia", "Drew", 2)
        ticket3 = m.create_ticket("2023-02-14", "Boston", "Bryan", 1)
        ticket4 = m.create_ticket("2023-02-12", "Chicago", "Anthony")
        ticket5 = m.create_ticket("2023-02-11", "Dallas", "Eddie", 3)

        self.assertEqual(ticket3.id, 3)
        self.assertEqual(ticket3.date, "2023-02-14")
        self.assertEqual(ticket3.destination, "Boston")
        self.assertEqual(ticket3.passenger, "Bryan")
        self.assertEqual(ticket3.bags, 1)
        self.assertFalse(ticket3.firstclass)

        self.assertEqual(ticket.bags, 0)

    def test_find_ticket_bryan(self):
        ticket = m.create_ticket("2023-02-11", "Philadelphia", "Tom")
        ticket2 = m.create_ticket("2023-02-12", "Philadelphia", "Drew", 2)
        ticket3 = m.create_ticket("2023-02-14", "Boston", "Bryan", 1)
        ticket4 = m.create_ticket("2023-02-12", "Chicago", "Anthony")
        ticket5 = m.create_ticket("2023-02-11", "Dallas", "Eddie", 3)

        found_ticket = m.find_ticket(3)

        self.assertEqual(ticket3, found_ticket)

    def test_find_ticket_error(self):
        with self.assertRaises(ValueError):
            ticket = m.find_ticket(9000)

    def test_upgrade_firstclass_Tom(self):
        ticket = m.create_ticket("2023-02-11", "Philadelphia", "Tom")
        ticket2 = m.create_ticket("2023-02-12", "Philadelphia", "Drew", 2)
        ticket3 = m.create_ticket("2023-02-14", "Boston", "Bryan", 1)
        ticket4 = m.create_ticket("2023-02-12", "Chicago", "Anthony")
        ticket5 = m.create_ticket("2023-02-11", "Dallas", "Eddie", 3)

        ticket = m.upgrade_firstclass(1)

        self.assertTrue(ticket.firstclass)

    def test_upgrade_firstclass_error(self):
        ticket = m.create_ticket("2023-02-11", "Philadelphia", "Tom")
        ticket2 = m.create_ticket("2023-02-12", "Philadelphia", "Drew", 2)
        ticket3 = m.create_ticket("2023-02-14", "Boston", "Bryan", 1)
        ticket4 = m.create_ticket("2023-02-12", "Chicago", "Anthony")
        ticket5 = m.create_ticket("2023-02-11", "Dallas", "Eddie", 3)

        ticket = m.upgrade_firstclass(1)

        self.assertTrue(ticket.firstclass)

        with self.assertRaises(ValueError):
            ticket = m.upgrade_firstclass(1)

    def test_delete_ticket(self):
        ticket = m.create_ticket("2023-02-11", "Philadelphia", "Tom")
        ticket2 = m.create_ticket("2023-02-12", "Philadelphia", "Drew", 2)
        ticket3 = m.create_ticket("2023-02-14", "Boston", "Bryan", 1)
        ticket4 = m.create_ticket("2023-02-12", "Chicago", "Anthony")
        ticket5 = m.create_ticket("2023-02-11", "Dallas", "Eddie", 3)

        tickets = m.all_tickets()

        self.assertEqual(len(tickets), 5)

        m.delete_ticket(5)
        m.delete_ticket(3)

        new = m.all_tickets()

        self.assertNotEqual(tickets, new)
        self.assertEqual(len(new), 3)

    def test_all_tickets(self):
        ticket = m.create_ticket("2023-02-11", "Philadelphia", "Tom")
        ticket2 = m.create_ticket("2023-02-12", "Philadelphia", "Drew", 2)
        ticket3 = m.create_ticket("2023-02-14", "Boston", "Bryan", 1)
        ticket4 = m.create_ticket("2023-02-12", "Chicago", "Anthony")
        ticket5 = m.create_ticket("2023-02-11", "Dallas", "Eddie", 3)

        test_list = [ticket, ticket2, ticket3, ticket4, ticket5]

        self.assertEqual(len(test_list), len(m.all_tickets()))

        m.delete_ticket(3)

        self.assertNotEqual(len(test_list), len(m.all_tickets()))

    def test_filter_destination(self):
        ticket = m.create_ticket("2023-02-11", "Philadelphia", "Tom")
        ticket2 = m.create_ticket("2023-02-12", "Philadelphia", "Drew", 2)
        ticket3 = m.create_ticket("2023-02-14", "Boston", "Bryan", 1)
        ticket4 = m.create_ticket("2023-02-12", "Chicago", "Anthony")
        ticket5 = m.create_ticket("2023-02-11", "Dallas", "Eddie", 3)

        tickets = m.all_tickets()

        filtered_tickets = m.filter_by_destination("Philadelphia")

        self.assertNotEqual(tickets, filtered_tickets)
        self.assertEqual(len(filtered_tickets), 2)

    def test_filter_firstclass(self):
        ticket = m.create_ticket("2023-02-11", "Philadelphia", "Tom")
        ticket2 = m.create_ticket("2023-02-12", "Philadelphia", "Drew", 2)
        ticket3 = m.create_ticket("2023-02-14", "Boston", "Bryan", 1)
        ticket4 = m.create_ticket("2023-02-12", "Chicago", "Anthony")
        ticket5 = m.create_ticket("2023-02-11", "Dallas", "Eddie", 3)

        tickets = m.all_tickets()

        ticket3 = m.upgrade_firstclass(3)
        ticket2 = m.upgrade_firstclass(2)
        ticket4 = m.upgrade_firstclass(4)

        filtered_tickets = m.filter_by_firstclass()

        self.assertNotEqual(tickets, filtered_tickets)
        self.assertEqual(len(filtered_tickets), 3)

    def test_update_bags(self):
        ticket = m.create_ticket("2023-02-11", "Philadelphia", "Tom")
        ticket2 = m.create_ticket("2023-02-12", "Philadelphia", "Drew", 2)
        ticket3 = m.create_ticket("2023-02-14", "Boston", "Bryan", 1)
        ticket4 = m.create_ticket("2023-02-12", "Chicago", "Anthony")
        ticket5 = m.create_ticket("2023-02-11", "Dallas", "Eddie", 3)

        self.assertEqual(ticket4.bags, 0)

        ticket4 = m.update_bags(4, 2)

        self.assertEqual(ticket4.bags, 2)
