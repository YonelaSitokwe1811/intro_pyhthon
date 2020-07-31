n=int(input("Enter the start number :"))
printed_values=0
row_length=7
print("\n")
for i in range (n,n+42,1):
  print(i, end='\t')
  printed_values+=1
  if not printed_values%row_length:
    printed_values=0
    print('\n')