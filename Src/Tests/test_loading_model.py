# Test Scipt to load tf_lite model.

import tflite_runtime.interpreter as tflite
import numpy as np
import time
import argparse

def main():

    # Model file
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model', help="Model file (.tflite)", dest='model_file', required=True)
    args = parser.parse_args()
    print("Loading {}.".format(args.model_file))

    # Loading model
    interpreter = tflite.Interpreter(model_path=args.model_file)
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    print("Model inputs: {} | outs: {}.".format(input_details[0]['shape'], output_details[0]['shape']))

    # Running raw inferences:
    # Test the model on random input data.
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)

    start = time.time()
    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    print("Ouput from random data: {} in {} ms.".format(output_data, ((time.time()-start)*1000)))

if __name__ == "__main__":
    main()
