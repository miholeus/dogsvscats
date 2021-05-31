# coding: utf-8
import tensorflow as tf

__model = None


def load_artifacts():
    print("loading saved artifacts...start")

    global __model

    if __model is None:
        __model = tf.keras.models.load_model('./artifacts/dogs_vs_cats.h5')
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_artifacts()

