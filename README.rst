Reflection Helper - Python
==========================

A module that makes reflection easier in Python, based on the C#
System.Reflection library

Installation
------------

Use ``pip3 install ReflectionHelper`` to install the module.
(Python3.7+)

Usage
-----

Import the module using

.. code-block:: python

    from ReflectionHelper import *

| The module adds 4 new functions to the ``type`` class.
| -``GetField``
| -``GetFields``
| -``GetMethod``
| -``GetMethods``

Classes
-------

MemberInfo
~~~~~~~~~~

A parent class storing the datas of the reflected values

FieldInfo
~~~~~~~~~

Iherits ``MemberInfo``

A class storing the reflected field

Methods
~~~~~~~

| **GetValue**
| Gets the value of the field

Returns: ``object``

+-------------+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-----------------+
| Parameter   | Type                                                             | Description                                                                                                            | Default value   |
+=============+==================================================================+========================================================================================================================+=================+
| cl          | The type of the class the field was reflected from or ``None``   | An instance of the class if the field is private; ``None``, instance or the type of the class if the field is static   | -               |
+-------------+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-----------------+

| **SetValue**
| Sets the value of the field

+-------------+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-----------------+
| Parameter   | Type                                                             | Description                                                                                                            | Default value   |
+=============+==================================================================+========================================================================================================================+=================+
| cl          | The type of the class the field was reflected from or ``None``   | An instance of the class if the field is private; ``None``, instance or the type of the class if the field is static   | -               |
+-------------+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-----------------+
| value       | ``object``                                                       | Sets the value of the field in the type to ``value``                                                                   | -               |
+-------------+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-----------------+

Variables
~~~~~~~~~

+------------+-----------+-------------------------+
| Variable   | Type      | Description             |
+============+===========+=========================+
| Name       | ``str``   | The name of the field   |
+------------+-----------+-------------------------+

MethodInfo
~~~~~~~~~~

Inherits ``MemberInfo``

A class storing the reflected method

Methods
~~~~~~~

**Invoke**

Runs the method and returns its result (or ``None`` if it doesn't have
a result)

Returns: ``object``

+-------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-----------------+
| Parameter   | Type                                                              | Description                                                                                                             | Default value   |
+=============+===================================================================+=========================================================================================================================+=================+
| cl          | The type of the class the method was reflected from or ``None``   | An instance of the class if the method is private; ``None``, instance or the type of the class if the field is static   | -               |
+-------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-----------------+
| arr         | List of ``object``                                                | The parameters to call the method with (see example below)                                                              | -               |
+-------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-----------------+

**InvokeAsync**

Asyncronous

Awaits the method and returns its result (or ``None`` if it doesn't
have a result)

Returns ``object``

+-------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-----------------+
| Parameter   | Type                                                              | Description                                                                                                             | Default value   |
+=============+===================================================================+=========================================================================================================================+=================+
| cl          | The type of the class the method was reflected from or ``None``   | An instance of the class if the method is private; ``None``, instance or the type of the class if the field is static   | -               |
+-------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-----------------+
| arr         | List of ``object``                                                | The parameters to call the method with (see example below)                                                              | -               |
+-------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-----------------+

**GetParameters**

Gets the parameters of the reflected method.

Returns: List of ``ParameterInfo``

+--------------+------------+--------------------------------------------------------------------------+-----------------+
| Parameter    | Type       | Description                                                              | Default value   |
+==============+============+==========================================================================+=================+
| enableSelf   | ``bool``   | If it's true, the ``self`` parameter will be returned too (if present)   | False           |
+--------------+------------+--------------------------------------------------------------------------+-----------------+

Variables
~~~~~~~~~

+--------------+------------+------------------------------------------------------+
| Variable     | Type       | Description                                          |
+==============+============+======================================================+
| Name         | ``str``    | The name of the method                               |
+--------------+------------+------------------------------------------------------+
| ReturnType   | ``type``   | The type of the returned value                       |
+--------------+------------+------------------------------------------------------+
| IsStatic     | ``bool``   | True if the method is static, otherwise false        |
+--------------+------------+------------------------------------------------------+
| IsAsync      | ``bool``   | True if the method is asyncronous, otherwise false   |
+--------------+------------+------------------------------------------------------+

ParameterInfo
~~~~~~~~~~~~~

A class storing the informations of a parameter

Printing it will write the type of the parameter.

Variables
~~~~~~~~~

+-------------------------+--------------+----------------------------------------------------------------------------+
| Variable                | Type         | Description                                                                |
+=========================+==============+============================================================================+
| Name                    | ``str``      | The name of the parameter                                                  |
+-------------------------+--------------+----------------------------------------------------------------------------+
| ParameterType           | ``type``     | The type of the parameter                                                  |
+-------------------------+--------------+----------------------------------------------------------------------------+
| Position                | ``int``      | The position of the parameter when calling the method (going from ``0``)   |
+-------------------------+--------------+----------------------------------------------------------------------------+
| Default                 | ``object``   | The default value of the parameter (``None`` if it doesn't have)           |
+-------------------------+--------------+----------------------------------------------------------------------------+
| HasDefault / Optional   | ``bool``     | True if the parameter has a default value, false if it doesn't             |
+-------------------------+--------------+----------------------------------------------------------------------------+

Functions
---------

GetField
~~~~~~~~

Gets a specified field of the type

Returns: ``FieldInfo`` if the field is present or ``forceEmpty`` is
true, otherwise ``None``

+--------------+------------+--------------------------------+-----------------+
| Parameter    | Type       | Description                    | Default value   |
+==============+============+================================+=================+
| name         | ``str``    | The name of the field to get   | -               |
+--------------+------------+--------------------------------+-----------------+
| forceEmpty   | ``bool``   | See description below          | False           |
+--------------+------------+--------------------------------+-----------------+

**forceEmpty**

Python doesn't store the private fields (``self.var``) before the
class gets initialized.

If ``forceEmpty`` is false, using ``type.GetField(str)`` on a private
filed will return ``None``.
But if it's true, it will still return a ``FieldInfo`` based on the
name, but when you try to get the value of it and the field doesn't
exist in the given class, it will raise an ``ArgumentError``.

You can alternatively use ``GetField(class, str)`` to with a
pre-initialized class to get the private field.

GetFields
~~~~~~~~~

Gets all the fields of the type.

Returns: List of ``FieldInfo``

This function has no parameters.

Again, this only returns static variables of the specified type. If you
want to get all the private ones too, use ``GetFields(class)`` with a
pre-initialized class

GetMethod
~~~~~~~~~

Gets the specified method of the type

Returns: ``MethodInfo`` if the method is present, otherwise ``None``

+-------------+--------+---------------------------------+-----------------+
| Parameter   | Type   | Description                     | Default value   |
+=============+========+=================================+=================+
| name        | str    | The name of the method to get   | -               |
+-------------+--------+---------------------------------+-----------------+

GetMethods
~~~~~~~~~~

Gets all the methods of the type-

Returns: List of ``MethodInfo``

This function has no parameters.

Examples
--------

**Getting a static field's value**

Example 1.

.. code-block:: python

    from ReflectionHelper import *

    class Ex:
        f = 0

    Field = Ex.GetField("f")
    print(Field.GetValue(None))
    #Output: 0

Example 2.

.. code-block:: python

    from ReflectionHelper import *

    class Ex:
        f = 0

    Inst = Ex()
    Field = type(Inst).GetField("f")
    print(Field.GetValue(None))
    #Output: 0

**Getting a private field's value**

Example 1.

.. code-block:: python

    from ReflectionHelper import *

    class Ex:
        def __init__(self, val):
            self.f = val

    Field = Ex.GetField("f", True)
    Inst = Ex("Yay")
    print(Field.GetValue(Inst))
    #Output: Yay

Example 2.

.. code-block:: python

    from ReflectionHelper import *

    class Ex:
        def __init__(self, val):
            self.f = val

    Inst = Ex("Yay")
    Field = GetField(Inst, "f")
    print(Field.GetValue(Inst))
    #Output: Yay

**Multiple instances**

.. code-block:: python

    from ReflectionHelper import *

    class Ex:
        def __init__(self, val):
            self.f = val
        
    Inst1 = Ex("First")
    Inst2 = Ex("Second")
    Field = Ex.GetField("f", True)
    print(Field.GetValue(Inst1), Field.GetValue(Inst2))
    #Output: First Second

**Setting a field's value**

.. code-block:: python

    from ReflectionHelper import *

    class Ex:
        def __init__(self, val):
            self.f = val
            
    Inst = Ex("Before")
    Field = Ex.GetField("f", True)
    print(Field.GetValue(Inst))
    Field.SetValue(Inst, "After")
    print(Field.GetValue(Inst))
    #Output:
    #Before
    #After

**Invoking method**

.. code-block:: python

    from ReflectionHelper import *

    class Ex:
        def M(p1, p2):
            print(f"First parameter: {p1}; Second parameter: {p2}")
            
    Method = Ex.GetMethod("M")
    Method.Invoke(None, ["H", "I"])
    #Output: First parameter: H; Second parameter: I

**Invoking async method**

.. code-block:: python

    from ReflectionHelper import *
    import asyncio

    class Ex:
        def __init__(self, seconds):
            self.s = seconds
        
        async def M(self, returnVal):
            await asyncio.sleep(self.s)
            return returnVal
            
    Method = Ex.GetMethod("M")
    Inst = Ex(5)
    print(asyncio.run(Method.InvokeAsync(Inst, ["Returned"])))
    #Output after waiting 5 seconds: Returned

**Get parameters of method**

.. code-block:: python

    from ReflectionHelper import *

    class Ex:
        def M(p1: int, p2: bool, p3, p4 = "Def") -> list:
            return [p1, p2, p3, p4]
            
    Parameters = Ex.GetMethod("M").GetParameters()
    for parameter in Parameters:
        print(f'Parameter data: name is {parameter.Name}, type is {parameter.ParameterType}, position in method is {parameter.Position}, default value is {parameter.Default}')
        
    #Output
    #Parameter data: name is p1, type is <class 'int'>, position in method is 0, default value is None
    #Parameter data: name is p2, type is <class 'bool'>, position in method is 1, default value is None
    #Parameter data: name is p3, type is None, position in method is 2, default value is None
    #Parameter data: name is p4, type is None, position in method is 3, default value is Def

