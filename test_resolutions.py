import unittest

import resolutions


class TestResolution(unittest.TestCase):
    """docstring for TestResolution"""
    
    def test_input_read(self):
        dummy_data = [
            '2',
            '300 50 230',
            '3',
            '42 24 994',
            '342 23 23',
            '342 289 920',
            '100 200 305',
            '1',
            '234 342 234',
        ]

        data = list(resolutions.parse_file(dummy_data))

        expected = [
            {
                'target': (300, 50, 230),
                'foods' : [
                    (42, 24, 994),
                    (342, 23, 23),
                    (342, 289, 920),
                ],
            }, 

            {
                'target': (100, 200, 305),
                'foods': [
                    (234, 342, 234),
                ],
            },
        ]

        self.assertEqual(data, expected)

    def test_format_case(self):
        dummy_target = '300 50 230'
        dummy_foods = [
            '42 24 994',
            '342 23 23',
            '342 289 920',
        ]

        data = resolutions.format_testcase(dummy_target, dummy_foods)

        expected = {
            'target': (300, 50, 230),
            'foods' : [
                (42, 24, 994),
                (342, 23, 23),
                (342, 289, 920),
            ],
        }

        self.assertEqual(data, expected)

    def test_format_macronutrients(self):
        dummy_data = '300 50 230'

        data = resolutions.format_macronutrients(dummy_data)

        expected = (300, 50, 230)

        self.assertEqual(data, expected)

    def test_evaluate_testcase_true(self):
        dummy_testcase = {
            'target': (100, 100, 100),
            'foods': [
                (100, 100, 100),
            ],
        }

        self.assertEqual('yes', resolutions.evaluate_testcase(dummy_testcase))

    def test_evaluate_testcase_false(self):
        dummy_testcase = {
            'target': (100, 100, 100),
            'foods': [
                (10, 10, 40),
                (10, 30, 10),
                (10, 60, 50),
            ],
        }

        self.assertEqual('no', resolutions.evaluate_testcase(dummy_testcase))


if __name__ == '__main__':
    unittest.main()
