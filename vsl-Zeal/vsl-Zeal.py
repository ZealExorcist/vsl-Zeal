class vsl:
    def __init__(self):
        self.variables = {}

    def assign_variable(self, var_name, value):
        self.variables[var_name] = value

    def get_variable(self, var_name):
        try:
            return self.variables[var_name]
        except KeyError:
            raise ValueError(f"Error: Variable '{var_name}' is not assigned.")
