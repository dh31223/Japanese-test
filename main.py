
import pandas as pd
import time


if __name__ == '__main__':
    df = pd.read_csv('text.csv')

    mod = input('1.开始\n0.结束')

    while mod == '1':
        label1 = df[df['label'] == 1]
        label0 = df[df['label'] == 0]

        n1 = len(label1)
        n0_target = int(n1 * 0.4 / 0.6)

        sampled = pd.concat([
            label1,
            label0.sample(n=n0_target, random_state=int(time.time()))
        ])

        result = sampled.sample(frac=1, random_state=int(time.time())).reset_index(drop=True)

        print(result.iloc[:10, 0])

        
        mod = input('1.开始\n0.结束')



    exit()


    print('结束了！')
