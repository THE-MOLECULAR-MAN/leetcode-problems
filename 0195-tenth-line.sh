# Read from the file file.txt and output the tenth line to stdout.
# head -n10 --lines 1 file.txt

# awk 'NR==10' file.txt
sed -n 10p file.txt
