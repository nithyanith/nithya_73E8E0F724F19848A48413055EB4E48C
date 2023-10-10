"""Write a function called linear_Search_Product that takes the list of products and a target product name as input.
The function should perform a linear Search to find the target product in the list and return a list of indices of all occurrences of the product if found"""

def LinearSearchProduct(productList,targetProduct):
  indices = []
  for index,Product in enumerate(productList):
    if Product == targetProduct:
      indices.append(index)
  return indices
#Example usage:
Products = ["Shoes","Boot","Loafer","Shoes","Sandals","Shoes"]
target = "Shoes"
target2 = 'Apple'
result = LinearSearchProduct(Products,target)
print(result)