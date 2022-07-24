import unittest

from Robot import Robot


class RobotTest(unittest.TestCase):
    # Testing Say robot name - Power On
    def test_say_robot_name_on(self):
        self.assertEqual(
            Robot("Jeff", True, 101).say_robot_name(),
            "Hi, Nice to meet you\nMy name is Jeff"
        )

    # Testing Say Robot name - Power Off
    def test_say_robot_name_off(self):
        self.assertEqual(
            Robot("Jeff", False, 101).say_robot_name(),
            "..."
        )

    # Testing Charge Method
    def test_charge_when_battery_full(self):
        self.assertEqual(
            Robot("Jeff", False, 101).charge(),
            "I'm fully charged"
        )

    def test_charge_when_battery_not_full(self):
        self.assertEqual(
            Robot("Jeff", False, 50).charge(),
            "Gimme a minute to charge...\n DONE"
        )

    # Testing Battery Status Method - Power ON
    def test_battery_full_status_power_on(self):
        self.assertEqual(
            Robot("Jeff", True, 101).battery_status(),
            "Battery: 100%\n"
            "I'm full!"
        )

    def test_battery_low_status_power_on(self):
        self.assertLessEqual(
            Robot("Jeff", True, 25).battery_status(),
            "Battery: 25%\n"
            "I think i might need a little charge"
        )

    def test_battery_average_status_power_on(self):
        self.assertLessEqual(
            Robot("Jeff", True, 99).battery_status(),
            "Battery: 99%\n"
        )

    # Testing Battery Status Method - Power OFF
    def test_battery_full_status_power_off(self):
        self.assertEqual(
            Robot("Jeff", False, 100).battery_status(),
            "..."
        )

    def test_battery_low_status_power_off(self):
        self.assertLessEqual(
            Robot("Jeff", False, 25).battery_status(),
            "..."
        )

    def test_battery_average_status_power_off(self):
        self.assertLessEqual(
            Robot("Jeff", False, 99).battery_status(),
            "..."
        )

    # Testing learn phrase - Power On
    def test_learn_phrase_add_phrase(self):
        self.assertEqual(
            Robot("Jeff", True, 100).learn_phrase("PhraseOne"),
            'Phrase Added'
        )

    def test_learn_phrase_add_same_phrase(self):
        self.assertEqual(
            Robot("Jeff", True, 100, phrases=["PhraseOne"]).learn_phrase("PhraseOne"),
            'Phrase Added'
        )

    def test_learn_phrase_limit(self):
        self.assertEqual(
            Robot("Jeff", True, 100, phrases=[
                "PhraseOne",
                "PhraseTwo",
                "PhraseThree",
                "PhraseFour",
                "PhraseFive",
                "PhraseSix"]).learn_phrase("PhraseSeven"),
            'Memory full'
        )

    # Testing learn phrase - Power Off
    def test_learn_phrase_add_phrase_power_off(self):
        self.assertEqual(
            Robot("Jeff", False, 100).learn_phrase("PhraseOne"),
            '...'
        )

    def test_learn_phrase_add_same_phrase_power_off(self):
        self.assertEqual(
            Robot("Jeff", False, 100, phrases=["PhraseOne"]).learn_phrase("PhraseOne"),
            '...'
        )

    def test_learn_phrase_limit_power_off(self):
        self.assertEqual(
            Robot("Jeff", False, 100, phrases=[
                "PhraseOne",
                "PhraseTwo",
                "PhraseThree",
                "PhraseFour",
                "PhraseFive",
                "PhraseSix"]).learn_phrase("PhraseSeven"),
            '...'
        )


if __name__ == '__main__':
    unittest.main()
