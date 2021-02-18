
class Solution : 

    def cal_min_rewards(self, arr : list) -> int : 
        res = [1] * len(arr)
        #   res = [1 for _ in range(len(arr))]

        for i in range(1, len(arr)) : 
            if arr[i] > arr[i-1] : 
                res[i] = res[i-1] + 1

        for i in range(len(arr) - 2, -1, -1) : 
            if arr[i] > arr[i+1] : 
                res[i] = max(res[i], arr[i+1] + 1)

        return sum(res)


def main() : 
    t = int(input())
    for _ in range(t) : 
        n = int(input())
        arr = list(map(int, input().split()))
        solution = Solution()
        
        print(solution.cal_min_rewards(arr))


if __name__ == '__main__' : 
    main()