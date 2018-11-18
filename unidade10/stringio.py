import io

string = 'String normal'

f = io.StringIO(string)
f.read()
f.write(' \nOutra linha.')

f.seek(0)
print(f.readlines())

