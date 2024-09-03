tables = [
'Table 1',
'Table 2',
'Table 3',
'Table 4',
'Table 5',
'Table 6',
'Table 7',
'Table 8',
'Table 9',
]


queries = [] 
for i in tables:
    pass
    queries.append(f"""\n%sql
DROP TABLE IF EXISTS {i}""")


# print(queries[:4])
import nbformat as nbf

# Create a new notebook object
nb = nbf.v4.new_notebook()

# Your text lines
# lines = [
#     "print('Hello, World!')",
#     "print('This is a new line.')",
#     "print('Each line will be in a new cell.')"
# ]

lines = queries
# Add each line as a new code cell
for line in lines:
    code_cell = nbf.v4.new_code_cell(line)
    nb.cells.append(code_cell)

# Write the notebook to a file
with open('generated_notebook.ipynb', 'w') as f:
    nbf.write(nb, f)

print("Notebook created successfully!")

