import unittest

from Robot import Robot


class RobotTest(unittest.TestCase):

    def setUp(self):
        self.robot_power_on_battery_full = Robot("Jeff", True, 101, phrases=["PhraseOne"])
        self.robot_power_on_battery_average = Robot("Jeff", True, 50, phrases=["PhraseOne"])
        self.robot_power_on_battery_lower = Robot("Jeff", True, 25, phrases=["PhraseOne"])
        self.robot_memory_full_power_on = Robot("Jeff", True, 101, phrases=[
            "PhraseOne",
            "PhraseTwo",
            "PhraseThree",
            "PhraseFour",
            "PhraseFive",
            "PhraseSix"])

        self.robot_power_off_battery_full = Robot("Jeff", False, 101, phrases=["PhraseOne"])
        self.robot_power_off_battery_average = Robot("Jeff", False, 50, phrases=["PhraseOne"])
        self.robot_power_off_battery_lower = Robot("Jeff", False, 25, phrases=["PhraseOne"])
        self.robot_memory_full_power_off = Robot("Jeff", False, 101, phrases=[
            "PhraseOne",
            "PhraseTwo",
            "PhraseThree",
            "PhraseFour",
            "PhraseFive",
            "PhraseSix"])

    # Testing Say robot name - Power On -------------------------------------------------------
    def test_say_robot_name_on(self):
        self.assertEqual(
            self.robot_power_on_battery_full.say_robot_name(),
            "Hi, Nice to meet you\nMy name is Jeff"
        )
        self.assertEqual(
            self.robot_power_on_battery_full.battery, 100
        )

    # Testing Say Robot name - Power Off --------------------------------------------------------
    def test_say_robot_name_off(self):
        self.assertEqual(
            self.robot_power_off_battery_full.say_robot_name(),
            "..."
        )
        self.assertEqual(
            self.robot_power_off_battery_full.battery, 101
        )

    # Testing Charge Method - Power ON ---------------------------------------------------------
    def test_charge_when_battery_full(self):
        self.assertEqual(
            self.robot_power_on_battery_full.charge(),
            "I'm fully charged"
        )

    def test_charge_when_battery_not_full(self):
        self.assertEqual(
            self.robot_power_on_battery_average.charge(),
            "Gimme a minute to charge...\n DONE"
        )

    # Testing Charge Method - Power OFF ---------------------------------------------------------
    def test_charge_when_battery_full_power_off(self):
        self.assertEqual(
            self.robot_power_off_battery_full.charge(),
            "..."
        )

    def test_charge_when_battery_not_full_power_off(self):
        self.assertEqual(
            self.robot_power_off_battery_average.charge(),
            "..."
        )

    # Testing Battery Status Method - Power ON ---------------------------------------------------
    def test_battery_full_status_power_on(self):
        self.assertEqual(
            self.robot_power_on_battery_full.battery_status(),
            "Battery: 100%\n"
            "I'm full!"
        )
        self.assertEqual(
            self.robot_power_on_battery_full.battery, 100
        )

    def test_battery_low_status_power_on(self):
        self.assertLessEqual(
            self.robot_power_on_battery_lower.battery_status(),
            "Battery: 24%\n"
            "I think i might need a little charge"
        )
        self.assertEqual(
            self.robot_power_on_battery_lower.battery, 24
        )

    def test_battery_average_status_power_on(self):
        self.assertLessEqual(
            self.robot_power_on_battery_average.battery_status(),
            "Battery: 49%\n"
        )
        self.assertEqual(
            self.robot_power_on_battery_average.battery, 49
        )

    # Testing Battery Status Method - Power OFF -----------------------------------------------------
    def test_battery_full_status_power_off(self):
        self.assertEqual(
            self.robot_power_off_battery_full.battery_status(),
            "..."
        )
        self.assertEqual(
            self.robot_power_off_battery_full.battery, 101
        )

    def test_battery_low_status_power_off(self):
        self.assertLessEqual(
            self.robot_power_off_battery_lower.battery_status(),
            "..."
        )
        self.assertEqual(
            self.robot_power_off_battery_lower.battery, 25
        )

    def test_battery_average_status_power_off(self):
        self.assertLessEqual(
            self.robot_power_off_battery_average.battery_status(),
            "..."
        )
        self.assertEqual(
            self.robot_power_off_battery_average.battery, 50
        )

    # Testing learn phrase - Power On ----------------------------------------------------------------
    def test_learn_phrase_add_phrase(self):
        self.assertEqual(
            self.robot_power_on_battery_full.learn_phrase("uau"),
            'Phrase Added'
        )
        self.assertEqual(
            self.robot_power_on_battery_full.battery, 96
        )

    def test_learn_phrase_add_same_phrase(self):
        self.assertEqual(
            self.robot_power_on_battery_full.learn_phrase("PhraseOne"),
            'Phrase Added'
        )
        self.assertEqual(
            self.robot_power_on_battery_full.battery, 96
        )

    def test_learn_phrase_limit(self):
        self.assertEqual(
            self.robot_memory_full_power_on.learn_phrase("PhraseSeven"),
            'Memory full'
        )
        self.assertEqual(
            self.robot_memory_full_power_on.battery, 101
        )

    # Testing learn phrase - Power Off -------------------------------------------------------------
    def test_learn_phrase_add_phrase_power_off(self):
        self.assertEqual(
            Robot("Jeff", False, 100).learn_phrase("PhraseOne"),
            '...'
        )
        self.assertEqual(
            self.robot_memory_full_power_off.battery, 101
        )

    def test_learn_phrase_add_same_phrase_power_off(self):
        self.assertEqual(
            self.robot_power_off_battery_full.learn_phrase("PhraseOne"),
            '...'
        )
        self.assertEqual(
            self.robot_power_off_battery_full.battery, 101
        )

    def test_learn_phrase_limit_power_off(self):
        self.assertEqual(
            self.robot_memory_full_power_off.learn_phrase("PhraseSeven"),
            '...')
        self.assertEqual(
            self.robot_memory_full_power_off.battery, 101
        )

    # Testing show phrases_power on -----------------------------------------------------
    def test_show_phrases_power_on(self):
        self.assertEqual(
            self.robot_memory_full_power_on.show_phrases(),
            'Done'
        )
        self.assertEqual(
            self.robot_memory_full_power_on.battery, 98
        )

    # Testing show phrases_power off -----------------------------------------------------
    def test_show_phrases_power_off(self):
        self.assertEqual(
            self.robot_memory_full_power_off.show_phrases(),
            '...'
        )
        self.assertEqual(
            self.robot_memory_full_power_off.battery, 101
        )

    # Testing show phrases_power on -----------------------------------------------------
    def test_show_a_phrase_power_on(self):
        self.assertEqual(
            self.robot_memory_full_power_on.show_a_phrase(1),
            'PhraseOne'
        )
        self.assertEqual(
            self.robot_memory_full_power_on.battery, 98
        )

    def test_show_a_phrase_power_on_invalid_phrase_num(self):
        self.assertEqual(
            self.robot_memory_full_power_on.show_a_phrase(0),
            'Phrase not found!\nbe sure you put the right phrase number...'
        )
        self.assertEqual(
            self.robot_memory_full_power_on.battery, 98
        )

    # Testing show phrases_power off -----------------------------------------------------
    def test_show_a_phrase_power_off(self):
        self.assertEqual(
            self.robot_memory_full_power_off.show_a_phrase(1),
            '...'
        )
        self.assertEqual(
            self.robot_memory_full_power_off.battery, 101
        )

    def test_show_a_phrase_power_off_invalid_phrase_num(self):
        self.assertEqual(
            self.robot_memory_full_power_off.show_a_phrase(1),
            '...'
        )
        self.assertEqual(
            self.robot_memory_full_power_off.battery, 101
        )


if __name__ == '__main__':
    unittest.main()
