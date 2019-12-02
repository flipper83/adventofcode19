from typing import List


def get_masses_mock_values() -> List[int]:
    file = open('masses.txt')
    return list((int(line.strip()) for line in file))
