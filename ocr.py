import csv
from math import exp
from math import pow

def load_csv(filename):
    lines = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            lines.append(line)
    return lines

def load_test_data():
    return load_csv("test.csv")

def load_validation_data():
    return load_csv("validation.csv")

#Possibly use different data for training and validation
def load_adult_train_data():
    return load_test_data()

def load_adult_valid_data():
    return load_validation_data()

def extract_features(raw, isActual):
    data = []
    for r in raw:
        point = {}
        if (isActual):
            point['label'] = int(r['valy'])
        else:
            point['label'] = int(r['testy'])

        features = []
        for i in range(0, len(raw[0]) - 1):
            features.append(int(r['pixel' + str(i)]))

        point['features'] = features
        data.append(point)
    return data

def dot(x, y):
    s = 0.0
    for i in range(0, len(x)):
        s = s + x[i]*y[i]
    return s

def sign(value):
    if (value <= 0):
        return -1
    else:
        return 1

def train(data, func, z=1):
    mistakes = []
    num_mistakes = 0
    T = 1
    for i in range(0, len(data)):
        val = 0.0
        for j in range(0, len(mistakes)):
            val += mistakes[j]['label'] * func(mistakes[j]['features'], data[i]['features'], z)

        if (sign(val) != data[i]['label']):
            mistakes.append(data[i])
            num_mistakes += 1

        T += 1

        if (T % 100 == 0):
            print float(num_mistakes)/T
    print "\n"

def kernel(x, y, z=1):
    return kerneld(x, y, 1)

def kerneld(x, y, d):
    return pow(dot(x, y) + 1, d)

def exponential_kernel(x, y, z=1):
    result_vector = []
    for i in range(0, len(x)):
        result_vector.append(x[i]-y[i])

    result = 0.0
    for j in range(0, len(result_vector)):
        result += pow(result_vector[j], 2)

    result = pow(result, .5)

    return exp(-1.0 * (result)/200)

def main():
    # load test data
    data_test = load_adult_train_data()
    test_data = extract_features(data_test, False)

    # load validation data
    data = load_validation_data()
    validation_data = extract_features(data, True)

    # 3.4.1
    train(validation_data, kernel)

    # 3.4.2
    set = [1, 3, 5, 7, 10, 15, 20]
    for d in set:
        train(validation_data, kerneld, d)

    # 3.4.3
    train(test_data, exponential_kernel)

if __name__ == "__main__":
    main()