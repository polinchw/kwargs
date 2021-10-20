# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(**kwargs):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {kwargs["name"]}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_dict(**kwargs):
    print(kwargs["d"]["dictA"]["name"])

def print_dict_more(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(kwargs["d"]["dictA"]["name"])




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(name='Bill')
    nested_dict = {'dictA': {'name': 'Bill'},
                   'dictB': {'name': 'Bob'}}
    print_dict(d=nested_dict)
    print_dict_more('hi','there',d=nested_dict)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
