import csv

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
            point["label"] = int(r['valy'])
        else:
            point["label"] = int(r['testy'])

        features = []
        for i in range(0, len(raw[0])-2):
            features.append(int(r['pixel' + str(i)]))

        point['features'] = features
        data.append(point)
    return data

def dot(x, y):
    s = 0
    for i in range(0, len(x)):
        s = s + x[i]*y[i]
    return s

def train(data):


def main():
    # test data
    test_data = load_adult_train_data()
    extract_features(test_data, False)

    # validation data
    #validation_data = load_validation_data()
    #extract_features(validation_data, True)

if __name__ == "__main__":
    main()