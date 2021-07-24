#This program calculates the fibbinoci numbers below 4 million, and adds up the even ones.
#!/usr/bin/env ruby
array=[1,2]
alpha=1
sum=0
while array[alpha]<4000000 do
   if array[alpha]%2==0
     sum+=array[alpha]
   end
   array.concat([array[alpha-1]+array[alpha]])
   alpha+=1
end
puts sum