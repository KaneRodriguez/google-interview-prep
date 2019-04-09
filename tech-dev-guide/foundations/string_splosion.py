# type: warmup
# url: https://codingbat.com/prob/p118366
# from: https://techdevguide.withgoogle.com/paths/foundational/stringsplosion-problem-ccocodcode/#!
def string_splosion(str):
  ans, prev = "", ""
  for c in str:
    prev += c
    ans += prev
  return ans
