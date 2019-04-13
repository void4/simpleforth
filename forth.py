def is_number(s):
	try:
		i = int(s)
		return True
	except ValueError:
		return False

def execute(program, debug=False):
	stack = []
	dictionary = {}
	
	define_function = False
	function_name = None

	program = program.split()
	
	pointer = 0
	
	while True:
		if pointer >= len(program):
			break
		
		command = program[pointer]
		
		if debug:
			print(command)
		
		if define_function and function_name is None:
			function_name = command
			dictionary[function_name] = []
		
		elif define_function and function_name is not None:
			if command == ";":
				define_function = False
				function_name = None
			else:
				dictionary[function_name].append(command)
		
		elif is_number(command):
			number = int(command)
			stack.append(number)
		
		elif command == "+":
			top = stack.pop(-1)
			top2 = stack.pop(-1)
			stack.append(top + top2)
		
		elif command == "-":
			top = stack.pop(-1)
			top2 = stack.pop(-1)
			stack.append(top2-top)
		
		elif command == ":":
			define_function = True
		
		else:
			actions = dictionary[command]
			
			program = program[:pointer+1] + actions + program[pointer+1:]
			
		if debug:
			print("STACK", stack)
			print("DICT", dictionary)
			print(program)
			print("")
			
		pointer += 1

#program = "2 1 -"
program = ": ADD + ; 1 2 ADD 3 4 ADD ADD"
execute(program, debug=True)
