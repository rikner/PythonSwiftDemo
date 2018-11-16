// a typealias for convenience
typealias PythonCallbackPointer = UnsafePointer<@convention(c) (CInt, CFloat)->Void>

// a pointer to a python function
private var callbackPointer: PythonCallbackPointer? = nil

// a function we want to call from python
@_cdecl("native_function")
func demo(intValue: CInt, doubleValue: CDouble) {
    print("Hello From Swift called by Python")
    print("int:", intValue)
    print("double:", doubleValue)

    // call callback if exists
    callbackPointer?.pointee(666, 0.9999)
}

// function with with we can set a callback from python
@_cdecl("set_callback")
func setCallback(pointer: PythonCallbackPointer) {
    callbackPointer = pointer
}
