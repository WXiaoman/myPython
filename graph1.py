import tensorflow as tf
sess = tf.Session()
filename_queue = tf.train.string_input_producer(
    tf.train.match_filenames_once("./laska.jpg"))
reader = tf.WholeFileReader()
key, value = reader.read(filename_queue)
image = tf.image.decode_jpeg(value)
fileImageUpDown = tf.image.encode_jpeg(tf.image.flip_up_down(image))
fileImageLeftRight = tf.image.encode_jpeg(tf.image.flip_left_right(image))
sess.run(tf.group(tf.global_variables_initializer(), tf.local_variables_initializer()))

coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(coord=coord,sess=sess)
example = sess.run(fileImageLeftRight)
print(example)

file = open("fileupdown.jpg","wb+")
file.write(fileImageUpDown.eval(session = sess))
file.close()
file = open("fileleftright.jpg","wb+")
file.write(fileImageLeftRight.eval(session = sess))
file.close()

coord.request_stop()
coord.join(threads)
sess.close()
