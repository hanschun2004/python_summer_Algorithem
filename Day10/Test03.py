# 병합 정렬 -> Dynamic Programing 형식과 비슷 O(nlogn)
def mergeSort(ls):
    if len(ls) > 1:
        mid = len(ls) //2
        left = ls[:mid]
        right = ls[mid:]
        # print(left , right , sep = " ")

        mergeSort(left) , mergeSort(right)

        i = 0 # left인덱스
        j = 0 # right인덱스
        k = 0 # ls인덱스
        while i < len(left) and j < len(right):
            # print(left , right, sep= " ")
            if left[i] < right[j]:
                ls[k] = left[i]
                i += 1
            else:
                ls[k] = right[j]
                j += 1
            k += 1
        # 오른쪽 왼쪽 데이터가 비교하고 난 후에 한쪽에만 데이터가 남아있을때
        # 전부 ls에 넣어주는 역활
        while i < len(left):
            ls[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            ls[k] = right[j]
            j += 1
            k += 1

        return ls
print(mergeSort([6,2,4,1,3,7,5,8]))
