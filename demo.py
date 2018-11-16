from ctypes import CDLL, byref, c_double, c_float, c_int, CFUNCTYPE
import subprocess

def main():
    # load library
    demo_lib = CDLL(library_path())
    
    # pass callback function by reference to our native code
    demo_lib.set_callback(byref(callable_from_native))

    # call swift function with c type parameters
    demo_lib.native_function(c_int(42), c_double(0.123))


def library_path():
    process = subprocess.run(['swift', 'build', '--show-bin-path'], stdout=subprocess.PIPE)
    bin_path = process.stdout.decode('utf-8').rstrip('\n\r')
    return bin_path + '/libDemo.dylib'


# specifiy return and argument type via @CFUNCTYPE
# in order to be able to call this function from native code
@CFUNCTYPE(None, c_int, c_float)
def callable_from_native(intValue, floatValue):
    print("Hello from Python called by Swift")
    print("int:", intValue)
    print("float:", floatValue)


if __name__ == "__main__":
    main()


