def slop(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)


#derivative
def derivative(a1, xi_list, yi_list):
    len_data = len(xi_list)
    error = 0
    for i in range(0, len_data):
        error += xi_list[i] * (a1*xi_list[i] - yi_list[i])

    deriv = 2 * error / len_data

    return deri

# gradient_descent
def gradient_descent(xi_list, yi_list, max_iterations, alpha, a1_initial):
    a1_list = [a1_initial]

    for i in range(0, max_iterations):
        a1 = a1_list[i]
        deriv = derivative(a1, xi_list, yi_list)
        a1_new = a1 - alpha * deriv
        a1_list.append(a1_new)

    return (a1_list)
