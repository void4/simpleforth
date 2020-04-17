def is_number(s):
	try:
		i = int(s)
		return True
	except ValueError:
		return False

def find_nth(l, x, s=0, inc=None, n=0):

	if inc is None:
		inc = []

	i = s
	while i < len(l):
		if l[i] == x:
			if n == 0:
				return i
			n -= 1

		elif l[i] in inc:
			n += 1

		i += 1

	return -1

def execute(program, debug=False):
	stack = []
	dictionary = {}

	define_function = False
	function_name = None

	program = program.split()

	if debug:
		print(program)

	pointer = 0

	def pop():
		return stack.pop(-1)

	def popn(n):
		return [pop() for i in range(n)][::-1]

	def push(v):
		stack.append(v)


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
			push(number)

		elif command == "+":
			a,b = popn(2)
			push(a + b)

		elif command == "-":
			a,b = popn(2)
			push(a - b)

		elif command == "pop":
			pop()

		elif command == "print":
			print(pop())

		elif command == "=":
			a,b = popn(2)
			push(1 if a==b else 0)

		elif command == "if":
			truth = pop()
			if not truth:
				elseindex = find_nth(program, "else", pointer, ["if"])
				thenindex = find_nth(program, "then", pointer, ["if"])
				if elseindex != -1 and elseindex < thenindex:
					# Pointer increased by 1 more at the end of loop
					pointer = elseindex
				elif thenindex != -1:
					pointer = thenindex

		elif command == "else":
			thenindex = find_nth(program, "then", pointer, ["if"])
			if thenindex != -1:
				pointer = thenindex

		elif command == "then":
			pass

		elif command == ":":
			define_function = True

		else:
			actions = dictionary[command]

			program = program[:pointer] + actions + program[pointer+1:]

		if debug:
			print("STACK", stack)
			print("DICT", dictionary)
			print("")

		pointer += 1

#program = "2 1 -"
program = ": ADD + ; 1 2 ADD 3 4 ADD ADD"
program = "1 2 = if 42 print else 666 print then 9 pop"
execute(program, debug=True)
