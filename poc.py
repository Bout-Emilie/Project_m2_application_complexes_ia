import pandas as pd
import tensorflow as tf
import constantes


class Tensor:


    def __init__(self,y_name="Alerte",train_path="iris_training.csv",test_path="iris_test.csv"):


        #Construit les DataFrames de training  a partir du CSV
        train = pd.read_csv(train_path, names=constantes.CSV_COLUMN_NAMES, header=1)
        self.train_x, self.train_y = train, train.pop(y_name)

        # Construit les DataFrames de test a partir du CSV
        test = pd.read_csv(test_path, names=constantes.CSV_COLUMN_NAMES, header=1)
        self.test_x, self.test_y = test, test.pop(y_name)
        self.classifier = ""


    def train_input_fn(self,features, labels, batch_size):
        """An input function for training"""
        # Convert the inputs to a Dataset.
        dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

        # Shuffle, repeat, and batch the examples.
        dataset = dataset.shuffle(1000).repeat().batch(batch_size)

        # Return the dataset.
        return dataset


    def eval_input_fn(self,features, labels, batch_size):
        """An input function for evaluation or prediction"""
        features=dict(features)
        if labels is None:
            # No labels, use only features.
            inputs = features
        else:
            inputs = (features, labels)

        # Convert the inputs to a Dataset.
        dataset = tf.data.Dataset.from_tensor_slices(inputs)

        # Batch the examples
        assert batch_size is not None, "batch_size must not be None"
        dataset = dataset.batch(batch_size)

        # Return the dataset.
        return dataset

    def train(self,batch_size,train_steps):

        # Utilisation du model Estimator de TensorFlow pour le DNNClassifier
        # Creation de la feature
        feature_columns = []
        for key in self.train_x.keys():
            feature_columns.append(tf.feature_column.numeric_column(key=key))

        # Creation de notre DNNClassifier
        self.classifier = tf.estimator.DNNClassifier(
            feature_columns=feature_columns,
            # Determine le nombre de couche et le nombre de neurones pour chaque
            hidden_units=[10, 10],
            # Determine le nombre de sortie.
            n_classes=2)

        # Train the Model.
        self.classifier.train(
            input_fn=lambda: self.train_input_fn(self.train_x, self.train_y,
                                                batch_size),
            steps=train_steps)

        # Evaluate the model.
        print(self.train_x)
        eval_result = self.classifier.evaluate(
            input_fn=lambda: self.eval_input_fn(self.test_x, self.test_y,
                                               batch_size))

        print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

        return self.classifier


    def predict(self,predict_x,batch_size):



        predictions = self.classifier.predict(
            input_fn=lambda: self.eval_input_fn(predict_x,
                                               labels=None,
                                               batch_size=batch_size))

        for pred_dict in predictions:
            class_id = pred_dict['class_ids']
            probability = pred_dict['probabilities']

            print(class_id)
            print(constantes.ALERTE[class_id.item(0)])

        return constantes.ALERTE[class_id.item(0)]

