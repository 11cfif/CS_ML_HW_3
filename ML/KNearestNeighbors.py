import numpy as np


def write_result(id, label):
    f = open('result.csv', 'w')  # opens the workfile file
    f.write('id,label\n')
    for i in range(len(label)):
        f.write(str(int(id[i])))
        f.write(',')
        f.write(str(label[i]))
        if i + 1 != len(label):
            f.write('\n')
    f.close()


def __main__():
    learn_path = "learn.csv"
    learn_data = np.loadtxt(learn_path, delimiter=',')
    test_path = "test.csv"
    test_data = np.loadtxt(test_path, delimiter=',')
    test_id = test_data[:, 0]
    test_x = test_data[:, 1:]
    learn_x = learn_data[:, 1:-1]
    learn_y = learn_data[:, -1]


__main__()