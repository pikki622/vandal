# coloring.
from colorama import (
    Fore,
    Back,
    Style,
    init,
)

init()

# dependencies.
import pandas as pd
import os
import random
from logistics.plugins.types import *

'''

(MODULE FUNCTIONS)
------------------

vandal.toolkit is a set of data manipulation tools that can be directly accessed from the main module as vandal.any_function_listed_below()

        random_value(mean, st_dev, **rounded) - gives a random value of mean and standard deviation inputed, if rounded = 'y', value will be rounded.

        random_pool(mean, st_dev, pool_size, **rounded) - gives random values of mean and standard deviation inputed for the amount of values defined in the pool size, if rounded = 'y', values will be rounded.

        split_values(data, split_method) - splits the data using a split method character.

        join_values(data, join_method) - joins the data using a join metod character.

        replace_values(data, replaced_value, replacing_value) - replaces a defined value with a desired value.

        list_sort(data, array) - manually sorts data depending on defined array of indexes.

        index_sort(data, split_method, index_array) - sorts the indicies in a list of values based on the index array defined as [x,x,x].

        auto_sort(data, split_method, trigger = lambda x: x[0]) - automatically splits all values in a list and sorts them based on the added trigger as lambda x: [x[i], x[i]] and joins them back together.

	create_password(length) - creates a random password with adjustable lenght (default: length = 8).

        save_to(file, prefix, func_name, choice) - file saver for code clarity.

        file_handler(file) - handles the file extenstion upon import.
        
        paint_text(text, color, print_trigger) - paints the text with a desired color ('fr', 'fg', 'fb', 'fk', 'fc', 'fm', 'fy', 'br', 'bg', 'bb', 'bk', 'bc', 'bm', 'by').
	
'''

# metadata of the used library.
from vandal.misc._meta import (
	__author__,
	__copyright__,
	__credits__,
	__license__,
	__version__,
	__documentation__,
	__contact__,
	__donate__
)

# gives a random value of mean and standard deviation inputed, if rounded = 'y', value will be rounded.
def random_value(mean, st_dev, **rounded):
        return (round(random.gauss(mean, st_dev)) if
                rounded.get('rounded') == 'y' else random.gauss(mean, st_dev))

# gives random values of mean and standard deviation inputed for the amount of values defined in the pool size, if rounded = 'y', values will be rounded.
def random_pool(mean, st_dev, pool_size, **rounded):
        return ([round(random.gauss(mean, st_dev))
                 for _ in range(pool_size)] if rounded.get('rounded') == 'y'
                else [random.gauss(mean, st_dev) for _ in range(pool_size)])

# splits the data using a split method character.
def split_values(data, split_method):
        return [i.split(split_method) for i in data]

# joins the data using a join metod character.
def join_values(data, join_method):
        return [join_method.join(i) for i in data]

# replaces a defined value with a desired value.
def replace_values(data, replaced_value, replacing_value):
        replaced_values = [i.split(replaced_value) for i in data]
        return [replacing_value.join(i) for i in replaced_values]

# manually sorts data depending on defined array of indexes.
def list_sort(data, array):
        return [data[d] for d in array]

# sorts the indicies in a list of values based on the index array defined as [x,x,x].
def index_sort(data, split_method, index_array):
        remixed_data = []
        array_count = 0
        result = [i.split(split_method) for i in data]
        array_lenght = len(result)
        for i in result:
                y1 = [i[x] for x in index_array]
                remixed_data += [split_method.join(y1)]
                if array_count == array_lenght:
                        break
                array_count += 1

        return remixed_data

# automatically splits all values in a list and sorts them based on the added trigger as lambda x: [x[i], x[i]] and joins them back together.
def auto_sort(data, split_method, trigger = lambda x: x[0]):
        split_values = [i.split(split_method) for i in data]
        auto_sort = sorted(split_values, key = trigger)
        return ['-'.join(i) for i in auto_sort]

# creates a random password with adjustable lenght (default: length = 8).
def create_password(length = 8):
        particles = 'abcdefghijklmnoprstuxwyzqABCDEFGHIJKLMNOPRSTUXWYZQ0123456789'
        return ''.join(random.sample(particles, length))

# handles the file extenstion upon import.
def file_handler(file):
        file = file.replace("'", '"').strip('"')
        if str(file).endswith('.csv'):
            data = pd.read_csv(file)
            print(Fore.YELLOW + '\nAVAILABLE COLUMNS' + Fore.RESET)
            for col in data.columns:
                print(col)
        elif str(file).endswith('.xlsx'):
            data = pd.read_excel(file)
            print(Fore.YELLOW + '\nAVAILABLE COLUMNS' + Fore.RESET)
            for col in data.columns:
                print(col)
        elif str(file).endswith('.json'):
            data = pd.read_json(file)
            print(Fore.YELLOW + '\nAVAILABLE COLUMNS' + Fore.RESET)
            for col in data.columns:
                print(col)
        else:
            raise Exception('=== ONLY CSV, XLSX AND JSON FILES SUPPORTED. ===\n')
        file_col = input('\nEnter column name: ').replace("'", '"').strip('"')
        try:
            data = data[file_col]
            return data
        except:
            raise Exception('=== INVALID COLUMN NAME. ===\n')

# file saver for code clarity.
def save_to(file, prefix, func_name, choice):
        if choice in ['0', 'csv']:
                extension = '.csv'
                file.to_csv(prefix + func_name + extension)
                print(Fore.YELLOW + os.path.join(os.getcwd() + '\\' + prefix + func_name + extension) + Fore.RESET)
        elif choice in ['1', 'xlsx']:
                extension = '.xlsx'
                file.to_excel(prefix + func_name + extension)
                print(Fore.YELLOW + os.path.join(os.getcwd() + '\\' + prefix + func_name + extension) + Fore.RESET)
        elif choice in ['2', 'json']:
                extension = '.json'
                file.to_json(prefix + func_name + extension)
                print(Fore.YELLOW + os.path.join(os.getcwd() + '\\' + prefix + func_name + extension) + Fore.RESET)
        else:
                print('=== NO OPTION CHOSEN, EXITING THE MENU... ===\n')

# >>> DEPRECATED AND MIGHT BE REMOVED IN THE FUTURE. THIS FUNCTION HAS BEEN MIGRATED TO THE LOGISTICS LIBRARY INSTEAD. <<<
# paints the text with a desired color ('Fr', 'Fg', 'Fb', 'Fk', 'Fc', 'Fm', 'Fy', 'Fw', 'Br', 'Bg', 'Bb', 'Bk', 'Bc', 'Bm', 'By', 'Bw').
def paint_text(
        text : StringType,
        color : StringType,
        print_trigger : BooleanType = True
        ) -> StringType:
        
        '''
        * coloring of CLI.
        
        - text - desired text to print.
        - color - desired color to print in.
        - print_trigger (True/False) - modify return type.
        '''
        
        # Fore coloring.
        colors = {
            'Fr' : Fore.RED,
            'Fg' : Fore.GREEN,
            'Fb' : Fore.BLUE,
            'Fk' : Fore.BLACK,
            'Fm' : Fore.MAGENTA,
            'Fy' : Fore.YELLOW,
            'Fc' : Fore.CYAN,
            'Fw' : Fore.WHITE,
            
        # Back coloring.
            'Br' : Back.RED,
            'Bg' : Back.GREEN,
            'Bb' : Back.BLUE,
            'Bk' : Back.BLACK,
            'Bm' : Back.MAGENTA,
            'By' : Back.YELLOW,
            'Bc' : Back.CYAN,
            'Bw' : Back.WHITE,
            }
        
        if print_trigger == True:
            return print(colors[color] + str(text) + Style.RESET_ALL)
        
        elif print_trigger == False:
            return colors[color] + str(text) + Style.RESET_ALL
