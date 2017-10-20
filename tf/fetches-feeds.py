import tensorflow as tf

input1 = tf.constant([3.0])
input2 = tf.constant([2.0])
input3 = tf.constant([5.0])
intermed = tf.add(input2, input3)
mul = tf.multiply(input1, intermed)

input4 = tf.placeholder(tf.float32)
input5 = tf.placeholder(tf.float32)
output = tf.multiply(input4, input5)

with tf.Session() as sess:
  # fetches in an array
  print(sess.run([mul, intermed]))
  # feeds in a map
  print(sess.run(output, feed_dict={input4:[7.], input5:[2.]}))