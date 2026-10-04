import unittest
from demographic_data_analyzer import calculate_demographic_data


class UnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = calculate_demographic_data(False)

    def test_race_count(self):
        actual = self.data["race_count"].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertEqual(actual, expected)

    def test_average_age_men(self):
        self.assertEqual(self.data["average_age_men"], 39.4)

    def test_percentage_bachelors(self):
        self.assertEqual(self.data["percentage_bachelors"], 16.4)

    def test_higher_education_rich(self):
        self.assertEqual(self.data["higher_education_rich"], 46.5)

    def test_lower_education_rich(self):
        self.assertEqual(self.data["lower_education_rich"], 17.4)

    def test_min_work_hours(self):
        self.assertEqual(self.data["min_work_hours"], 1)

    def test_min_work_hours_rich(self):
        self.assertEqual(self.data["min_work_hours_rich"], 10.0)

    def test_highest_earning_country(self):
        self.assertEqual(self.data["highest_earning_country"], "Iran")

    def test_highest_earning_country_percentage(self):
        self.assertEqual(
            self.data["highest_earning_country_percentage"], 41.9
        )

    def test_top_IN_occupation(self):
        self.assertEqual(
            self.data["top_IN_occupation"], "Prof-specialty"
        )


if __name__ == "__main__":
    unittest.main()