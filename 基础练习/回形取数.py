# m行n列
#这玩意过蓝桥的测试会超时，我还没想到节省性能的方法，下次再说
#可参考这个文章https://blog.csdn.net/weixin_45829462/article/details/103882792
def flagquan(msize, nsize, mstart, nstart, jzz):
    end = 0
    for i in range(mstart, mstart + msize):
        print(jzz[i][nstart], end=" ")
        end += 1
    if (nstart + 1 >= nstart + nsize):
        return end
    for j in range(nstart + 1, nstart + nsize):
        print(jzz[mstart + msize - 1][j], end=" ")
        end += 1
    if (mstart + msize - 2 < 1):
        return end
    if (mstart >= mstart + msize - 2):
        return end
    for k in range(mstart + msize - 2, mstart, -1):
        print(jzz[k][nstart + nsize - 1], end=" ")
        end += 1
    if (nstart + nsize - 1 < 1):
        return end
    for l in range(nstart + nsize - 1, nstart, -1):
        print(jzz[mstart][l], end=" ")
        end += 1
    return end


m, n = map(int, input().split())
sums = m * n
ju = 0
jz = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    jz[i] = [int(j) for j in input().split()]
mm = 0
nn = 0
while (ju < sums):
    ju = flagquan(m, n, mm, nn, jz)
    mm += 1
    nn += 1
    m -= 2
    n -= 2
