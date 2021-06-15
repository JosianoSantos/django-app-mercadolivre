import unittest

from api.mercado_libre.items import get_most_expensives_by_category, get_best_sellers_by_item_category


class BasicTests(unittest.TestCase):

    def test_get_most_expensives_by_category(self):
        print('Testing get_most_expensives_by_category')
        response = get_most_expensives_by_category('MLA352679', test=True)
        self.assertEqual(response.status_code, 200)

    def test_get_best_sellers_by_item_category(self):
        print('Testing get_best_sellers_by_item_category')
        response = get_best_sellers_by_item_category('MLA352679', test=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
