# -*- coding: utf-8 -*-
# RNN 으로 시계열 데이터 예측 https://excelsior-cjh.tistory.com/184
#%% 가상의 시계열 데이터 생성
import matplotlib.pyplot as plt 
import numpy as np 
import tensorflow as tf 
t_min, t_max = 0, 30 
resolution = 0.1 
def time_series(t): 
    return t * np.sin(t) / 3 + 2 * np.sin(t*5) 

# mini-batch function 
def next_batch(batch_size, n_steps): 
    t0 = np.random.rand(batch_size, 1) * (t_max - t_min - n_steps * resolution) 
    Ts = t0 + np.arange(0., n_steps + 1) * resolution 
    ys = time_series(Ts) 
    return ys[:, :-1].reshape(-1, n_steps, 1), ys[:, 1:].reshape(-1, n_steps, 1) 
t = np.linspace(t_min, t_max, int((t_max - t_min) / resolution)) 
n_steps = 20 
t_instance = np.linspace(12.2, 12.2 + resolution * (n_steps + 1), n_steps + 1)
 
plt.figure(figsize=(11,4)) 
plt.subplot(121) 
plt.title("time series (generated)", fontsize=14) 
plt.plot(t, time_series(t), label=r"$t . \sin(t) / 3 + 2 . \sin(5t)$") 
plt.plot(t_instance[:-1], time_series(t_instance[:-1]), "b-", linewidth=3, label="training sample")
plt.legend(loc="lower left", fontsize=14) 
plt.axis([0, 30, -17, 13]) 
plt.xlabel("Time") 
plt.ylabel("Value", rotation=0) 
plt.subplot(122) 
plt.title("training sample", fontsize=14) 
plt.plot(t_instance[:-1], time_series(t_instance[:-1]), "bo", markersize=12, label="sample") 
plt.plot(t_instance[1:], time_series(t_instance[1:]), "w*", markeredgewidth=0.5, markeredgecolor="b", markersize=14, label="target") 
plt.legend(loc="upper left") 
plt.xlabel("Time") 
plt.show()
#%%
################
# Layer Params #
################
n_steps = 20
n_neurons = 100
n_inputs = 1
n_outputs = 1

X = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None, n_steps, n_outputs])

# RNN Model
cell = tf.nn.rnn_cell.BasicRNNCell(num_units=n_neurons, activation=tf.nn.relu)
rnn_outputs, states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)

# 하나의 출력을 위한 작업
stacked_rnn_outputs = tf.reshape(tensor=rnn_outputs, shape=[-1, n_neurons])
stacked_outputs = tf.layers.dense(stacked_rnn_outputs, n_outputs)
predictions = tf.reshape(stacked_outputs, [-1, n_steps, n_outputs])

################
# Train Params #
################
learning_rate = 0.001
n_iterations = 600
batch_size = 50

# loss
mse = tf.losses.mean_squared_error(labels=y, predictions=predictions)
# optimizer
train_op = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(mse)

# Train
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for iteration in range(n_iterations):
        batch_x, batch_y = next_batch(batch_size, n_steps)
        sess.run(train_op, feed_dict={X: batch_x, y: batch_y})
        if iteration % 100 == 0:
            loss = mse.eval(feed_dict={X: batch_x, y: batch_y})
            print('step: {:03d}, MSE: {:.4f}'.format(iteration, loss))
    # 새로운 데이터 예측하기
    X_new = time_series(np.array(t_instance[:-1].reshape(-1, n_steps, n_inputs)))
    y_pred = sess.run(predictions, feed_dict={X: X_new})
    
print('y_pred:{}\n{}'.format(y_pred.shape, y_pred))
#%%
plt.title("Testing the Model", fontsize=14)
plt.plot(t_instance[:-1], time_series(t_instance[:-1]), "bo", markersize=10, label="instance")
plt.plot(t_instance[1:], time_series(t_instance[1:]), "w*", markersize=10, label="target", color='yellow')
plt.plot(t_instance[1:], y_pred[0,:,0], "r.", markersize=10, label="prediction")
plt.legend(loc="upper left")
plt.xlabel("Time")

plt.show()