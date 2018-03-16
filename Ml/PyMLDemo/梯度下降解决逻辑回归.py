#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 根据俩门成绩预测出该人会不会被录取

data_path = "F:\\GoBig.avi\\tyd_ml_material\\ExamplesToCode\\GradeintDescent_LogisticRegression\\GradientDescent\\data\\LogiReg_data.txt"
pdData = pd.read_csv(data_path, header=None, names=["Exam 1", "Exam 2", "Admitted"])
# print(pdData.head())
# print(pdData.shape)

positive = pdData[pdData["Admitted"] == 1]
negative = pdData[pdData["Admitted"] == 0]

fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(positive["Exam 1"], positive['Exam 2'], s=30, marker='x', c='r', label='Admitted')
ax.scatter(negative["Exam 1"], negative['Exam 2'], s=30, marker='o', c='b', label='Not Admitted')
ax.legend()
ax.set_xlabel("Exam 1 Score")
ax.set_ylabel("Exam 2 Score")


# plt.show()

# 定义Sigmoid Function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# 定义model,因为这里是横向定义的，书本里面的向量是纵向的
def model(X, theta):
    return sigmoid(np.dot(X, theta.T))


# 在第0列插入一个值都为1的Ones vector
pdData.insert(0, "Ones", 1)
orig_data = pdData.as_matrix()
# get no of columns
cols = orig_data.shape[1]
X = orig_data[:, 0:cols - 1]
y = orig_data[:, cols - 1:cols]
# initial theta
theta = np.zeros([1, 3])


# cost function
def cost(X, y, theta):
    left = np.multiply(-y, np.log(model(X, theta)))
    right = np.multiply(1 - y, np.log(1 - model(X, theta)))
    return np.sum(left - right) / len(X)


# calculate gradient
def gradient(X, y, theta):
    grad = np.zeros(theta.shape)
    error = (model(X, theta) - y).ravel()
    for j in range(len(theta.ravel())):  # for each parameter
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)
    return grad


# 3 kinds of gradient descent
STOP_ITER = 0  # 按照迭代次数
STOP_COST = 1  # 按照损失
STOP_GRAD = 2  # 按照梯度


def stopCriterion(type, value, threshold):
    # 3 kinds of criterions
    if type == STOP_ITER:
        return value > threshold
    elif type == STOP_COST:
        return abs(value[-1] - value[-2]) < threshold
    elif type == STOP_GRAD:
        return np.linalg.norm(value) < threshold  # 求二范式


def shuffleDate(data):  # 洗牌
    np.random.shuffle(data)
    cols = data.shape[1]
    X = data[:, 0:cols - 1]
    y = data[:, cols - 1:cols]
    return X, y


import time


def descent(data, theta, batchSize, stopType, threshold, alpha):
    init_time = time.time()
    i = 0  # 迭代次数
    k = 0  # batch
    X, y = shuffleDate(data)
    grad = np.zeros(theta.shape)
    costs = [cost(X, y, theta)]

    while True:
        grad = gradient(X[k:k + batchSize], y[k:k + batchSize], theta)
        k += batchSize
        if k >= len(y.ravel()):
            k = 0
            X, y = shuffleDate(data)
        theta = theta - alpha * grad
        costs.append(cost(X, y, theta))
        i += 1

        if type == STOP_ITER:
            value = i
        elif type == STOP_COST:
            value = costs
        else:
            value = grad

        if stopCriterion(type, value, threshold): break

    return theta, i - 1, costs, grad, time.time() - init_time


def runExpe(data, theta, batchSize, stopType, threshold, alpha):
    # import pdb; pdb.set_trace();
    theta, iter, costs, grad, dur = descent(data, theta, batchSize, stopType, threshold, alpha)
    name = "Original" if (data[:, 1] > 2).sum() > 1 else "Scaled"
    name += " data - learning rate: {} - ".format(alpha)
    if batchSize == len(y.ravel()):
        strDescType = "Gradient"
    elif batchSize == 1:
        strDescType = "Stochastic"
    else:
        strDescType = "Mini-batch ({})".format(batchSize)
    name += strDescType + " descent - Stop: "
    if stopType == STOP_ITER:
        strStop = "{} iterations".format(threshold)
    elif stopType == STOP_COST:
        strStop = "costs change < {}".format(threshold)
    else:
        strStop = "gradient norm < {}".format(threshold)
    name += strStop
    print("***{}\nTheta: {} - Iter: {} - Last cost: {:03.2f} - Duration: {:03.2f}s".format(
        name, theta, iter, costs[-1], dur))
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(np.arange(len(costs)), costs, 'r')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Cost')
    ax.set_title(name.upper() + ' - Error vs. Iteration')
    return theta

n=100
runExpe(orig_data, theta, n, STOP_ITER, threshold=1, alpha=0.000001)
plt.show()
