def recursive_function(target, current):
    if current <= target:
        print(current)
        recursive_function(target,current+1)


length = int(input('Enter the askdfalksdjf'))

recursive_function(length, 0)