
def read_data():
    result = []

    while True:
        user_text = input("Please enter a number: ")

        if user_text == "x":
            break
        else:
            result.append(int(user_text))

    return result


def calc_min_max_mean(lst):
    res_min = min(lst)
    res_max = max(lst)
    num_elems = len(lst)
    total_sum = sum(lst)
    res_mean = total_sum / num_elems

    return (res_min, res_max, res_mean)


values = read_data()
results = calc_min_max_mean(values)

print(f"min: {results[0]}, max: {results[1]}, mean: {results[2]}")
