



# Laser_Echo_Energy_Generator

在距离选通激光成像雷达中，计算激光回波能量是一个非常重要的步骤。回波能量可以看作是激光脉冲与选通门的卷积。

## 三种卷积模式

1. ‘*mode=full*’,默认值,将计算每个电的卷积,若a, v长度为n, m. 则最终输出结果的长度为$m+n+1$,在边界信号不完全重叠,即存在边界效应
2. '*mode=same*‘,返回长度为max(m, n),存在边界效应
3. '*mode=valid*'',返回长度为min(m, n). 只会显示两个信号的重叠部分,不会有边界效应



