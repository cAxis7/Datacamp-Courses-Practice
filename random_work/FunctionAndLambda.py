import math
from functools import reduce

# Define the function with an arbitrary number of arguments
def sort_types(*args):
    nums, strings = [], []    
    for arg in args:
        # Check if 'arg' is a number and add it to 'nums'
        if isinstance(arg, (int, float)):
            nums.append(arg)
        # Check if 'arg' is a string and add it to 'strings'
        elif isinstance(arg, str):
            strings.append(arg)
    
    return (nums, strings)

def key_types(**kwargs):
    dict_type = dict()
    # Iterate over key value pairs
    for key, value in kwargs.items():
        # Update a list associated with a key
        if type(value) in dict_type:
            dict_type[type(value)].append(key)
        else:
            dict_type[type(value)] = [key]
            
    return dict_type

# Define the arguments passed to the function
def sort_all_types(*args, **kwargs):

    # Find all the numbers and strings in the 1st argument
    nums1, strings1 = sort_types(*args)
    
    # Find all the numbers and strings in the 2nd argument
    nums2, strings2 = sort_types(*kwargs.values())
    
    return (nums1 + nums2, strings1 + strings2)

def my_zip(*args):
    
    # Retrieve Iterable lengths and find the minimal length
    lengths = list(map(len, args))
    min_length = min(lengths)

    tuple_list = []
    for i in range(0, min_length):
        # Map the elements in args with the same index i
        mapping = map(lambda x: x[i], args)
        # Convert the mapping and append it to tuple_list
        tuple_list.append(tuple(mapping))
        
    return tuple_list

# Write an expression to get the k-th element of the series 
get_elmnt = lambda k: ((-1)**k)/(2*k+1)

def calc_pi(n):
    curr_elmnt = get_elmnt(n)
    
    # Define the base case
    if n == 0:
    	return 4
      
    # Make the recursive call
    return 4 * get_elmnt(n) + calc_pi(n - 1)

if __name__ == "__main__":

    print(sort_types(1.57, 'car', 'hat', 4, 5, 'tree', 0.89))
    res = key_types(a=1, b=2, c=(1, 2), d=3.1, e=4.2)
    print(res)
    res = sort_all_types(
	    1, 2.0, 'dog', 5.1, num1 = 0.0, num2 = 5, str1 = 'cat'
    )
    print(res)
    
    # Convert func1() to a lambda expression
    lambda1 = lambda x, y: x if x >= y else y
    print(str(lambda1(5, 4)))
    print(str(lambda1(4, 5)))

    # Convert func2() to a lambda expression
    lambda2 = lambda s: dict([(c, s.count(c)) for c in set(s)])
    print(lambda2('DataCamp'))

    # Convert func3() to a lambda expression
    lambda3 = lambda *nums: math.sqrt(sum([n**2 for n in nums]))
    print(str(lambda3(3, 4)))
    print(str(lambda3(3, 4, 5)))

    result = my_zip([1,2,3],['a','b','c','d'], 'DataCamp')
    print(result)

    # Filter all the spells in spells with more than two 'a's
    spells = ['riddikulus',
              'obliviate',
              'sectumsempra',
              'avada kedavra',
              'alohomora',
              'lumos',
              'expelliarmus',
              'expecto patronum']
    print(spells)
    fspells = filter(lambda s: s.count('a') > 2, spells)
    print(list(fspells))

    # Convert a number sequence into a single number
    nums = [5, 6, 0, 1]
    num = reduce(lambda x, y: str(x) + str(y), nums)
    print(str(nums) + ' is converted to ' + str(num))

    # Compare the approximated Pi value to the theoretical one
    print("approx = {}, theor = {}".format(calc_pi(500), math.pi))