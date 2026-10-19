import io
import unittest
from contextlib import redirect_stdout
from cuid2.polarlabs_batch import generate_batch, main

class PolarLabsBatchTests(unittest.TestCase):
    def test_correct_batch_count_and_length(self):
        values = generate_batch(5, 12)
        self.assertEqual(len(values), 5)
        self.assertTrue(all(len(x) == 12 for x in values))

    def test_no_duplicates_in_small_batch(self):
        values = generate_batch(100, 24)
        self.assertEqual(len(set(values)), 100)

    def test_invalid_count_or_length_is_rejected(self):
        for count, length in [(0, 24), (10001, 24), (1, 1), (1, 99)]:
            with self.subTest(count=count, length=length):
                with self.assertRaises(ValueError):
                    generate_batch(count, length)

    def test_cli_prints_exact_number_of_ids(self):
        output = io.StringIO()
        with redirect_stdout(output):
            main(["--count", "3", "--length", "10"])
        lines = output.getvalue().splitlines()
        self.assertEqual(len(lines), 3)
        self.assertTrue(all(len(x) == 10 for x in lines))

if __name__ == "__main__":
    unittest.main()
