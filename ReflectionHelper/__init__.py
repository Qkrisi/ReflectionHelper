from forbiddenfruit import curse
from ReflectionHelper.ReflectedClasses import FieldInfo, MethodInfo

def GetField(self, n, forceEmpty = False):return FieldInfo(n, self) if forceEmpty or (hasattr(self, n) and not callable(getattr(self, n))) else None
def GetFields(self):
	lst = [i for i in dir(self) if not callable(getattr(self, i)) and not str(i).startswith('__')]
	final = []
	for name in lst:final.append(FieldInfo(name, self))
	return final
	
def GetMethod(self, n):return MethodInfo(n, self) if hasattr(self, n) and callable(getattr(self, n)) else None
def GetMethods(self):
	lst = [i for i in dir(self) if callable(getattr(self, i)) and not str(i).startswith('__')]
	final = []
	for name in lst:final.append(MethodInfo(name, self))
	return final

curse(type, 'GetField', GetField)
curse(type, 'GetFields', GetFields)
curse(type, 'GetMethod', GetMethod)
curse(type, 'GetMethods', GetMethods)
