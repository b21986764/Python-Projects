import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("./breast-cancer-wisconsin.csv")

dataset_copy=dataset.copy()
dataset_copy = dataset_copy.apply(pd.to_numeric, errors='coerce')
dataset_copy.fillna(1,inplace=True)


train_set = dataset_copy.sample(frac=0.8, random_state=0)
test_set = dataset_copy.sample(frac=0.2, random_state=0)
train_labels = train_set[["Class"]]
test_labels = test_set[["Class"]]



dataset.fillna(1,inplace=True)

x=dataset[["Bare_Nuclei"]].mean(skipna=True)
train_set.drop(["Code_number"],axis=1,inplace=True)
b=list(train_set.corr().values)


plt.matshow(train_set.corr())
plt.xticks(range(len(train_set.columns)), train_set.columns,rotation=90)
plt.yticks(range(len(train_set.columns)), train_set.columns)
for y in range(train_set.corr().shape[0]):
      for x in range(train_set.corr().shape[1]):
        plt.text(x, y, '%.2f' % b[x][y],horizontalalignment='center',verticalalignment='center',size=7)
plt.colorbar()
plt.show()
train_set = train_set.drop(columns=["Class"])
test_set = test_set.drop(columns=["Class"])
test_set.drop(["Code_number"],axis=1,inplace=True)




def sigmoid(x):
    return 1 / (1 + np.exp(-0.005*x))

def sigmoid_derivative(x):
    return 0.005 * x * (1 - x )




def run_on_test_set(test_inputs, test_labels, weights):
    tp = 0
    outputs = np.dot(test_set,weights)
    outputs = sigmoid(outputs)
        
    loss = np.subtract(test_labels,outputs)
   

    tuning=np.multiply(loss,sigmoid_derivative(outputs))
        
    k=np.transpose(test_set)
    weights = weights+np.dot(k,tuning)
    
    for i in list(outputs):
        if i[0]<0.5:
            i[0]=0
        if i[0]>=0.5:
            i[0]=1

    for predicted_val, label in zip(list(test_labels.values),list(outputs)):

        if predicted_val == label:
            tp += 1
    l=len(list(test_labels.values))
    accuracy = float(tp)/l
    return accuracy

def main():
    global train_set
    global test_set
    global train_labels
    global test_labels
    
    iteration_count = 2500
    np.random.seed(1)
    weights = 2 * np.random.random((9, 1)) - 1
    accuracy_array = []
    loss_array = []
    
    for iteration in range(iteration_count):
         
        outputs = sigmoid(np.dot(train_set,weights))
        
        loss = np.subtract(train_labels,outputs)
        loss_array.append([float(loss.mean())])
        
        tuning=np.multiply(loss,sigmoid_derivative(outputs))
        
        weights = weights+np.dot(np.transpose(train_set),tuning)
        
        
        accuracy_array.append([run_on_test_set(test_set,test_labels,weights)])
    print loss.mean()
    
    y = np.linspace(0, 2500, 2500)
   
    plt.plot(y,loss_array,"b",label="loss_array")
    plt.legend()
    plt.show()
    
    
    a = np.linspace(0, 2500, 2500)
    plt.plot(a,accuracy_array,"r",label="accuracy_array")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()