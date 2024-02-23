import unittest
from io import StringIO

import Conversion


class TestConversion(unittest.TestCase):
    def test_replacing_periods(self):
        test_mock_file = StringIO(("1\n"
                                   "00:00:01.000 --> 00:00:04.000\n"
                                   "This is the first subtitle.\n"
                                   "\n"
                                   "2\n"
                                   "00:00:05.000 --> 00:00:08.000\n"
                                   "This is the second subtitle.\n")
                                  )

        result = list(Conversion.replace_periods_with_comma_in_timestamps(test_mock_file))

        expected = [
            "1\n",
            "00:00:01,000 --> 00:00:04,000\n",
            "This is the first subtitle.\n",
            "\n",
            "2\n",
            "00:00:05,000 --> 00:00:08,000\n",
            "This is the second subtitle.\n",
        ]

        self.assertEqual(expected, result)

    def test_convert_vtt_to_srt(self):
        test_vtt_path = r"./Test_files/test_vtt.vtt"
        test_expected_srt_path = r"./Test_files/expected.srt"

        Conversion.convert_vtt_to_srt(test_vtt_path)

        with open(test_expected_srt_path, "r") as expected_srt_file, \
             open(test_vtt_path.replace('.vtt', '.srt'), "r") as result_file:
            self.assertEqual(expected_srt_file.read(), result_file.read())


if __name__ == '__main__':
    unittest.main()