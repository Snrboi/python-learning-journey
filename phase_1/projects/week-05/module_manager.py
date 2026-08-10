modules = [
    "profile",
    "calculator",
    "github",
    "settings",
    "ai assistant"
]
print("====AIOS MODULES====")

for index, mode in enumerate(modules, start= 1):
    print(f"{index}: {mode.title()}")
command = input("Enter a module to search for: ").lower()
if command in modules:
    print("Module found!")
else:
    print("Module not found")

new_module = modules.copy()
modules.append("Developer Tools")
print(modules)
print(new_module)
upper_module = [module.upper() for module in modules]
print(upper_module)