#This is a template for the first problem on Project Euler
#!/usr/bin/env ruby
def multiple_sum(number,limit)
  x=limit.divmod(number)[0]
  return number*x*(x+1)/2
end
#This sums multiples of a number up to a given value.

y=multiple_sum(3,999)+multiple_sum(5,999)-multiple_sum(15,999)
puts y