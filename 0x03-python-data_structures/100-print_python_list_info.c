#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - func starts here
* @p: Pyobjcect
*/

void print_python_list_info(PyObject *p)
{
	int indx;
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (indx = 0; indx < size; indx++)
		printf("Element %i: %s\n", indx, Py_TYPE(obj->ob_item[indx])->tp_name);
}
