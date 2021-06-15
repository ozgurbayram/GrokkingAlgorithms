import time
## Binary Searhch
def binarySearch(a,i):
	# Low and High index's of array
	low = 0 
	high = len(a)-1
	
	# Counter
	count = 0

	while low<=high:
		mid =round((low+high)/2)
		guess = a[mid]
		if guess == i:
			return f'Found at {mid} after {count} calculation '
		if guess >i:
			high = mid-1
			# Theses 3 line of code just for visualization
			time.sleep(1)
			print(a[low:high])
			count +=1
		else:
			low = mid +1
			# Theses 3 line of code just for visualization
			time.sleep(1)
			print(a[low:high])
			count +=1

	return None
			
if __name__ == '__main__':
	arr = list(range(64))

	print(binarySearch(arr,5))
