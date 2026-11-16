class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        def recurse(nums):

            if len(nums)==1:
                return nums

            mp = len(nums) // 2
            left = nums[:mp]
            right = nums[mp:]

            l = recurse(left)
            r = recurse(right)

            return sort(l, r)

        def sort(left, right):
            print(left)
            print(right)

            output = []
            i=0
            j=0

            while i<len(left) or j<len(right):
                if i<len(left) and j<len(right):
                    if left[i] <= right[j]:
                        print(left[i])
                        print(right[j])
                        output.append(left[i])
                        i+=1
                    else:
                        output.append(right[j])
                        j+=1

                elif i<len(left):
                    output.append(left[i])
                    i+=1
                else:
                    output.append(right[j])
                    j+=1
            print(output)
            return output

        
        return recurse(nums)