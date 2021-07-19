class interview_questions:
    # def __init__(self, *args,  **kwargs):
    #     # for key, value in kwargs.items():
    #     #     print ("%s == %s" %(key, value))
    #     self.driver = []
    #     for arg in args:
    #         self.driver.append(arg)

    def palin(self, *args):
        output = []
        for val in args:
            if str(val)[0] == '-':
                output.append(False)
            else:
                output.append(str(val) == str(val)[::-1])
        return output

    def elementRemoval(self, arr, val):

        count = 0
        for i in range(len(arr)):
            if val != arr[i]:
                arr[count] = arr[i]
                count+=1
                # print(arr)
        return count,arr 


      
        #     if arr[i] != val :
        #         arr[count] = arr[i]
        #         count +=1
        # print(arr)
        # return count


        # print('kwargs[\'arr\']= ', kwargs['arr'])
        # for key,value in kwargs.items():
        #     print('key = ', key)
        #     print('value = ', value)


# def trial(arr,val):
#     print('arr= ', arr)
#     print('val= ', val)



iq = interview_questions()
# print(iq.palin(-123, 123,'racecar'))
a = [2,3,3,2]
res,updatedArray = iq.elementRemoval(arr = a, val = 3)
print("[")
for i in range(res):
    print(a[i], end='')
print("]")
print(updatedArray)
# trial(val= 3, arr=[2,3,3,2])




# def remover(arr,x):
#     l = len(arr)
#     ct = 0
#     itr = l - 1
#     for i in range(l-1,0,-1):
#         while i > 0 and arr[itr] != x:
#             temp = arr[]



# count = 0
#         for i in range(len(nums)):
#             if nums[i] != val :
#                 nums[count] = nums[i]
#                 count +=1
#         return count