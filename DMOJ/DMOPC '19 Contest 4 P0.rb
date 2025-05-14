# frozen_string_literal: true

str1 = gets.to_s.chars
str2 = gets.to_s.chars
count = 0

(0...str1.length).each do |i|
  count += 1 if str1[i] != str2[i]
end
if count == 1
  puts("LARRY IS SAVED!")
else
  puts("LARRY IS DEAD!")
end