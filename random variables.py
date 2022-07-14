import numpy as np
import matplotlib.pyplot as plt


def linear_congruential_generator(seed, period, total_num):
    a = 5214665
    c = 8689898

    random_num = []
    random_num.append(seed / period)

    N_i = []
    N_i.append(seed)
    for i in range(total_num):
        N_i.append(np.mod(a * N_i[i - 1] + c, period))
        random_num.append(N_i[i] / period)

    random_num = np.array(random_num, dtype=float)

    return random_num


def main(seed_x, seed_y, period, total_num):
    no_inside_circle = 0
    x = linear_congruential_generator(seed_x, period, total_num)
    y = linear_congruential_generator(seed_y, period, total_num)

    no_inside_circle_numpy = 0
    x_numpy = np.random.random([total_num])
    y_numpy = np.random.random([total_num])
    for i in range(total_num):

        if np.power(x[i], 2) + np.power(y[i], 2) < 1.:
            no_inside_circle = no_inside_circle + 1
        if np.power(x_numpy[i], 2) + np.power(y_numpy[i], 2) < 1.:
            no_inside_circle_numpy = no_inside_circle_numpy + 1
    monte_carlo_pi = 4 * (no_inside_circle / total_num)
    numpy_rand_num_pi = 4 * (no_inside_circle_numpy / total_num)

    print("Monter-Carlo value of pi using linear congruential generator : ", np.array(monte_carlo_pi, dtype=float),
          "\nMonter-Carlo value of pi using numpy random generator :", np.array(numpy_rand_num_pi, dtype=float))

    theta = np.linspace(0, np.pi / 2, 2000)
    a = np.cos(theta)
    b = np.sin(theta)
    plt.scatter(x, y, marker='.', label='pseudo-random-points', color='y', linewidths=0.05)
    plt.plot(a, b, label='circle', color='blue')
    plt.legend()
    plt.show()

    plt.scatter(x_numpy, y_numpy, marker='.', label='numpy-random-points', color='orange', linewidths=0.05)
    plt.plot(a, b, label='circle', color='red')
    plt.legend()
    plt.show()


main(0.25, 0.95, 1e100, 500)