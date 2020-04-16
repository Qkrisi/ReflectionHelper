from inspect import getfullargspec, signature as sig, Parameter
from asyncio import iscoroutinefunction

class MemberInfo:
	def getClass(t):return type(t) if not type(t) is type else t
	def checkForSame(invoke, base):
		if invoke==None:return
		if MemberInfo.getClass(base)!=MemberInfo.getClass(invoke):raise TypeError("The base and invokation type should be the same or None")
	def checkAttribute(invoke, base, name):
		if not hasattr(invoke if invoke!=None else base, name): raise AttributeError(f'{"The" if invoke!=None and not type(invoke) is type else "Static"} attribute "{name}" could not be found')
	def __init__(self, name, e):
		self.e = e
		self.Name=name
		self.baseType = type(self.e) if not type(self.e) is type else self.e
		self.attribute = lambda cl : getattr(cl if cl!=None else self.baseType, self.Name)

class FieldInfo(MemberInfo):
	def SetValue(self, cl, vl):
		MemberInfo.checkForSame(cl, self.e)
		MemberInfo.checkAttribute(cl, self.baseType, self.Name)
		setattr(cl if cl!=None else self.e, self.Name, vl)
	def GetValue(self, cl):
		MemberInfo.checkForSame(cl, self.e)
		MemberInfo.checkAttribute(cl, self.baseType, self.Name)
		return self.attribute(cl)
		
class MethodInfo(MemberInfo):
	def getDefaultArgs(func):
		signature = sig(func)
		return {
			k: v.default
			for k, v in signature.parameters.items()
			if v.default is not Parameter.empty
		}
	
	def __init__(self, name, e):
		super().__init__(name, e)
		try:
			argspec = getfullargspec(self.attribute(self.e))
			self.ReturnType = None if not 'return' in argspec.annotations else argspec.annotations['return']
			s = True
			for arg in argspec.args:
				if arg=="self":
					s=False
					break
			self.IsStatic = s
		except TypeError:
			self.ReturnType = None
			self.IsStatic = True
		self.IsAsync = iscoroutinefunction(self.attribute(self.e))
	def Invoke(self, cl, arr):
		MemberInfo.checkForSame(cl, self.e)
		MemberInfo.checkAttribute(cl, self.baseType, self.Name)
		if not type(arr) is list: raise TypeError("Invoke needs a list of arguments")
		return self.attribute(cl)(*arr)
	async def InvokeAsync(self, cl, arr):
		MemberInfo.checkForSame(cl, self.e)
		MemberInfo.checkAttribute(cl, self.baseType, self.Name)
		if not type(arr) is list: raise TypeError("InvokeAsync needs a list of arguments")
		return await self.attribute(cl)(*arr)
	def GetParameters(self, enableSelf = False) -> list:
		argspec = None
		try:
			argspec = getfullargspec(self.attribute(self.e))
		except TypeError:
			return []
		final = []
		ind = 0
		for arg in argspec.args:
			if enableSelf or arg!="self":
				defaults = MethodInfo.getDefaultArgs(self.attribute(self.e))
				final.append(ParameterInfo(arg, None if not arg in argspec.annotations else argspec.annotations[arg], ind, None if not arg in defaults else defaults[arg], True if arg in defaults else False))
				ind+=1
		return final

class ParameterInfo:
	def __init__(self, name, pt, position, default, hasDefault):
		self.Name = name
		self.ParameterType = pt
		self.Position = position
		self.Default = default
		self.HasDefault, self.Optional = [hasDefault]*2
	def __str__(self):return str(self.ParameterType)
