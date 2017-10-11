import tensorflow as tf

# create a variable
state = tf.Variable(0, name="counter")

# computation graph: operation nodes
one = tf.constant(1)
new_value = tf.add(state, one)        # new_value <- state + 1
update = tf.assign(state, new_value)  # state <- new_value

# initializer operation to initialize global variables
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init_op)       # run initializer operation
  print(sess.run(state))
  for _ in range(3):
    sess.run(update)      # run 'update' operation chain
    print(sess.run(state))
