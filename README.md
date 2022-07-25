# SM2
【项目名称】report on the application of this deduce technique in Ethereum with ECDSA

【项目简介】通过编写代码实现ECDSA，对ECDSA在SM2中的应用有进一步理解。

【代码说明】

SM2椭圆曲线公钥密码算法包括SM2-1椭圆曲线数字签名算法、SM2-2椭圆曲线密钥交换协议、SM2-3椭圆曲线公钥加密算法，分别用于实现数字签名密钥协商和数据加密等功能。

椭圆曲线数字签名算法，首先要进行公私钥的生成。

随机取一个在(1，n−1)区间上的整数作为私钥：

![image](https://user-images.githubusercontent.com/105579212/180797384-cb791d24-7a0f-4c99-a025-9f862e64e51d.png)

公钥等于私钥乘以椭圆曲线上的基点，得到公私钥对象：

![image](https://user-images.githubusercontent.com/105579212/180798229-43e1e7be-1b88-4b31-9b0a-7ee6fd4be216.png)

进行数字签名，首先生成一个临时密钥k，计算P = k∗G，其中P是椭圆曲线上的一个点，取P点的x坐标，r ≡ x (mod n)，使用sha1函数计算message的哈希值，使用H(m)表示，s ≡ k ^(-1)∗(H(m) + 私钥∗r)，而(r,s)即为数字签名：

![image](https://user-images.githubusercontent.com/105579212/180798310-43095e30-8208-4eb7-aceb-98a2a5ff5071.png)

【运行截图】

![image](https://user-images.githubusercontent.com/105579212/180797329-f42dfd9c-fad5-4f2f-857f-c14f6de3bbc4.png)
