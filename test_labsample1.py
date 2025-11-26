import labsample1


def test_get_longest_workout():
    workouts = labsample1.load_csv()
    longestworkout = labsample1.get_longest_workout(workouts)
    assert(75.0 == longestworkout["duration"])

   


def test_calc_total_duration():
    workouts = labsample1.load_csv()
    totalduration = labsample1.calc_total_duration(workouts)
    expectedresult = 853.0
    assert(expectedresult == totalduration)


def test_calc_average_duration():
    workouts = labsample1.load_csv()
    avergae = labsample1.calc_average_duration(workouts)
    expectedresult = 42.65
    assert(expectedresult == avergae)