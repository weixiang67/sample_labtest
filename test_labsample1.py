import labsample1


def test_get_longest_workout():
    workouts = labsample1.load_csv()
    longest = labsample1.get_longest_workout(workouts)
    result = {"date": "25.01.2022", "activity": "Cycling","duration": 75.0}
    assert(result == longest)

def test_calc_total_duration():
    workouts = labsample1.load_csv()
    total = labsample1.calc_total_duration(workouts)
    result = 853
    assert (result == total)


def test_calc_average_duration():
    workouts = labsample1.load_csv()
    average = labsample1.calc_average_duration(workouts)
    result = 42.65
    assert(result == average)
