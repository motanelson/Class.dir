import jpype
import jpype.imports
import os
import copy
print("\033c\033[47;31m\ngive me file  class: to run ? \n")
a="Hello.class"
a=input().strip()
b=a.replace(".class","")
if not jpype.isJVMStarted():
    jpype.startJVM(classpath=["."])
Hello = jpype.JClass(b)

print(Hello.class_.__dir__())
jpype.shutdownJVM()