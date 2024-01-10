import camelcase

# need to install camelcase package with
   # pip install camelcase

   # to check the list do : pip list

   # to unistall camelcase => pip unistall camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt)) #Hello World
