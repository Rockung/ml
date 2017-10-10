import tensorflow as tf

# step 1. define a DAG
# ====================

# 1x2 matrix
mat1 = tf.constant([[3., 3.]])

# 2x1 matrix
mat2 = tf.constant([[2.], [2.]])

# matrix operation
product = tf.matmul(mat1, mat2)

# step 2. create a session
sess = tf.Session()

# step 3. computing

result = sess.run([product])
print(result)
