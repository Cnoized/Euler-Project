#This program determines the largest factor of a given number.
#!/usr/bin/env ruby
puts "This program gives back the prime factorization of a number."
print "Number: "
number=gets.to_i
x=2
array=[]
y=number
while x!=number && number!=1 do 
  while number%x==0
    array.concat([x])
    number/=x
	y=number
	puts number
  end
  x+=1
end
if x==number
  array.concat([x])
  puts number
end

print "Prime factorization is: #{array}"