import jpype
import jpype.imports
import os
import copy
compilers="openjdk-asmtools-jasm $1.jbat -w . "
print("\033c\033[47;31m\ngive me file  class: to run ? \n")
#a="Hello.java"
a=input().strip()
b=a.replace(".class","")
os.system(compilers.replace("$1",b)  )
if not jpype.isJVMStarted():
    jpype.startJVM(classpath=["."])
Hello = jpype.JClass(b)

print(Hello.__dir__(""))

jpype.shutdownJVM()