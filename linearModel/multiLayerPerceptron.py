import torch
import torch.nn as nn
import matplotlib.pyplot as plt

def calcPerceptron(device, x, y):
    model = nn.Sequential(
        nn.Linear(len(x), 32, bias=True),
        nn.ReLU(),
        nn.Linear(32, 32, bias=True),
        nn.ReLU(),
        nn.Linear(32, len(x), bias=True)
    ).to(device)

    learningRate = 1e-12

    criterion = nn.MSELoss().to(device)
    optimizer = torch.optim.SGD(model.parameters(), lr=learningRate)

    costList = []
    iteration = 10000
    for epoch in range(iteration + 1):
        optimizer.zero_grad()
        hypothesis = model(x)
        cost = criterion(hypothesis, y)
        cost.backward()
        optimizer.step()
        costList.append(cost.detach().cpu())
        #if epoch % 1000 == 0:
        #    print(f"{epoch} // {cost.item()}, {hypothesis}, {type(hypothesis)}")

    print(f"비용 함수 오차 그래프 출력중...")
    plt.figure(figsize=(20, 10))
    plt.plot([n for n in range (iteration + 1)], costList, 'r', label='Cost Function')

    plt.title(f"비용 함수 오차 시각화")
    plt.xlabel("반복 횟수")
    plt.ylabel("오차 값")
    plt.xlim(0, iteration)
    plt.legend(loc='upper right')

    return model(x)