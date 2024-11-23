import os

# Create the 'tmp' directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate ani files with looping feature
animation1 = "Animation 1 with continuous loop"
animation2 = "Animation 2 with loop 3 times"

ani_file1 = open('./tmp/animation1.ani', 'w')
ani_file1.write(animation1)
ani_file1.close()

ani_file2 = open('./tmp/animation2.ani', 'w')
ani_file2.write(animation2)
ani_file2.close()