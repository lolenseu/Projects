import os
import tensorflow as tf


num1 = tf.Variable(1, tf.int16)
num2 = tf.Variable(5999, tf.int16)


while True:
    print(num1 + num1)
