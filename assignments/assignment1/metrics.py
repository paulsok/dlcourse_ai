import numpy as np


def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification
    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels
    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score

    num_samples = prediction.shape[0]

    TP = FP = TN = FN = 0

    for i in range(num_samples):
        if ground_truth[i]:
            if prediction[i]:
                TP += 1
            else:
                FN += 1
        else:
            if prediction[i]:
                FP += 1
            else:
                TN += 1

    precision = recall = f1 = accuracy = 0

    if (TP + FP) != 0:
        precision = TP / (TP + FP)

    if (TP + FN) != 0:
        recall = TP / (TP + FN)

    if (TP + FN + TN + FP) != 0:
        accuracy = (TP + TN) / (TP + FN + TN + FP)

    if (precision + recall) != 0:
        f1 = 2 * precision * recall / (precision + recall)

    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification
    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels
    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy

    num_samples = prediction.shape[0]

    if num_samples == 0:
        return 0

    TP_TN = 0
    for i in range(num_samples):
        if (ground_truth[i] == prediction[i]):
            TP_TN += 1

    accuracy = TP_TN / num_samples

    return accuracy
