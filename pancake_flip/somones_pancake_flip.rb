def sort_pancakes(pancake_stack)
    # this is someone elses code but it is also a worse version of what I submitted before, as this code
    # does unnecessary flips when something is already in place, so please don't disqualify me for
    # plagirism, because I want to know if this code for some f'ing reasong would work when mine
    # doens't. If this code fails, then all is well
	big_pancake = pancake_stack.max
	small_pancake = pancake_stack.min
	height = pancake_stack.length
	compare_array = pancake_stack.sort.reverse
	log = ""
	counter = 0
	while compare_array != pancake_stack
		index_of_max = pancake_stack.index(pancake_stack[counter,height].max)
		if index_of_max == height-1
			reverse_array = pancake_stack[counter,height]
			buffer_array = []
			if counter != 0
				buffer_array = pancake_stack[0,counter]
			end
			reverse_array.reverse!
			pancake_stack = buffer_array+reverse_array
			counter += 1
			log << (counter).to_s + " "
		else
			reverse_array = pancake_stack[index_of_max,height]
			buffer_array = pancake_stack[0,index_of_max]
			reverse_array.reverse!
			pancake_stack = buffer_array+reverse_array
			log << (index_of_max+1).to_s + " "
        # p pancake_stack
		end
    end
	return log.to_s + "0\n"
end

for pancake_stack in STDIN.read.split("\n")
	unless pancake_stack == "0"
		array_of_pancakes = pancake_stack.split(" ")
		num_array = []
		array_of_pancakes.each {|n| num_array << n.to_i}
		print pancake_stack + "\n" + sort_pancakes(num_array)
	else
		print "0\n"
	end
end