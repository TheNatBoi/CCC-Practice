# frozen_string_literal: true

T = gets.to_i
(1..T).each { |i|
  N = gets.to_i
  max = 0
  (1..N).each { |j|
    F = gets.to_i
    if max < F
      max = F
    end
  }
  puts(max)
}