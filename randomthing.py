def my_function(a, b, c):
    x = 9
    local_vars = locals()
    for var, value in local_vars.items():
        print(f"{var} = {value}")

my_function(1, 2, 3)