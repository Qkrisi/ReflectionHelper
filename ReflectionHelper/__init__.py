from forbiddenfruit import curse
from ReflectionHelper.ReflectedClasses import FieldInfo, MethodInfo

def GetField(self, name : str, forceEmpty = False):
	if not type(name) is str:raise TypeError("Name should be a string")
	if not type(forceEmpty) is bool:raise TypeError("forceEmpty should be a bool")
	return FieldInfo(name, self) if forceEmpty or (hasattr(self, name) and not callable(getattr(self, name))) else None
def GetFields(self):
	lst = [i for i in dir(self) if not callable(getattr(self, i)) and not str(i).startswith('__')]
	final = []
	for name in lst:final.append(FieldInfo(name, self))
	return final
	
def GetMethod(self, name : str):
	if not type(name) is str:raise TypeError("Name should be a string")
	return MethodInfo(name, self) if hasattr(self, name) and callable(getattr(self, name)) else None
def GetMethods(self):
	lst = [i for i in dir(self) if callable(getattr(self, i)) and not str(i).startswith('__')]
	final = []
	for name in lst:final.append(MethodInfo(name, self))
	return final

curse(type, 'GetField', GetField)
curse(type, 'GetFields', GetFields)
curse(type, 'GetMethod', GetMethod)
curse(type, 'GetMethods', GetMethods)
