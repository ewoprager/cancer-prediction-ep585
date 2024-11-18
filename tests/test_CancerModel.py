import unittest

from cancer_prediction.cancer_model import CancerModel


class TestCancerModel(unittest.TestCase):
    def test_target_to_diagnosis(self):
        model = CancerModel()
        diagnosis: str = model.target_to_diagnosis(0)
        assert diagnosis == "Malignant"
        diagnosis = model.target_to_diagnosis(1)
        assert diagnosis == "Benign"

    def test_diagnosis_to_target(self):
        model = CancerModel()
        target: int = model.diagnosis_to_target("Benign")
        assert target == 1
        target = model.diagnosis_to_target("Malignant")
        assert target == 0


if __name__ == "__main__":
    unittest.main()
