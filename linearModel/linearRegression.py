import torch
import matplotlib.pyplot as plt

def calcRegression(x, y, codeName):
    print(f"{codeName} 선형 회귀 계산중...")
    
    learningRate = 1e-11 * 2.464
    weight = torch.zeros(1, requires_grad=True)
    bias = torch.zeros(1, requires_grad=True)
    optimizer = torch.optim.SGD([weight, bias], lr=learningRate)

    hy = []
    iteration = 50000
    iterCount = [x for x in range(iteration + 1)]
    for n in range(iteration + 1):
        hypothesis = weight * x + bias
        cost = torch.mean((hypothesis - y) ** 2)
        hy.append(cost.detach().numpy())
        optimizer.zero_grad()
        cost.backward()
        optimizer.step()
        if __name__ == '__main__' and n % 100 == 0:
            print(f"{n} // loss : {cost}, weight : {weight}, bias : {bias}")

    print(f"{codeName} 비용 함수 오차 그래프 출력중...")
    
    #if __name__ == '__main__':
    plt.figure(figsize=(20,10))
    plt.plot(iterCount, hy, 'r', label='Cost Function')

    plt.title(f"{codeName} 비용 함수 오차 시각화")
    plt.xlabel("반복 횟수")
    plt.ylabel("오차 값")
    plt.xlim(0, iteration)
    plt.legend(loc='upper right')
    #plt.show()

    ret = weight * x + bias
    return ret
