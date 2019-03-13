import tensorflow as tf
import numpy as np
sess = tf.Session()
filename_queue = tf.train.string_input_producer(
    tf.train.match_filenames_once("./iris.csv"),
    shuffle=True
)

reader = tf.TextLineReader(skip_header_lines=1)
key, value = reader.read(filename_queue)
record_defaults = [[""],[0.], [0.], [0.], [0.], [""]]
ind, col1, col2, col3, col4, col5 = tf.decode_csv(value, record_defaults=record_defaults)
features = tf.stack([col1,col1,col3,col4])

init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
sess.run(init_op)
#tf.global_variables_initializer().run(session=sess)
#sess.run(tf.global_variables_initializer(),tf.local_variables_initializer())
# tf.global_variables_initializer()
#with tf.Session() as sess:
    # 启动线程
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(coord=coord, sess=sess)

for iteration in range(0, 5):
    example = sess.run([features])
    print(example)
    coord.request_stop()
    coord.join(threads)
    #sess.run(features)

