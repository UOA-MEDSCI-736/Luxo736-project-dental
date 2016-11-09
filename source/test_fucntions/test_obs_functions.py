from obs_functions import *

#trtying to test a string that is not a File path
def test_file_name_string():
    # setup i.e. dummy parameters
    input_filename = "hola"
    exp_output = None
    
    # call the function
    real_output = read_my_file(input_filename)
    
    # compare
    assert real_output == exp_output


#trying to pass a number as an argument to read_my_file function
def test_pass_number():
    # setup i.e. dummy parameters
    input_filename = 123
    exp_output = None
    
    # call the function
    real_output = read_my_file(input_filename)
    
    # compare
    assert real_output == exp_output
