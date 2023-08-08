```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class AIModel:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = keras.Sequential()
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))
        model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def train(self, train_data, train_labels, epochs=10):
        self.model.fit(train_data, train_labels, epochs=epochs)

    def evaluate(self, test_data, test_labels):
        return self.model.evaluate(test_data, test_labels)

    def predict(self, input_data):
        return self.model.predict(input_data)

class VirtualMentor:
    def __init__(self):
        self.ai_model = AIModel()

    def train_mentor(self, train_data, train_labels):
        self.ai_model.train(train_data, train_labels)

    def evaluate_mentor(self, test_data, test_labels):
        return self.ai_model.evaluate(test_data, test_labels)

    def provide_guidance(self, input_data):
        prediction = self.ai_model.predict(input_data)
        return prediction
```