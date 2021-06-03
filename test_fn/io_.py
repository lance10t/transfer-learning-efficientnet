import numpy as np
import os
import csv

def readFiles(fileFolder='test_images'):
    return np.sort(os.listdir(fileFolder))

    """ 
def output_test_csv(files, scores, scoreFile = 'score.csv', nameFile = 'name.csv'):
    # scores should represent the likelihood of an image belonging to a specific class
    # scores should have dimension: [len(files), scores]
    
    writer = csv.writer(open(scoreFile, 'w'))
    for s in scores:
        writer.writerow(s)

    writer = csv.writer(open(nameFile, 'w'))  
    for f in files:
        name_ = f.split('.')[-2]
        writer.writerow(name_) """


def score(scores, gt, k=5):
    class_ = np.argsort(-scores, axis=1)
    top1_acc = np.mean(gt==class_[:,0])   

    true_mat = np.zeros([class_.shape[0], k], dtype=bool)
    for i in range(k):
        true_mat[:,i] = (gt == class_[:,i])
    
    true_mat = np.max(true_mat, axis=1)
    topk_acc = np.mean(true_mat)

    return top1_acc, topk_acc


if __name__ == "__main__":
    files = readFiles()
    ###### replace with your own function #######
    # scores = output of predict function (len(files), num_classes=72)

    np.random.seed(42)
    scores = np.random.random([len(files), 72])
    ############################################
    # gt = ground truth (len(files),)
    gt = np.array([69, 68])
    top1, top5 = score(scores, gt, 5)
    print(top1)
    print(top5)

    #print(scores)

