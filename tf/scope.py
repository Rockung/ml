import tensorflow as tf

with tf.variable_scope("foo", initializer=tf.constant_initializer(0.4)):
  v = tf.get_variable("v", [1])
  assert v.eval() == 0.4
  