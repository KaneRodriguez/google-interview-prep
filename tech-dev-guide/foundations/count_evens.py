# type: warmup
# url: https://codingbat.com/prob/p189616
def count_evens(nums):
  return len(filter(lambda x: x%2 == 0, nums))
