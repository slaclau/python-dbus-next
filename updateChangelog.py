import distro
import fileinput
import sys

if len(sys.argv) > 0:
    codename = sys.argv[0]
else:
    codename = distro.codename()

for line in fileinput.input("debian/changelog", inplace=True):
    print(line.replace(") replaceme", "~" + codename + ") " + codename), end="")
