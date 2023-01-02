sample_dict={
    'physics':82,
    'maths':88,
    'computers': 75
    }
print(min(sample_dict,key=sample_dict.get))

print(sample_dict.get('maths'))
print(sample_dict.get('CRT'))
